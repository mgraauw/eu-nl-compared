# Device

| zib                                        | xtehr                      | type_zib   | type_xtehr      | card._zib   | card._xtehr   |
|:-------------------------------------------|:---------------------------|:-----------|:----------------|:------------|:--------------|
| MedicalDevice                              | EHDSDevice, EHDSDeviceUse                 |            |                 |             | 0..*          |
|                                            | EHDSDevice.expiryDate      |            | dateTime        |             | 0..1          |
| MedicalDevice.Product.ProductID            | EHDSDevice.identifier      | CD         | Identifier      | 0..1        | 1..*          |
|                                            | EHDSDevice.lotNumber       |            | string          |             | 0..1          |
|                                            | EHDSDevice.manufactureDate |            | dateTime        |             | 0..1          |
|                                            | EHDSDevice.manufacturer    |            | string          |             | 0..1          |
| MedicalDevice.Product.ProductType          | EHDSDevice.modelNumber     | CD         | string          | 0..1        | 0..1          |
|                                            | EHDSDevice.name            |            | string          |             | 0..*          |
|                                            | EHDSDevice.note            |            | Narrative       |             | 0..*          |
|                                            | EHDSDevice.serialNumber    |            | string          |             | 0..1          |
|                                            | EHDSDevice.type            |            | CodeableConcept |             | 0..*          |
|                                            | EHDSDevice.version         |            | string          |             | 0..1          |
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
| MedicalDevice.HealthProfessional           |                            |            |                 | 0..1        |               |
| MedicalDevice.Indication::Problem          |                            |            |                 | 0..*        |               |
| MedicalDevice.Location::HealthcareProvider |                            |            |                 | 0..1        |               |
| MedicalDevice.Product                      |                            |            |                 | 1           |               |
| MedicalDevice.ProductDescription           |                            | ST         |                 | 0..1        |               |


## EHDSDevice

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDevice |
| zib | MedicalDevice |
| alias_zib | NL: MedischHulpmiddel |
| binding_xtehr |  |
| card._xtehr | 0..* |
| card._zib |  |
| definition_xtehr | C.12 - EHDS refined base model for Device information |
| definition_zib | Root concept of the MedicalDevice information model. This root concept contains all data elements of the MedicalDevice information model. |
| definitioncode_zib | SNOMED CT: 49062001 Device |
| id_xtehr | EHDSDevice |
| id_zib | NL-CM:10.1.1 |
| name_zib | MedicalDevice |
| path_xtehr | EHDSDevice |
| path_zib | MedicalDevice |
| short_xtehr | Device model |
| stereotype_zib | rootconcept |
| type_xtehr |  |
| type_zib |  |

### Comments

* de zib kent 1 MedicalDevice, in XtEHR is dit gesplitst in:
  * Device
  * DeviceUse
* Definitie:
  * de zib definieert dit als: "Medical devices are any internally implanted and external devices and/or aids used by the patient (in the past) to reduce the effects of functional limitations in organ systems or to facilitate the treatment of a disease."
  * de XtEHR zegt: "Describes the patient's implanted and external medical devices and equipment upon which their health status depends. Includes devices such as cardiac pacemakers, implantable fibrillator, prosthesis, ferromagnetic bone implants, etc. of which the HP needs to be aware."
* de zib includeert dus 'aids' (hulpmiddelen) zoals krukken of rolstoelen die niet in de XtEHR definitie vallen
* de HDR maakt onderscheid tussen Devices voor en tijdens opname ziekenhuis

## EHDSDevice.expiryDate

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDevice.expiryDate |
| zib |  |
| alias_zib |  |
| binding_xtehr |  |
| card._xtehr | 0..1 |
| card._zib |  |
| definition_xtehr | The date and time beyond which this device is no longer valid or should not be used (if applicable). |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSDevice.expiryDate |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSDevice.expiryDate |
| path_zib |  |
| short_xtehr | C.12.4 - Expiry date |
| stereotype_zib |  |
| type_xtehr | dateTime |
| type_zib |  |

### Comments

* de zib kent geen expiryDate

