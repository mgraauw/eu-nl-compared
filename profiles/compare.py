import json
import pathlib

package_paths = {
    "ips": pathlib.Path(".") / "packages" / "hl7.fhir.uv.ips-1.1.0",
    "zib2017": pathlib.Path(".") / "packages" / "nictiz.fhir.nl.stu3.zib2017-2.2.20",
    "zib2020": pathlib.Path(".") / "packages" / "nictiz.fhir.nl.r4.zib2020-0.11.0-beta.1"
}

class Profile:
    def __init__(self, package, profile_name):
        self.package = package
        self.name = profile_name

        content = self.read()
        
        # Fish out interesting data: min and max cardinality and binding strengths
        self.of_interest = [el["path"] for el in content["differential"]["element"] if "min" in el or "max" in el or "binding" in el or "type" in el]

    def read(self):
        if self.package == "ips":
            file = package_paths[self.package] / f"StructureDefinition-{self.name}.json"
        else:
            file = package_paths[self.package] / f"{self.name}.json"

        with open(file) as fd:
            content = json.load(fd)

        return content

class Comparator:
    def __init__(self, exceptions_file):
        self.exceptions_file = pathlib.Path(".") / exceptions_file

    def fits_in(self, first, second):
        self.first = first
        self.second = second

        self.findings = []
        try:
            with open(self.exceptions_file) as f:
                self.exceptions = json.load(f)[f"{first.name} ({first.package}) fits in {second.name} ({second.package})"]
        except KeyError:
            self.exceptions = {}

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
        if "binding" in second_el:
            first_vs = self._getBoundValueSet(first_el)
            second_vs = self._getBoundValueSet(second_el)
            print(self.path, first_vs, second_vs, first_el["binding"]["strength"], second_el["binding"]["strength"])

            if self.path in self.exceptions:
                if "valueSet" in self.exceptions[self.path]:
                    known_self = self.exceptions[self.path]["valueSet"]["self"]
                    known_other = self.exceptions[self.path]["valueSet"]["other"]
                    if known_self == first_vs and known_other == second_vs:
                        if "comment" in self.exceptions[self.path]["valueSet"]:
                            self._finding(self.exceptions[self.path]["valueSet"]["comment"], "checked")
                        # We don't have to flag on ValueSet differences anymore, but still on binding strengths, so we
                        # simply set both ValueSets to empty
                        first_vs = second_vs = ""

            if first_vs != second_vs:
                if second_el["binding"]["strength"] == "required":
                    self._finding(f"required Valueset in {self.second.name} differs from {self.first.name}. Manual check needed.", "manual")
                elif second_el["binding"]["strength"] == "extensible":
                    self._finding(f"extensible Valueset in {self.second.name} differs from {self.first.name}. Manual check needed.", "manual")
                else:
                    self._finding("differences in Valueset preferences. Manual check needed.", "manual")
            else:
                if second_el["binding"]["strength"] == "required" and first_el["binding"]["strength"] != "required":
                    self._finding(f"required binding in {self.second.name} is more restrictive than {first_el['binding']['strength']} binding in {self.first.name}.")
                elif second_el["binding"]["strength"] == "extensible" and first_el["binding"]["strength"] not in ["extensbile", "required"]:
                    self._finding(path, f"extensible ValueSet in {self.second.name} is more restrictive than {first_el['binding']['strength']} binding in {self.first.name}.")
                else:
                    # We don't care much about other differences
                    pass

    def _checkTypes(self, first_el, second_el):
        if "type" in second_el:
            self_types = {t["code"] for t in first_el["type"] if "code" in t}
            other_types = {t["code"] for t in second_el["type"] if "code" in t}

            try:
                known_self = set(self.exceptions[self.path]["type"]["self"])
                known_other = set(self.exceptions[self.path]["type"]["other"])
                if known_self == self_types and known_other == other_types:
                    return
            except KeyError:
                # Nothing in exceptions about this, let's continue
                pass

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

    def _finding(self, message, severity = "error"):
        if severity == "checked":
            symbol = "."
        elif severity == "manual":
            symbol = "?"
        else:
            symbol = "x"
        self.findings.append(f"{symbol} {self.path}: {message}")

if __name__ == "__main__":
    comparator = Comparator("exceptions.json")

    zib_Problem2017 = Profile("zib2017", "zib-Problem")
    zib_Problem2020 = Profile("zib2020", "zib-Problem")
    Condition_uv_ips = Profile("ips", "Condition-uv-ips")
    for line in comparator.fits_in(zib_Problem2017, Condition_uv_ips):
        print(line)
    #with open(pathlib.Path(".") / "results" / "Condition.md", "w") as f:
    #write(f, "# Condition resources")
    #write(f, "## zib-Problem (2017) <-> Condition-uv-ips")
    #write(f, *zib_Problem2017.fits_in(Condition_uv_ips, ignored_file))
    #write(f)
    #write(f, *Condition_uv_ips.fits_in(zib_Problem2017, ignored_file))
    #write(f)
    #write(f, "## zib-Problem (2020) <-> Condition-uv-ips")
    #write(f, *zib_Problem2020.fits_in(Condition_uv_ips, ignored_file))
    #write(f)
    #write(f, *Condition_uv_ips.fits_in(zib_Problem2020, ignored_file))