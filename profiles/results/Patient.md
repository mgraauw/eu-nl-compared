# Patient profiles
## nl-core-patient (2017) <-> Patient-uv-ips
x nl-core-patient (zib2017) does not seem to fit in Patient-eu-eps (eps)
* x Patient.name: required in Patient-eu-eps but optional in nl-core-patient.
* x Patient.birthDate: required in Patient-eu-eps but optional in nl-core-patient.
* ~ Patient.contact.relationship: The zib binds two ValueSets, one of which partially overlaps semantically with the required ValueSet in the Patient-eu-eps profile.

x Patient-eu-eps (eps) does not seem to fit in nl-core-patient (zib2017)
* x Patient.generalPractitioner: restricted to 1 in nl-core-patient but unrestricted in Patient-eu-eps.


## zib-Patient (2020) <-> Patient-uv-ips
x zib-Patient (zib2020) does not seem to fit in Patient-eu-eps (eps)
* x Patient.name: required in Patient-eu-eps but optional in zib-Patient.
* x Patient.birthDate: required in Patient-eu-eps but optional in zib-Patient.

x Patient-eu-eps (eps) does not seem to fit in zib-Patient (zib2020)
* x Patient.maritalStatus: required Valueset in zib-Patient is more restrictive than Patient-eu-eps.
* x Patient.communication.language: required Valueset in zib-Patient is more restrictive than Patient-eu-eps.
