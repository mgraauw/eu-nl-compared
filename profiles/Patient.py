import pathlib
from compare import Comparator, Profile

if __name__ == "__main__":
    comparator = Comparator("checked-findings.json")

    nl_core_patient_2017 = Profile("zib2017", "nl-core-patient")
    zib_Patient2020 = Profile("zib2020", "zib-Patient")
    Patient_uv_ips = Profile("ips", "Patient-uv-ips")
    Patient_eu_eps = Profile("eps", "Patient-eu-eps", Patient_uv_ips)
    with open(pathlib.Path(".") / "results" / "Patient.md", "w") as f:
        f.write("# Patient profiles\n")
        f.write("## nl-core-patient (2017) <-> Patient-uv-ips\n")
        for line in comparator.fits_in(nl_core_patient_2017, Patient_eu_eps):
            f.write(line + "\n")
        f.write("\n")
        for line in comparator.fits_in(Patient_eu_eps, nl_core_patient_2017):
            f.write(line + "\n")
        f.write("\n\n")
        f.write("## zib-Patient (2020) <-> Patient-uv-ips\n")
        for line in comparator.fits_in(zib_Patient2020, Patient_eu_eps):
            f.write(line + "\n")
        f.write("\n")
        for line in comparator.fits_in(Patient_eu_eps, zib_Patient2020):
            f.write(line + "\n")

    # TODO: Compare name, address