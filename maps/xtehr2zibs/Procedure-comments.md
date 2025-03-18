# Procedure

| zib                                                       | xtehr                          | type_zib   | type_xtehr      | card._zib   | card._xtehr   |
|:----------------------------------------------------------|:-------------------------------|:-----------|:----------------|:------------|:--------------|
| Procedure                                                 | EHDSProcedure                  |            |                 |             | 0..*          |
| Procedure.ProcedureAnatomicalLocation::AnatomicalLocation | EHDSProcedure.anatomicLocation |            | CodeableConcept | 0..1        | 0..*          |
| Procedure.ProcedureType                                   | EHDSProcedure.code             | CD         | CodeableConcept | 1           | 0..1          |
|                                                           | EHDSProcedure.complication     |            | CodeableConcept |             | 0..*          |
| Procedure.ProcedureEndDate                                | EHDSProcedure.date[x]          | TS         | dateTime        | 0..1        | 0..1          |
| Procedure.ProcedureStartDate                              | EHDSProcedure.date[x]          | TS         | dateTime        | 0..1        | 0..1          |
|                                                           | EHDSProcedure.description      |            | string          |             | 0..1          |
|                                                           | EHDSProcedure.deviceUsed       |            | EHDSDevice      |             | 0..*          |
| Procedure.MedicalDevice                                   | EHDSProcedure.focalDevice      |            | Reference       | 0..*        | 0..*          |
|                                                           | EHDSProcedure.identifier       |            | Identifier      |             | 0..*          |
| Procedure.Location::HealthcareProvider                    | EHDSProcedure.location         |            | EHDSLocation    | 0..1        | 0..*          |
|                                                           | EHDSProcedure.note             |            | string          |             | 0..1          |
|                                                           | EHDSProcedure.outcome          |            | CodeableConcept |             | 0..1          |
| Procedure.Performer::HealthProfessional                   | EHDSProcedure.performer        |            | Reference       | 0..*        | 0..*          |
| Procedure.Indication::Problem                             | EHDSProcedure.reason           |            | Reference       | 0..*        | 0..*          |
|                                                           | EHDSProcedure.subject          |            | Reference       |             | 1..1          |
| Procedure.ProcedureMethod                                 |                                | CD         |                 | 0..*        |               |
| Procedure.Requester::HealthProfessional                   |                                |            |                 | 0..*        |               |



## EHDSProcedure

### Table

| attribute | value |
|---|---|
| xtehr | EHDSProcedure |
| zib | Procedure |
| name_zib | Procedure |
| path_zib | Procedure |
| alias_zib | NL: Verrichting |
| type_zib |  |
| card._zib |  |
| stereotype_zib | rootconcept |
| id_zib | NL-CM:14.1.1 |
| definition_zib | Root concept of the Procedure information model. This root concept contains all data elements of the Procedure information model. |
| definitioncode_zib | SNOMED CT: 71388002 Procedure |
| id_xtehr | EHDSProcedure |
| path_xtehr | EHDSProcedure |
| short_xtehr | Procedure model |
| definition_xtehr | C.16 - EHDS refined base model for An action that is or was performed on or for a patient |
| type_xtehr |  |
| card._xtehr | 0..* |
| binding_xtehr |  |

### Comments

* xtehr modelleert een aantal metagegevens (identifier etc.) expliciet, de zib niet
* xtehr Procedure geeft in tekstuele omschrijving aan alleen voor heden en verleden te zijn, de zib gaat ook over de toekomst.

## EHDSProcedure.anatomicLocation

### Table

