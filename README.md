# Comparison between XtEHR and zibs

## Sources

| Comparison Logical model| Comparison FHIR profile | XtEHR | zib2017 | zib2020 | zib2024 (prereleease) |
|---|---|---|---|---|---|
|Alert| | [AlertFlag](https://build.fhir.org/ig/Xt-EHR/xt-ehr-common/StructureDefinition-EHDSAlertFlag.html)| | [Alert-v4.1](https://zibs.nl/wiki/Alert-v4.1(2020EN)) | |
|AllergyIntolerance| |[Allergy Intolerance](https://build.fhir.org/ig/Xt-EHR/xt-ehr-common/StructureDefinition-EHDSAllergyIntolerance.html)| | [AllergyIntolerance-v3.3](https://zibs.nl/wiki/AllergyIntolerance-v3.3(2020EN))| |
|[Condition](./maps/xtehr2zibs/Condition-comments.md)| |[Condition](https://build.fhir.org/ig/Xt-EHR/xt-ehr-common/StructureDefinition-EHDSCondition.html)| | [Problem-v4.4](https://zibs.nl/wiki/Problem-v4.4(2020EN))| |
|[Device](./maps/xtehr2zibs/Device_And_DeviceUse-comments.md)| |[Device](https://build.fhir.org/ig/Xt-EHR/xt-ehr-common/StructureDefinition-EHDSDevice.html)<br/>[DeviceUse](https://build.fhir.org/ig/Xt-EHR/xt-ehr-common/StructureDefinition-EHDSDeviceUse.html)| |[MedicalDevice-v3.3.1](https://zibs.nl/wiki/MedicalDevice-v3.3.1(2020EN))
|Medication overview | | |
|[Patient](./maps/xtehr2zibs/Patient-comments.md)| | [Patient](https://build.fhir.org/ig/Xt-EHR/xt-ehr-common/StructureDefinition-EHDSPatient.html)| |[Patient-v3.2](https://zibs.nl/wiki/Patient-v3.2(2020EN)) |
|[Procedure](./maps/xtehr2zibs/Procedure-comments.md)| |[Procedure](https://build.fhir.org/ig/Xt-EHR/xt-ehr-common/StructureDefinition-EHDSProcedure.html)| | [Procedure-v5.2](https://zibs.nl/wiki/Procedure-v5.2(2020EN)) |
