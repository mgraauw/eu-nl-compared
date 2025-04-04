# DeviceUseStatement/Device profiles
## zib 2017 <-> EPS
### zib-MedicalDevice (2017) <-> DeviceUseStatement-eu-eps
x zib-MedicalDevice (zib2017) does not seem to fit in DeviceUseStatement-eu-eps (eps)
* x DeviceUseStatement.timing[x]: required in DeviceUseStatement-eu-eps but optional in zib-MedicalDevice.

x zib-MedicalDeviceProduct (zib2017) does not seem to fit in Device-eu-eps (eps)
* x Device.patient: required in Device-eu-eps but optional in zib-MedicalDeviceProduct.

x DeviceUseStatement-eu-eps (eps) does not seem to fit in zib-MedicalDevice (zib2017)
* ~ DeviceUseStatement.bodySite: The zib requires SNOMED codes for all body sites defined in branch <442083009, but the EPS ValueSet is only preferred, so in theory overlapping codes from other systems might be used.

+ Device-eu-eps (eps) does seem to fit in zib-MedicalDeviceProduct (zib2017).


### zib-MedicalDevice (2020) <-> DeviceUseStatement-eu-eps
x zib-MedicalDevice (zib2020) does not seem to fit in DeviceUseStatement-eu-eps (eps)
* x DeviceUseStatement.timing[x]: required in DeviceUseStatement-eu-eps but optional in zib-MedicalDevice.

x zib-MedicalDevice.Product (zib2020) does not seem to fit in Device-eu-eps (eps)
* x Device.patient: required in Device-eu-eps but optional in zib-MedicalDevice.Product.

x DeviceUseStatement-eu-eps (eps) does not seem to fit in zib-MedicalDevice (zib2020)
* x DeviceUseStatement.bodySite: required Valueset in zib-MedicalDevice is more restrictive than DeviceUseStatement-eu-eps.
* x DeviceUseStatement.note: restricted to 1 in zib-MedicalDevice but unrestricted in DeviceUseStatement-eu-eps.

x Device-eu-eps (eps) does not seem to fit in zib-MedicalDevice.Product (zib2020)
* x Device.identifier: restricted to 1 in zib-MedicalDevice.Product but unrestricted in Device-eu-eps.
* x Device.udiCarrier: restricted to 1 in zib-MedicalDevice.Product but unrestricted in Device-eu-eps.
* x Device.type: The IPS/EPS uses the combination of DeviceUseStatement and Device to explicitly state that there or no devices, by introducing codes for this purpose on Device.type. This usage is precluded by the zib, which restricts the ValueSet on Device.type.
* x Device.note: restricted to 1 in zib-MedicalDevice.Product but unrestricted in Device-eu-eps.