| attribute | value |
|---|---|
| xtehr | EHDSProcedure.anatomicLocation |
| zib | Procedure.ProcedureAnatomicalLocation::AnatomicalLocation |
| name_zib | ProcedureAnatomicalLocation::AnatomicalLocation |
| path_zib | Procedure.ProcedureAnatomicalLocation::AnatomicalLocation |
| alias_zib | NL: VerrichtingAnatomischeLocatie::AnatomischeLocatie |
| type_zib |  |
| card._zib | 0..1 |
| stereotype_zib | data,reference |
| id_zib | NL-CM:14.1.13 |
| definition_zib | Anatomical location which is the focus of the procedure. |
| definitioncode_zib | SNOMED CT: 405813007 Procedure site - Direct |
| id_xtehr | EHDSProcedure.anatomicLocation |
| path_xtehr | EHDSProcedure.anatomicLocation |
| short_xtehr | C.16.6 - Anatomic location |
| definition_xtehr | Anatomic location and laterality where the procedure was performed. This is the target site. |
| type_xtehr | CodeableConcept |
| card._xtehr | 0..* |
| binding_xtehr | {'strength': 'preferred', 'description': 'SNOMED CT, ICD-O-3'} |

### Comments

* xtehr has more than one anatomicalLocation
* zib has separate laterality + location
* xtehr possibly allows 2 codes, maybe for laterality and location, or a combined (postcoordinated) code
* xtehr specs are unclear about the precise intent
  * I've asked on IPS Zulip channel

## EHDSProcedure.code

### Table

| attribute | value |
|---|---|
| xtehr | EHDSProcedure.code |
| zib | Procedure.ProcedureType |
| name_zib | ProcedureType |
| path_zib | Procedure.ProcedureType |
| alias_zib | NL: VerrichtingType |
| type_zib | CD |
| card._zib | 1 |
| stereotype_zib | data |
| id_zib | NL-CM:14.1.4 |
| definition_zib | The name of the procedure.<br />Choices are the DHD procedure thesaurus,  the procedures file (CBV), the Care activities file (NZa), the Dutch Mental Health and Addiction Care procedures list (GGZ) and the procedures list of the Dutch College of General Practitioners (NHG). |
| definitioncode_zib |  |
| id_xtehr | EHDSProcedure.code |
| path_xtehr | EHDSProcedure.code |
| short_xtehr | C.16.3 - Code |
| definition_xtehr | Code identifying the procedure |
| type_xtehr | CodeableConcept |
| card._xtehr | 0..1 |
| binding_xtehr | {'strength': 'preferred', 'description': 'SNOMED CT'} |

### Comments

* zib limits to a few Dutch sets (DHD, NHG etc.)
* xtehr prefers SNOMED
  * with DHD zib is xtehr-compliant (narrower)
  * with NHG not (leaving code out makes it xtehr-compliant but no longer zib-compliant)
  * others to be examined
* code is optional in xtehr and required in zib

## EHDSProcedure.complication

### Table

| attribute | value |
|---|---|
| xtehr | EHDSProcedure.complication |
| zib |  |
| name_zib |  |
| path_zib |  |
| alias_zib |  |
| type_zib |  |
| card._zib |  |
| stereotype_zib |  |
| id_zib |  |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSProcedure.complication |
| path_xtehr | EHDSProcedure.complication |
| short_xtehr | C.16.9 - Complication |
| definition_xtehr | Any complications that occurred during the procedure, or in the immediate post-performance period. These are generally tracked separately from the procedure description, which will typically describe the procedure itself rather than any 'post procedure' issues. |
| type_xtehr | CodeableConcept |
| card._xtehr | 0..* |
| binding_xtehr | {'strength': 'preferred', 'description': 'ICD-10*, SNOMED CT, Orphacode if rare disease is diagnosed'} |

### Comments

* complication ontbreekt in de zib

## EHDSProcedure.date[x]

### Table

| attribute | value |
|---|---|
| xtehr | EHDSProcedure.date[x] |
| zib | Procedure.ProcedureEndDate |
| name_zib | ProcedureEndDate |
| path_zib | Procedure.ProcedureEndDate |
| alias_zib | NL: VerrichtingEindDatum |
| type_zib | TS |
| card._zib | 0..1 |
| stereotype_zib | data |
| id_zib | NL-CM:14.1.3 |
| definition_zib | The end date (and if possible end time) of the procedure. A ‘vague’ date, such as only the year, is permitted. <br/>The element offers the option to indicate the end of the period of a series of related procedures. The end date element is only used for a procedures that takes some time and is then always applied. If the procedure still continues, the value is left empty. For instantaneous or very short lasting procedures the element is omitted. |
| definitioncode_zib |  |
| id_xtehr | EHDSProcedure.date[x] |
| path_xtehr | EHDSProcedure.date[x] |
| short_xtehr | C.16.4 - Date |
| definition_xtehr | Date and time of the procedure or interval of its performance |
| type_xtehr | dateTime |
| card._xtehr | 0..1 |
| binding_xtehr |  |

