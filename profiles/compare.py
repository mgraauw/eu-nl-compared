import enum
import json
import pathlib

package_paths = {
    "ips": pathlib.Path(".") / "packages" / "hl7.fhir.uv.ips-1.1.0",
    "eps": pathlib.Path(".") / "packages" / "hl7.fhir.eu.eps-0.0.1",
    "zib2017": pathlib.Path(".") / "packages" / "nictiz.fhir.nl.stu3.zib2017-2.2.20",
    "zib2020": pathlib.Path(".") / "packages" / "nictiz.fhir.nl.r4.zib2020-0.11.0-beta.1"
}

class Profile:
    def __init__(self, package, profile_name, base = None):
        self.package = package
        self.name = profile_name

        content = self.read()
        
        # Fish out interesting data: min and max cardinality and binding strengths
        self.of_interest = [el["path"] for el in content["differential"]["element"] if "min" in el or "max" in el or "binding" in el or "type" in el]
        if base:
            # Unify with the things marked as interesting by the base
            self.of_interest = list(set(self.of_interest + base.of_interest))

    def read(self):
        if self.package in ["ips", "eps"]:
            file = package_paths[self.package] / f"StructureDefinition-{self.name}.json"
        else:
            file = package_paths[self.package] / f"{self.name}.json"

        with open(file) as fd:
            content = json.load(fd)

        return content

class Compatibility(enum.StrEnum):
    compatible = enum.auto()
    incompatible = enum.auto()
    soft_incompatible = "soft incompatible"
    manual = enum.auto()

