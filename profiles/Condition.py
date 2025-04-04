import pathlib
from compare import Comparator, Profile

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
        f.write("\n\n")
        f.write("## zib-Problem (2020) <-> Condition-uv-ips\n")
        for line in comparator.fits_in(zib_Problem2020, Condition_eu_eps):
            f.write(line + "\n")
        f.write("\n")
        for line in comparator.fits_in(Condition_eu_eps, zib_Problem2020):
            f.write(line + "\n")