### Comments

* compliant

## EHDSProcedure.date[x]

### Table

| attribute | value |
|---|---|
| xtehr | EHDSProcedure.date[x] |
| zib | Procedure.ProcedureStartDate |
| name_zib | ProcedureStartDate |
| path_zib | Procedure.ProcedureStartDate |
| alias_zib | NL: VerrichtingStartDatum |
| type_zib | TS |
| card._zib | 0..1 |
| stereotype_zib | data |
| id_zib | NL-CM:14.1.2 |
| definition_zib | The (desired) start date (and if possible start time) of the procedure. A ‘vague’ date, such as only the year, is permitted. 
The element offers the option to indicate the start of the period of a series of related procedures. |
| definitioncode_zib |  |
| id_xtehr | EHDSProcedure.date[x] |
| path_xtehr | EHDSProcedure.date[x] |
| short_xtehr | C.16.4 - Date |
| definition_xtehr | Date and time of the procedure or interval of its performance |
| type_xtehr | dateTime |
| card._xtehr | 0..1 |
| binding_xtehr |  |

### Comments

* compliant

## EHDSProcedure.description

### Table

| attribute | value |
|---|---|
| xtehr | EHDSProcedure.description |
| zib |  |
| name_zib |  |
| path_zib |  |
| alias_zib |  |
| type_zib |  |
| card._zib |  |
| stereotype_zib |  |
| id_zib |  |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSProcedure.description |
| path_xtehr | EHDSProcedure.description |
| short_xtehr | C.16.2 - Description |
| definition_xtehr | Procedure specification in string form |
| type_xtehr | string |
| card._xtehr | 0..1 |
| binding_xtehr |  |

### Comments

* zib heeft geen 'description'
* description in de xtehr is een tekstuele omschrijving, geen toelichting (zie ook 'note' hieronder)

## EHDSProcedure.deviceUsed

### Table

| attribute | value |
|---|---|
| xtehr | EHDSProcedure.deviceUsed |
| zib |  |
| name_zib |  |
| path_zib |  |
| alias_zib |  |
| type_zib |  |
| card._zib |  |
| stereotype_zib |  |
| id_zib |  |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSProcedure.deviceUsed |
| path_xtehr | EHDSProcedure.deviceUsed |
| short_xtehr | C.16.10 - Device used |
| definition_xtehr | Device used to perform the procedure |
| type_xtehr | EHDSDevice |
| card._xtehr | 0..* |
| binding_xtehr |  |

### Comments

* zib heeft geen 'deviceUsed'

## EHDSProcedure.focalDevice

### Table

