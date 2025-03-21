# DeviceUse

| zib                                        | xtehr                     | type_zib   | type_xtehr      | card._zib   | card._xtehr   |
|:-------------------------------------------|:--------------------------|:-----------|:----------------|:------------|:--------------|
| MedicalDevice                              | EHDSDeviceUse             |            |                 |             | 0..*          |
| MedicalDevice.AnatomicalLocation           | EHDSDeviceUse.bodySite    |            | CodeableConcept | 0..1        | 0..1          |
|                                            | EHDSDeviceUse.device      |            | Reference       |             | 1..1          |
| MedicalDevice.EindDatum                    | EHDSDeviceUse.endDate     | TS         | dateTime        | 0..1        | 0..1          |
|                                            | EHDSDeviceUse.identifier  |            | Identifier      |             | 0..*          |
| MedicalDevice.StartDate                    | EHDSDeviceUse.implantDate | TS         | dateTime        | 0..1        | 0..1          |
| MedicalDevice.Comment                      | EHDSDeviceUse.note        | ST         | Narrative       | 0..1        | 0..*          |
|                                            | EHDSDeviceUse.recorded    |            | dateTime        |             | 0..1          |
|                                            | EHDSDeviceUse.source      |            | Reference       |             | 0..1          |
|                                            | EHDSDeviceUse.status      |            | CodeableConcept |             | 0..1          |
|                                            | EHDSDeviceUse.subject     |            | Reference       |             | 1..1          |
| MedicalDevice.HealthProfessional           |                           |            |                 | 0..1        |               |
| MedicalDevice.Indication::Problem          |                           |            |                 | 0..*        |               |
| MedicalDevice.Location::HealthcareProvider |                           |            |                 | 0..1        |               |
| MedicalDevice.Product                      |                           |            |                 | 1           |               |
| MedicalDevice.Product.ProductID            |                           | CD         |                 | 0..1        |               |
| MedicalDevice.Product.ProductType          |                           | CD         |                 | 0..1        |               |
| MedicalDevice.ProductDescription           |                           | ST         |                 | 0..1        |               |



## EHDSDeviceUse

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDeviceUse |
| zib | MedicalDevice |
| alias_zib | NL: MedischHulpmiddel |
| binding_xtehr |  |
| card._xtehr | 0..* |
| card._zib |  |
| definition_xtehr | C.25 - EHDS refined base model for Device Use |
| definition_zib | Root concept of the MedicalDevice information model. This root concept contains all data elements of the MedicalDevice information model. |
| definitioncode_zib | SNOMED CT: 49062001 Device |
| id_xtehr | EHDSDeviceUse |
| id_zib | NL-CM:10.1.1 |
| name_zib | MedicalDevice |
| path_xtehr | EHDSDeviceUse |
| path_zib | MedicalDevice |
| short_xtehr | Device use model |
| stereotype_zib | rootconcept |
| type_xtehr |  |
| type_zib |  |

### Comments



## EHDSDeviceUse.bodySite

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDeviceUse.bodySite |
| zib | MedicalDevice.AnatomicalLocation |
| alias_zib | NL: AnatomischeLocatie |
| binding_xtehr |  |
| card._xtehr | 0..1 |
| card._zib | 0..1 |
| definition_xtehr | Anatomical location of the device. May include laterality. |
| definition_zib | Patient’s anatomical location of the medical device used. |
| definitioncode_zib | SNOMED CT: 363698007 Finding site |
| id_xtehr | EHDSDeviceUse.bodySite |
| id_zib | NL-CM:10.1.15 |
| name_zib | AnatomicalLocation |
| path_xtehr | EHDSDeviceUse.bodySite |
| path_zib | MedicalDevice.AnatomicalLocation |
| short_xtehr | C.25.7 - Body site |
| stereotype_zib | data,reference |
| type_xtehr | CodeableConcept |
| type_zib |  |

### Comments