class Comparator:
    def __init__(self, checked_findings_file):
        self.checked_findings_file = pathlib.Path(".") / checked_findings_file

    def fits_in(self, first, second):
        self.first = first
        self.second = second

        self.findings = []
        try:
            with open(self.checked_findings_file) as f:
                self.checked_findings = json.load(f)[f"{first.name} ({first.package}) fits in {second.name} ({second.package})"]
        except KeyError:
            self.checked_findings = {}

        first_snap = first.read()["snapshot"]["element"]
        second_snap = second.read()["snapshot"]["element"]
        
        # If we want to know if we "fit in" the other, we have to look at the restrictions done by the other and see
        # if we're compatible. We don't need to look at our own restrictions
        for self.path in second.of_interest:
            try:
                first_el = list(filter(lambda e: e["path"] == self.path, first_snap))[0]
                second_el = list(filter(lambda e: e["path"] == self.path, second_snap))[0]
            except IndexError:
                # Happens when we have extensions. Need to look into this
                continue

            self._checkMinMax(first_el, second_el)
            self._checkBinding(first_el, second_el)
            self._checkTypes(first_el, second_el)

        result = []
        if len(self.findings):
            result.append(f"x {first.name} ({first.package}) does not seem to fit in {second.name} ({second.package})"),
            for finding in self.findings:
                result.append(f"* {finding}")
        else:
            result.append(f"+ {first.name} ({first.package}) does seem to fit in {second.name} ({second.package}).")
        return result

    def _checkMinMax(self, first_el, second_el):
        if second_el["min"] > first_el["min"]:
            self._finding(f"required in {self.second.name} but optional in {self.first.name}.")

        if second_el["max"] != "*": # if other is unrestricted we always fit
            if first_el["max"] == "*":
                 self._finding(f"restricted to {second_el['max']} in {self.second.name} but unrestricted in {self.first.name}.")
            else:
                self_max = int(first_el["max"])
                other_max = int(second_el["max"])
                if self_max > other_max:
                    self._finding(f"restricted to {other_max} in {other_name} but to {self_max} in {self.first.name}.")

    def _checkBinding(self, first_el, second_el):
        if "binding" not in second_el:
            return

        first_vs = self._getBoundValueSet(first_el)
        second_vs = self._getBoundValueSet(second_el)
        vs_handled = self._isChecked("valueSet", first_vs, second_vs)
        bs_handled = self._isChecked("strength", first_el["binding"]["strength"], second_el["binding"]["strength"])

        if first_vs == second_vs and not bs_handled:
            if second_el["binding"]["strength"] == "required" and first_el["binding"]["strength"] != "required":
                self._finding(f"required binding in {self.second.name} is more restrictive than {first_el['binding']['strength']} binding in {self.first.name}.")
            elif second_el["binding"]["strength"] == "extensible" and first_el["binding"]["strength"] not in ["extensible", "required"]:
                self._finding(f"extensible binding in {self.second.name} is more restrictive than {first_el['binding']['strength']} binding in {self.first.name}.")
            else:
                # We don't care much about other differences
                pass
        if first_vs != second_vs and not vs_handled:
            if second_el["binding"]["strength"] == "required":
                if first_el["binding"]["strength"] == "required":
                    self._finding(f"required Valueset in {self.second.name} differs from required ValueSet in {self.first.name}. Manual check needed.", Compatibility.manual)
                else:
                    self._finding(f"required Valueset in {self.second.name} is more restrictive than {self.first.name}.")
            elif second_el["binding"]["strength"] == "extensible":
                self._finding(f"extensible Valueset in {self.second.name} differs from {self.first.name}. Manual check needed.", Compatibility.manual)
            else:
                self._finding("differences in Valueset preferences. Manual check needed.", Compatibility.manual)

    def _checkTypes(self, first_el, second_el):
        if "type" in second_el:
            self_types = {t["code"] for t in first_el["type"] if "code" in t}
            other_types = {t["code"] for t in second_el["type"] if "code" in t}

            if not self._isChecked("type", self_types, other_types):
                if self_types > other_types:
                    self._finding(f"{self.second.name} restricts types to {other_types}, which is narrower than the allowed types in {self.first.name}.")
                elif self_types.isdisjoint(other_types):
                    self._finding(f"{self.second.name} restricts types to {other_types}, while {self.first.name} restricts them to {self_types}.")

    def _getBoundValueSet(self, snapshot_element):
        vs = None
        if "valueSetReference" in snapshot_element["binding"]:
            vs = snapshot_element["binding"]["valueSetReference"]["reference"]
        else:
            vs = snapshot_element["binding"]["valueSet"]
        return vs.split("|")[0] # Cut of version number

    def _isChecked(self, key, first, second):
        """
        Check if the incompatibility is described in the checked findings file and act accordingly.
        That is:
        - if the supplied "first" and "second" match the values for "self" and "other" under the "key", the finding
          is described.
        - if they don't match, something has changed apparently and this is flagged.
        - if they do match and "compatibility" is set to "compatible", then they are regarded compatible. If 
          "compatibility" is absent, a hard incompatibility is assumed.
        - if they are not compatible or if a "finding" is defined, a finding is is created with the proper
          compatibility level.
        """

        if self.path in self.checked_findings:
            if key in self.checked_findings[self.path]:
                ex = self.checked_findings[self.path][key]
                compatibility = Compatibility.incompatible if "compatibility" not in ex else Compatibility(ex["compatibility"])
                
                self_value = ex["self"]
                other_value = ex["other"]
                if type(self_value) == list: self_value = set(self_value)    # Comparison is done on sets so order doesn't matter
                if type(other_value) == list: other_value = set(other_value)

                if self_value == first and other_value == second:
                    if "finding" in ex:
                        self._finding(ex["finding"], compatibility)
                    elif compatibility != Compatibility.compatible:
                        self._finding("Documented incompatibility", compatibility)
                    else:
                        # Silently ignore documented compatibility without message
                        pass
                    return True
                else:
                    self._finding("Documented finding is outdated. Please re-check.", Compatibility.manual)
        return False

    def _finding(self, message, severity: Compatibility = Compatibility.incompatible):
        if severity == Compatibility.compatible:
            symbol = "+"
        elif severity == Compatibility.soft_incompatible:
            symbol = "~"
        elif severity == Compatibility.manual:
            symbol = "?"
        else:
            symbol = "x"
        self.findings.append(f"{symbol} {self.path}: {message}")

if __name__ == "__main__":
    comparator = Comparator("checked-findings.json")

    zib_Problem2017 = Profile("zib2017", "zib-Problem")
    zib_Problem2020 = Profile("zib2020", "zib-Problem")
    Condition_uv_ips = Profile("ips", "Condition-uv-ips")
    Condition_eu_eps = Profile("eps", "Condition-eu-eps", Condition_uv_ips)
    with open(pathlib.Path(".") / "results" / "Condition.md", "w") as f:
        f.write("# Condition resources\n")
        f.write("## zib-Problem (2017) <-> Condition-uv-ips\n")
        for line in comparator.fits_in(zib_Problem2017, Condition_eu_eps):
            f.write(line + "\n")
        f.write("\n")
        for line in comparator.fits_in(Condition_eu_eps, zib_Problem2017):
            f.write(line + "\n")
        # f.write("\n\n")
        # f.write("## zib-Problem (2020) <-> Condition-uv-ips\n")
        # for line in comparator.fits_in(zib_Problem2020, Condition_eu_eps):
        #     f.write(line + "\n")
        # f.write("\n")
        # for line in comparator.fits_in(Condition_eu_eps, zib_Problem2020):
        #     f.write(line + "\n")
