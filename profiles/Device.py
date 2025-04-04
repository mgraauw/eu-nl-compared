import pathlib
from compare import Comparator, Profile

if __name__ == "__main__":
    comparator = Comparator("checked-findings.json")

    zib_MedicalDevice2017 = Profile("zib2017", "zib-MedicalDevice")
    zib_MedicalDeviceProduct2017 = Profile("zib2017", "zib-MedicalDeviceProduct")
    zib_MedicalDevice2020 = Profile("zib2020", "zib-MedicalDevice")
    zib_MedicalDeviceProduct2020 = Profile("zib2020", "zib-MedicalDevice.Product")
    DeviceUseStatement_uv_ips = Profile("ips", "DeviceUseStatement-uv-ips")
    DeviceUseStatement_eu_eps = Profile("eps", "DeviceUseStatement-eu-eps", DeviceUseStatement_uv_ips)
    Device_uv_ips = Profile("ips", "Device-uv-ips")
    Device_eu_eps = Profile("eps", "Device-eu-eps", Device_uv_ips)
    with open(pathlib.Path(".") / "results" / "Device.md", "w") as f:
        f.write("# DeviceUseStatement/Device profiles\n")
        f.write("## zib 2017 <-> EPS\n")
        f.write("### zib-MedicalDevice (2017) <-> DeviceUseStatement-eu-eps\n")
        for line in comparator.fits_in(zib_MedicalDevice2017, DeviceUseStatement_eu_eps):
            f.write(line + "\n")
        f.write("\n")
        for line in comparator.fits_in(zib_MedicalDeviceProduct2017, Device_eu_eps):
            f.write(line + "\n")
        f.write("\n")
        for line in comparator.fits_in(DeviceUseStatement_eu_eps, zib_MedicalDevice2017):
            f.write(line + "\n")
        f.write("\n")
        for line in comparator.fits_in(Device_eu_eps, zib_MedicalDeviceProduct2017):
            f.write(line + "\n")
        f.write("\n\n")
        f.write("### zib-MedicalDevice (2020) <-> DeviceUseStatement-eu-eps\n")
        for line in comparator.fits_in(zib_MedicalDevice2020, DeviceUseStatement_eu_eps):
            f.write(line + "\n")
        f.write("\n")
        for line in comparator.fits_in(zib_MedicalDeviceProduct2020, Device_eu_eps):
            f.write(line + "\n")
        f.write("\n")
        for line in comparator.fits_in(DeviceUseStatement_eu_eps, zib_MedicalDevice2020):
            f.write(line + "\n")
        f.write("\n")
        for line in comparator.fits_in(Device_eu_eps, zib_MedicalDeviceProduct2020):
            f.write(line + "\n")