## EHDSDeviceUse.device

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDeviceUse.device |
| zib |  |
| alias_zib |  |
| binding_xtehr |  |
| card._xtehr | 1..1 |
| card._zib |  |
| definition_xtehr | The details of the device used. |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSDeviceUse.device |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSDeviceUse.device |
| path_zib |  |
| short_xtehr | C.25.5 - Device |
| stereotype_zib |  |
| type_xtehr | Reference |
| type_zib |  |

### Comments



## EHDSDeviceUse.endDate

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDeviceUse.endDate |
| zib | MedicalDevice.EindDatum |
| alias_zib | EndDate |
| binding_xtehr |  |
| card._xtehr | 0..1 |
| card._zib | 0..1 |
| definition_xtehr | Date when the device was explanted from the patient or the external device was no longer in use; likewise when the device is planned to be explanted. |
| definition_zib | The end date of the last use or explant of the medical device. A ‘vague’ date, such as only the year, is permitted. |
| definitioncode_zib |  |
| id_xtehr | EHDSDeviceUse.endDate |
| id_zib | NL-CM:10.1.14 |
| name_zib | EindDatum |
| path_xtehr | EHDSDeviceUse.endDate |
| path_zib | MedicalDevice.EindDatum |
| short_xtehr | C.25.4 - End date |
| stereotype_zib | data |
| type_xtehr | dateTime |
| type_zib | TS |

### Comments



## EHDSDeviceUse.identifier

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDeviceUse.identifier |
| zib |  |
| alias_zib |  |
| binding_xtehr |  |
| card._xtehr | 0..* |
| card._zib |  |
| definition_xtehr | An identifier for this statement. |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSDeviceUse.identifier |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSDeviceUse.identifier |
| path_zib |  |
| short_xtehr | C.25.1 - Identifier |
| stereotype_zib |  |
| type_xtehr | Identifier |
| type_zib |  |

### Comments



## EHDSDeviceUse.implantDate

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDeviceUse.implantDate |
| zib | MedicalDevice.StartDate |
| alias_zib | NL: BeginDatum |
| binding_xtehr |  |
| card._xtehr | 0..1 |
| card._zib | 0..1 |
| definition_xtehr | Date when procedure was performed. |
| definition_zib | The start date of the first use or implant of the medical device. A ‘vague’ date, such as only the year, is permitted. |
| definitioncode_zib |  |
| id_xtehr | EHDSDeviceUse.implantDate |
| id_zib | NL-CM:10.1.11 |
| name_zib | StartDate |
| path_xtehr | EHDSDeviceUse.implantDate |
| path_zib | MedicalDevice.StartDate |
| short_xtehr | C.25.3 - Implant date |
| stereotype_zib | data |
| type_xtehr | dateTime |
| type_zib | TS |

### Comments



## EHDSDeviceUse.note

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDeviceUse.note |
| zib | MedicalDevice.Comment |
| alias_zib | NL: Toelichting |
| binding_xtehr |  |
| card._xtehr | 0..* |
| card._zib | 0..1 |
| definition_xtehr | Details about the device statement that were not represented at all or sufficiently in one of the attributes provided in a class. These may include for example a comment, an instruction, or a note associated with the statement. |
| definition_zib | Comment about use or information on the medical device used. |
| definitioncode_zib | LOINC: 48767-8 Annotation comment [Interpretation] Narrative |
| id_xtehr | EHDSDeviceUse.note |
| id_zib | NL-CM:10.1.10 |
| name_zib | Comment |
| path_xtehr | EHDSDeviceUse.note |
| path_zib | MedicalDevice.Comment |
| short_xtehr | C.25.8 - Note |
| stereotype_zib | data |
| type_xtehr | Narrative |
| type_zib | ST |

### Comments