## EHDSDevice.identifier

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDevice.identifier |
| zib | MedicalDevice.Product.ProductID |
| alias_zib | NL: ProductID |
| binding_xtehr |  |
| card._xtehr | 1..* |
| card._zib | 0..1 |
| definition_xtehr | An identifier of the device which is unique within in a defined scope. Multiple identifiers can be used. |
| definition_zib | Unique identification of the product, such as the serial number. <br/>Frequently used coding systems are HIBC and GTIN.<br/>If the law requires this to be registered on the basis of a UDI (Unique Device Identifier), the unique identification must consist of a UDI-DI (Device Identifier) and a UDI-PI (Production Identifier(s)). See http://www.gs1.org/healthcare/udi for more information. <br/>The UDI-DI must be recorded in reference to GS1 GTIN (01) encryptions, with which for example a firm is linked to the product type. The UDI-PI must consist of the following: application identifier (AI); expiration date (17) and serial number (21) and/or batch or lot number (10). |
| definitioncode_zib |  |
| id_xtehr | EHDSDevice.identifier |
| id_zib | NL-CM:10.1.4 |
| name_zib | ProductID |
| path_xtehr | EHDSDevice.identifier |
| path_zib | MedicalDevice.Product.ProductID |
| short_xtehr | C.12.1 - Identifier |
| stereotype_zib | data |
| type_xtehr | Identifier |
| type_zib | CD |

### Comments

* de xtehr definieert (nog) geen eisen aan de identifier, het lijkt er dus op dat de Nederlandse identifiers wel voldoen
* eHN ePS noemt 'such as' UDI
* de zib kent maar 1 identifier, de xtehr staat er meerdere toe

## EHDSDevice.lotNumber

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDevice.lotNumber |
| zib |  |
| alias_zib |  |
| binding_xtehr |  |
| card._xtehr | 0..1 |
| card._zib |  |
| definition_xtehr | Lot number of manufacture |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSDevice.lotNumber |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSDevice.lotNumber |
| path_zib |  |
| short_xtehr | C.12.5 - Lot number |
| stereotype_zib |  |
| type_xtehr | string |
| type_zib |  |

### Comments

* de zib kent geen lotNumber

## EHDSDevice.manufactureDate

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDevice.manufactureDate |
| zib |  |
| alias_zib |  |
| binding_xtehr |  |
| card._xtehr | 0..1 |
| card._zib |  |
| definition_xtehr | The date and time when the device was manufactured |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSDevice.manufactureDate |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSDevice.manufactureDate |
| path_zib |  |
| short_xtehr | C.12.3 - Manufacture date |
| stereotype_zib |  |
| type_xtehr | dateTime |
| type_zib |  |

### Comments

* de zib kent geen manufactureDate

## EHDSDevice.manufacturer

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDevice.manufacturer |
| zib |  |
| alias_zib |  |
| binding_xtehr |  |
| card._xtehr | 0..1 |
| card._zib |  |
| definition_xtehr | Name of device manufacturer |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSDevice.manufacturer |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSDevice.manufacturer |
| path_zib |  |
| short_xtehr | C.12.2 - Manufacturer |
| stereotype_zib |  |
| type_xtehr | string |
| type_zib |  |

### Comments

* de zib kent geen manufacturer

## EHDSDevice.modelNumber

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDevice.modelNumber |
| zib | MedicalDevice.Product.ProductType |
| alias_zib | NL: ProductType |
| binding_xtehr |  |
| card._xtehr | 0..1 |
| card._zib | 0..1 |
| definition_xtehr | The manufacturer's model number for the device |
| definition_zib | The code of the type of product. |
| definitioncode_zib |  |
| id_xtehr | EHDSDevice.modelNumber |
| id_zib | NL-CM:10.1.3 |
| name_zib | ProductType |
| path_xtehr | EHDSDevice.modelNumber |
| path_zib | MedicalDevice.Product.ProductType |
| short_xtehr | C.12.8 - Model number |
| stereotype_zib | data |
| type_xtehr | string |
| type_zib | CD |

### Comments

* de zib kent geen modelNumber

## EHDSDevice.name

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDevice.name |
| zib |  |
| alias_zib |  |
| binding_xtehr |  |
| card._xtehr | 0..* |
| card._zib |  |
| definition_xtehr | The name and name type of the device as known to the manufacturer and/or patient |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSDevice.name |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSDevice.name |
| path_zib |  |
| short_xtehr | C.12.7 - Name |
| stereotype_zib |  |
| type_xtehr | string |
| type_zib |  |

### Comments

* de zib kent geen name (wel een algemenere 'ProductDescription')

## EHDSDevice.note

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDevice.note |
| zib |  |
| alias_zib |  |
| binding_xtehr |  |
| card._xtehr | 0..* |
| card._zib |  |
| definition_xtehr | Device notes and comments |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSDevice.note |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSDevice.note |
| path_zib |  |
| short_xtehr | C.12.11 - Note |
| stereotype_zib |  |
| type_xtehr | Narrative |
| type_zib |  |

### Comments

* TODO