| attribute | value |
|---|---|
| xtehr | EHDSProcedure.focalDevice |
| zib | Procedure.MedicalDevice |
| name_zib | MedicalDevice |
| path_zib | Procedure.MedicalDevice |
| alias_zib | NL: MedischHulpmiddel |
| type_zib |  |
| card._zib | 0..* |
| stereotype_zib | data,reference |
| id_zib | NL-CM:14.1.7 |
| definition_zib | The product, the placing of which in or on the body is the purpose of the procedure, for example placing an implant. |
| definitioncode_zib | SNOMED CT: 405815000 Procedure device |
| id_xtehr | EHDSProcedure.focalDevice |
| path_xtehr | EHDSProcedure.focalDevice |
| short_xtehr | C.16.11 - Focal device |
| definition_xtehr | Device or devices that is/are implanted, removed, or otherwise manipulated (calibration, battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as a focal portion of the Procedure. |
| type_xtehr | Reference |
| card._xtehr | 0..* |
| binding_xtehr |  |

### Comments

* definitie in Procedure is hetzelfde
* maar MedischHulpmiddel en Device zelf niet helemaal

## EHDSProcedure.identifier

### Table

| attribute | value |
|---|---|
| xtehr | EHDSProcedure.identifier |
| zib |  |
| name_zib |  |
| path_zib |  |
| alias_zib |  |
| type_zib |  |
| card._zib |  |
| stereotype_zib |  |
| id_zib |  |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSProcedure.identifier |
| path_xtehr | EHDSProcedure.identifier |
| short_xtehr | C.16.1 - Identifier |
| definition_xtehr | Procedure identifier |
| type_xtehr | Identifier |
| card._xtehr | 0..* |
| binding_xtehr |  |

### Comments

* identifier is in de zib impliciet, in xtehr expliciet gemodelleerd

## EHDSProcedure.location

### Table

| attribute | value |
|---|---|
| xtehr | EHDSProcedure.location |
| zib | Procedure.Location::HealthcareProvider |
| name_zib | Location::HealthcareProvider |
| path_zib | Procedure.Location::HealthcareProvider |
| alias_zib | NL: Locatie::Zorgaanbieder |
| type_zib |  |
| card._zib | 0..1 |
| stereotype_zib | context,reference |
| id_zib | NL-CM:14.1.5 |
| definition_zib | The healthcare center where the procedure was, is or or will be carried out. |
| definitioncode_zib |  |
| id_xtehr | EHDSProcedure.location |
| path_xtehr | EHDSProcedure.location |
| short_xtehr | C.16.12 - Location |
| definition_xtehr | Location where the procedure had been performed |
| type_xtehr | EHDSLocation |
| card._xtehr | 0..* |
| binding_xtehr |  |

### Comments

* xtehr staat meerdere locaties toe, zib max. 1

## EHDSProcedure.note

### Table

| attribute | value |
|---|---|
| xtehr | EHDSProcedure.note |
| zib |  |
| name_zib |  |
| path_zib |  |
| alias_zib |  |
| type_zib |  |
| card._zib |  |
| stereotype_zib |  |
| id_zib |  |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSProcedure.note |
| path_xtehr | EHDSProcedure.note |
| short_xtehr | C.16.13 - Note |
| definition_xtehr | Additional information about the procedure |
| type_xtehr | string |
| card._xtehr | 0..1 |
| binding_xtehr |  |

### Comments

* de xtehr heeft een 'note', deze zib geen 'toelichting'

## EHDSProcedure.outcome

### Table

| attribute | value |
|---|---|
| xtehr | EHDSProcedure.outcome |
| zib |  |
| name_zib |  |
| path_zib |  |
| alias_zib |  |
| type_zib |  |
| card._zib |  |
| stereotype_zib |  |
| id_zib |  |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSProcedure.outcome |
| path_xtehr | EHDSProcedure.outcome |
| short_xtehr | C.16.8 - Outcome |
| definition_xtehr | The outcome of the procedure - did it resolve the reasons for the procedure being performed? |
| type_xtehr | CodeableConcept |
| card._xtehr | 0..1 |
| binding_xtehr | {'strength': 'preferred', 'description': 'SNOMED CT'} |

### Comments

* de zib kent geen outcome'

## EHDSProcedure.performer

### Table

| attribute | value |
|---|---|
| xtehr | EHDSProcedure.performer |
| zib | Procedure.Performer::HealthProfessional |
| name_zib | Performer::HealthProfessional |
| path_zib | Procedure.Performer::HealthProfessional |
| alias_zib | NL: Uitvoerder::Zorgverlener |
| type_zib |  |
| card._zib | 0..* |
| stereotype_zib | context,reference |
| id_zib | NL-CM:14.1.6 |
| definition_zib | The healthcare provider who carried out or will carry out the procedure. In most cases, only the medical specialty is entered, and not the name of the healthcare provider. |
| definitioncode_zib |  |
| id_xtehr | EHDSProcedure.performer |
| path_xtehr | EHDSProcedure.performer |
| short_xtehr | C.16.5 - Performer |
| definition_xtehr | An actor who or what performed the procedure |
| type_xtehr | Reference |
| card._xtehr | 0..* |
| binding_xtehr |  |

### Comments

* compliant

## EHDSProcedure.reason

### Table

| attribute | value |
|---|---|
| xtehr | EHDSProcedure.reason |
| zib | Procedure.Indication::Problem |
| name_zib | Indication::Problem |
| path_zib | Procedure.Indication::Problem |
| alias_zib | NL: Indicatie::Probleem |
| type_zib |  |
| card._zib | 0..* |
| stereotype_zib | data,reference |
| id_zib | NL-CM:14.1.9 |
| definition_zib | The indication is the reason for the procedure. |
| definitioncode_zib | SNOMED CT: 363702006 Has focus |
| id_xtehr | EHDSProcedure.reason |
| path_xtehr | EHDSProcedure.reason |
| short_xtehr | C.16.7 - Reason |
| definition_xtehr | The reason why the procedure was performed. |
| type_xtehr | Reference |
| card._xtehr | 0..* |
| binding_xtehr |  |

### Comments

* compliant

## EHDSProcedure.subject

### Table

| attribute | value |
|---|---|
| xtehr | EHDSProcedure.subject |
| zib |  |
| name_zib |  |
| path_zib |  |
| alias_zib |  |
| type_zib |  |
| card._zib |  |
| stereotype_zib |  |
| id_zib |  |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSProcedure.subject |
| path_xtehr | EHDSProcedure.subject |
| short_xtehr | C.16.14 - Patient |
| definition_xtehr | On whom or on what the procedure was performed. This is usually an individual human, but can also be performed on animals, groups of humans or animals, organizations or practitioners (for licensing), locations or devices (for safety inspections or regulatory authorizations). If the actual focus of the procedure is different from the subject, the focus element specifies the actual focus of the procedure. |
| type_xtehr | Reference |
| card._xtehr | 1..1 |
| binding_xtehr |  |

### Comments

* subject (Patient) is in xtehr expliect gemodelleerd, in zibs impliciet

## zib: Procedure.ProcedureMethod

### Table

| attribute | value |
|---|---|
| xtehr |  |
| zib | Procedure.ProcedureMethod |
| name_zib | ProcedureMethod |
| path_zib | Procedure.ProcedureMethod |
| alias_zib | NL: VerrichtingMethode |
| type_zib | CD |
| card._zib | 0..* |
| stereotype_zib | data |
| id_zib | NL-CM:14.1.12 |
| definition_zib | the method or technique that was used to perform the procedure, e.g. approach, lavage, pressuring, ets |
| definitioncode_zib | SNOMED CT: 260686004 Method |
| id_xtehr |  |
| path_xtehr |  |
| short_xtehr |  |
| definition_xtehr |  |
| type_xtehr |  |
| card._xtehr |  |
| binding_xtehr |  |

### Comments

* xtehr kent geen methode (wel een 'deviceUsed' maar dat is niet hetzelfde)

## zib: Procedure.Requester::HealthProfessional

### Table

| attribute | value |
|---|---|
| xtehr |  |
| zib | Procedure.Requester::HealthProfessional |
| name_zib | Requester::HealthProfessional |
| path_zib | Procedure.Requester::HealthProfessional |
| alias_zib | NL: Aanvrager::Zorgverlener |
| type_zib |  |
| card._zib | 0..* |
| stereotype_zib | context,reference |
| id_zib | NL-CM:14.1.10 |
| definition_zib | The healthcare provider who requested the procedure. |
| definitioncode_zib |  |
| id_xtehr |  |
| path_xtehr |  |
| short_xtehr |  |
| definition_xtehr |  |
| type_xtehr |  |
| card._xtehr |  |
| binding_xtehr |  |

### Comments

* xtehr kent geen aanvrager