## EHDSDeviceUse.recorded

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDeviceUse.recorded |
| zib |  |
| alias_zib |  |
| binding_xtehr |  |
| card._xtehr | 0..1 |
| card._zib |  |
| definition_xtehr | Date and time at which the statement was made/recorded. |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSDeviceUse.recorded |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSDeviceUse.recorded |
| path_zib |  |
| short_xtehr | C.25.9 - Recorded |
| stereotype_zib |  |
| type_xtehr | dateTime |
| type_zib |  |

### Comments



## EHDSDeviceUse.source

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDeviceUse.source |
| zib |  |
| alias_zib |  |
| binding_xtehr |  |
| card._xtehr | 0..1 |
| card._zib |  |
| definition_xtehr | Who reported the device was being used by the patient. |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSDeviceUse.source |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSDeviceUse.source |
| path_zib |  |
| short_xtehr | C.25.10 - Source |
| stereotype_zib |  |
| type_xtehr | Reference |
| type_zib |  |

### Comments



## EHDSDeviceUse.status

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDeviceUse.status |
| zib |  |
| alias_zib |  |
| binding_xtehr | {'strength': 'preferred', 'description': 'HL7 device-statement-status'} |
| card._xtehr | 0..1 |
| card._zib |  |
| definition_xtehr | Current status of the Device Usage. |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSDeviceUse.status |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSDeviceUse.status |
| path_zib |  |
| short_xtehr | C.25.2 - Status |
| stereotype_zib |  |
| type_xtehr | CodeableConcept |
| type_zib |  |

### Comments



## EHDSDeviceUse.subject

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDeviceUse.subject |
| zib |  |
| alias_zib |  |
| binding_xtehr |  |
| card._xtehr | 1..1 |
| card._zib |  |
| definition_xtehr | The patient using the device. |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSDeviceUse.subject |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSDeviceUse.subject |
| path_zib |  |
| short_xtehr | C.25.6 - Subject |
| stereotype_zib |  |
| type_xtehr | Reference |
| type_zib |  |

### Comments



## zib: MedicalDevice.HealthProfessional

### Table

| attribute | value |
|---|---|
| xtehr |  |
| zib | MedicalDevice.HealthProfessional |
| alias_zib | NL: Zorgverlener |
| binding_xtehr |  |
| card._xtehr |  |
| card._zib | 0..1 |
| definition_xtehr |  |
| definition_zib | The healthcare provider involved in the indication for use of the medical device implant. |
| definitioncode_zib |  |
| id_xtehr |  |
| id_zib | NL-CM:10.1.9 |
| name_zib | HealthProfessional |
| path_xtehr |  |
| path_zib | MedicalDevice.HealthProfessional |
| short_xtehr |  |
| stereotype_zib | context,reference |
| type_xtehr |  |
| type_zib |  |

### Comments



## zib: MedicalDevice.Indication::Problem

### Table

| attribute | value |
|---|---|
| xtehr |  |
| zib | MedicalDevice.Indication::Problem |
| alias_zib | NL: Indicatie::Probleem |
| binding_xtehr |  |
| card._xtehr |  |
| card._zib | 0..* |
| definition_xtehr |  |
| definition_zib | The medical reason for use of the medical device. |
| definitioncode_zib |  |
| id_xtehr |  |
| id_zib | NL-CM:10.1.7 |
| name_zib | Indication::Problem |
| path_xtehr |  |
| path_zib | MedicalDevice.Indication::Problem |
| short_xtehr |  |
| stereotype_zib | context,reference |
| type_xtehr |  |
| type_zib |  |

### Comments



## zib: MedicalDevice.Location::HealthcareProvider

### Table