## EHDSDevice.serialNumber

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDevice.serialNumber |
| zib |  |
| alias_zib |  |
| binding_xtehr |  |
| card._xtehr | 0..1 |
| card._zib |  |
| definition_xtehr | Serial number assigned by the manufacturer |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSDevice.serialNumber |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSDevice.serialNumber |
| path_zib |  |
| short_xtehr | C.12.6 - Serial number |
| stereotype_zib |  |
| type_xtehr | string |
| type_zib |  |

### Comments

* de zib kent geen serialNumber

## EHDSDevice.type

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDevice.type |
| zib |  |
| alias_zib |  |
| binding_xtehr | {'strength': 'preferred', 'description': 'SNOMED CT, EMDN'} |
| card._xtehr | 0..* |
| card._zib |  |
| definition_xtehr | Device type |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSDevice.type |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSDevice.type |
| path_zib |  |
| short_xtehr | C.12.10 - Type |
| stereotype_zib |  |
| type_xtehr | CodeableConcept |
| type_zib |  |

### Comments

* de zib kent geen serialNumber

## EHDSDevice.version

### Table

| attribute | value |
|---|---|
| xtehr | EHDSDevice.version |
| zib |  |
| alias_zib |  |
| binding_xtehr |  |
| card._xtehr | 0..1 |
| card._zib |  |
| definition_xtehr | The actual design of the device or software version running on the device |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSDevice.version |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSDevice.version |
| path_zib |  |
| short_xtehr | C.12.9 - Version |
| stereotype_zib |  |
| type_xtehr | string |
| type_zib |  |

### Comments

* de zib kent geen version

## zib: MedicalDevice.AnatomicalLocation

### Table

| attribute | value |
|---|---|
| xtehr |  |
| zib | MedicalDevice.AnatomicalLocation |
| alias_zib | NL: AnatomischeLocatie |
| binding_xtehr |  |
| card._xtehr |  |
| card._zib | 0..1 |
| definition_xtehr |  |
| definition_zib | Patient’s anatomical location of the medical device used. |
| definitioncode_zib | SNOMED CT: 363698007 Finding site |
| id_xtehr |  |
| id_zib | NL-CM:10.1.15 |
| name_zib | AnatomicalLocation |
| path_xtehr |  |
| path_zib | MedicalDevice.AnatomicalLocation |
| short_xtehr |  |
| stereotype_zib | data,reference |
| type_xtehr |  |
| type_zib |  |

### Comments

* TODO: dit is DeviceUse.BodySite

## zib: MedicalDevice.Comment

### Table

| attribute | value |
|---|---|
| xtehr |  |
| zib | MedicalDevice.Comment |
| alias_zib | NL: Toelichting |
| binding_xtehr |  |
| card._xtehr |  |
| card._zib | 0..1 |
| definition_xtehr |  |
| definition_zib | Comment about use or information on the medical device used. |
| definitioncode_zib | LOINC: 48767-8 Annotation comment [Interpretation] Narrative |
| id_xtehr |  |
| id_zib | NL-CM:10.1.10 |
| name_zib | Comment |
| path_xtehr |  |
| path_zib | MedicalDevice.Comment |
| short_xtehr |  |
| stereotype_zib | data |
| type_xtehr |  |
| type_zib | ST |

### Comments

* TODO: dit is min of meer DeviceUse.note

## zib: MedicalDevice.EindDatum

### Table

| attribute | value |
|---|---|
| xtehr |  |
| zib | MedicalDevice.EindDatum |
| alias_zib | EndDate |
| binding_xtehr |  |
| card._xtehr |  |
| card._zib | 0..1 |
| definition_xtehr |  |
| definition_zib | The end date of the last use or explant of the medical device. A ‘vague’ date, such as only the year, is permitted. |
| definitioncode_zib |  |
| id_xtehr |  |
| id_zib | NL-CM:10.1.14 |
| name_zib | EindDatum |
| path_xtehr |  |
| path_zib | MedicalDevice.EindDatum |
| short_xtehr |  |
| stereotype_zib | data |
| type_xtehr |  |
| type_zib | TS |

### Comments

* TDO: zit in DeviceUse

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

* de xtehr kent geen MedicalDevice.HealthProfessional maar een DeviceUse.source: dat is de bron van de informatie, niet de verantwoordelijke

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

* zie opmerking bij HealthProfessional

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

* de xtehr kent geen MedicalDevice.Indication::Problem

===============tot hier =================

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

* de zib kent ProductDescription wat een beschrijving van het product is
  * DeviceUse kent een 'note' die bedoeld is voor informatie die niet in de andere velden zit
