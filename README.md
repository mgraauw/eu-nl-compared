# Comparison between XtEHR and zibs

## Mappen

* zibs2020: bevat de mappen
  * downloads: de zibs zelf, dit zijn de Excels van zibs.nl gedownload
  * mappable
* zibs2024: bevat de mappen
  * downloads: de zibs zelf, deze zijn met Excel (Data->from web) gedownload omdat de Excels nog niet op zibs.nl stonden
  * mappable
* maps met mappingen tussen zibs en logical models, deze worden met de hand gemaakt, voorlopig een mapping voor zowel zibs2020 als zibs2024
* maps/xtehr2zibs: dit zijn de aangemaakte mappings in Excel en markdown
* maps/xtehr2zibs2024: dito

De 'mappable' Excels zijn allemaal gestandaardiseerd naar een gemeenschappelijk format met voor de zibs kolommen:

* name
* path
* type
* card.
* id
* definition
* definitioncode

en voor de XtEHR logical models:

* id
* path
* short
* definition
* type
* card.
* binding

Dit gemeenschappelijk formaat maakt het eenvoudiger de volgende mapping stappen te doen. Belangrijkste is **path** dit is een puntgescheiden path (naam.naam2.naam3) waarmee de mapping tussen zibs en logical models gemaakt wordt.

In **maps** staat de met de hand gemaakte path-op-path mapping, dit is alleen een tussenstap in de conversie.

In **xtehr2zibs** en **xtehr2zibs2024** staan de gegenereerde files:

* Excels voor wie die graag wil zien
* dito CSV, wordt nu niet gebruikt maar vanuit Github worden deze netjes gerenderd als je naar die map gaat
* markdown:
  * {file}.md is de gegenereerde mardown
  * {file}-comments.md is na genereren identiek aan de vorige maar dat is degene die met de hand aangepast kan worden om onder comments kopjes de bevindingen per item te noteren.

## Sources

| Comparison Logical model 2024 | Comparison Logical model 2020 | Comparison FHIR profile | XtEHR | zib2020 | zib2024 (prereleease) |
|---|---|---|---|---|---|
|Alert|Alert | [AlertFlag](https://build.fhir.org/ig/Xt-EHR/xt-ehr-common/StructureDefinition-EHDSAlertFlag.html)| | [Alert-v4.1](https://zibs.nl/wiki/Alert-v4.1(2020EN)) | |
|AllergyIntolerance|AllergyIntolerance |[Allergy Intolerance](https://build.fhir.org/ig/Xt-EHR/xt-ehr-common/StructureDefinition-EHDSAllergyIntolerance.html)| | [AllergyIntolerance-v3.3](https://zibs.nl/wiki/AllergyIntolerance-v3.3(2020EN))| |
|[Condition](./maps/xtehr2zibs/Condition-comments.md)| |[Condition](https://build.fhir.org/ig/Xt-EHR/xt-ehr-common/StructureDefinition-EHDSCondition.html)| | [Problem-v4.4](https://zibs.nl/wiki/Problem-v4.4(2020EN))| |
|[Device](./maps/xtehr2zibs2024/Device_And_DeviceUse-comments.md)| [Device](./maps/xtehr2zibs2024/Device_And_DeviceUse-comments.md) |[Device](https://build.fhir.org/ig/Xt-EHR/xt-ehr-common/StructureDefinition-EHDSDevice.html)<br/>[DeviceUse](https://build.fhir.org/ig/Xt-EHR/xt-ehr-common/StructureDefinition-EHDSDeviceUse.html)| |[MedicalDevice-v3.3.1](https://zibs.nl/wiki/MedicalDevice-v3.3.1(2020EN))|[MedicalDevice-v5.0](https://zibs.nl/wiki/MedicalDevice-v5.0(2024EN))
|Medication overview | | |
|[Patient](./maps/xtehr2zibs2024/Patient-comments.md)| [Patient](./maps/xtehr2zibs2024/Patient-comments.md) | [Patient](https://build.fhir.org/ig/Xt-EHR/xt-ehr-common/StructureDefinition-EHDSPatient.html)| |[Patient-v3.2](https://zibs.nl/wiki/Patient-v3.2(2020EN)) | [Patient-v4.3](https://zibs.nl/wiki/Patient-v4.3(2024EN))
|[Procedure](./maps/xtehr2zibs2024/Procedure-comments.md)| [Procedure](./maps/xtehr2zibs2024/Procedure-comments.md) |[Procedure](https://build.fhir.org/ig/Xt-EHR/xt-ehr-common/StructureDefinition-EHDSProcedure.html)| | [Procedure-v5.2](https://zibs.nl/wiki/Procedure-v5.2(2020EN)) | [Procedure-v6.0](https://zibs.nl/wiki/Procedure-v6.0(2024EN)) |