| attribute | value |
|---|---|
| xtehr |  |
| zib | MedicalDevice.Location::HealthcareProvider |
| alias_zib | NL: Locatie::Zorgaanbieder |
| binding_xtehr |  |
| card._xtehr |  |
| card._zib | 0..1 |
| definition_xtehr |  |
| definition_zib | The healthcare provider at which use of the medical device was initiated or where the aid was implanted. |
| definitioncode_zib |  |
| id_xtehr |  |
| id_zib | NL-CM:10.1.8 |
| name_zib | Location::HealthcareProvider |
| path_xtehr |  |
| path_zib | MedicalDevice.Location::HealthcareProvider |
| short_xtehr |  |
| stereotype_zib | context,reference |
| type_xtehr |  |
| type_zib |  |

### Comments



## zib: MedicalDevice.Product

### Table

| attribute | value |
|---|---|
| xtehr |  |
| zib | MedicalDevice.Product |
| alias_zib | NL: Product |
| binding_xtehr |  |
| card._xtehr |  |
| card._zib | 1 |
| definition_xtehr |  |
| definition_zib | The medical device (internally or externally). |
| definitioncode_zib | SNOMED CT: 405815000 Procedure device |
| id_xtehr |  |
| id_zib | NL-CM:10.1.2 |
| name_zib | Product |
| path_xtehr |  |
| path_zib | MedicalDevice.Product |
| short_xtehr |  |
| stereotype_zib | container |
| type_xtehr |  |
| type_zib |  |

### Comments



## zib: MedicalDevice.Product.ProductID

### Table

| attribute | value |
|---|---|
| xtehr |  |
| zib | MedicalDevice.Product.ProductID |
| alias_zib | NL: ProductID |
| binding_xtehr |  |
| card._xtehr |  |
| card._zib | 0..1 |
| definition_xtehr |  |
| definition_zib | Unique identification of the product, such as the serial number. 
Frequently used coding systems are HIBC and GTIN.
If the law requires this to be registered on the basis of a UDI (Unique Device Identifier), the unique identification must consist of a UDI-DI (Device Identifier) and a UDI-PI (Production Identifier(s)). See http://www.gs1.org/healthcare/udi for more information. 

The UDI-DI must be recorded in reference to GS1 GTIN (01) encryptions, with which for example a firm is linked to the product type. The UDI-PI must consist of the following: application identifier (AI); expiration date (17) and serial number (21) and/or batch or lot number (10). |
| definitioncode_zib |  |
| id_xtehr |  |
| id_zib | NL-CM:10.1.4 |
| name_zib | ProductID |
| path_xtehr |  |
| path_zib | MedicalDevice.Product.ProductID |
| short_xtehr |  |
| stereotype_zib | data |
| type_xtehr |  |
| type_zib | CD |

### Comments



## zib: MedicalDevice.Product.ProductType

### Table

| attribute | value |
|---|---|
| xtehr |  |
| zib | MedicalDevice.Product.ProductType |
| alias_zib | NL: ProductType |
| binding_xtehr |  |
| card._xtehr |  |
| card._zib | 0..1 |
| definition_xtehr |  |
| definition_zib | The code of the type of product. |
| definitioncode_zib |  |
| id_xtehr |  |
| id_zib | NL-CM:10.1.3 |
| name_zib | ProductType |
| path_xtehr |  |
| path_zib | MedicalDevice.Product.ProductType |
| short_xtehr |  |
| stereotype_zib | data |
| type_xtehr |  |
| type_zib | CD |

### Comments



## zib: MedicalDevice.ProductDescription

### Table

| attribute | value |
|---|---|
| xtehr |  |
| zib | MedicalDevice.ProductDescription |
| alias_zib | NL: ProductOmschrijving |
| binding_xtehr |  |
| card._xtehr |  |
| card._zib | 0..1 |
| definition_xtehr |  |
| definition_zib | Textual description of the product. |
| definitioncode_zib |  |
| id_xtehr |  |
| id_zib | NL-CM:10.1.13 |
| name_zib | ProductDescription |
| path_xtehr |  |
| path_zib | MedicalDevice.ProductDescription |
| short_xtehr |  |
| stereotype_zib | data |
| type_xtehr |  |
| type_zib | ST |

### Comments

