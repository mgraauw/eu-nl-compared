# Patient

| zib                                 | xtehr                             | type_zib   | type_xtehr      | card._zib   | card._xtehr   |
|:------------------------------------|:----------------------------------|:-----------|:----------------|:------------|:--------------|
| Patient                             | EHDSPatient                       |            |                 |             | 0..*          |
| Patient.AddressInformation          | EHDSPatient.address               |            | EHDSAddress     | 0..*        | 0..*          |
| Patient.Gender                      | EHDSPatient.administrativeGender  | CD         | CodeableConcept | 0..1        | 0..1          |
|                                     | EHDSPatient.citizenship           |            | CodeableConcept |             | 0..*          |
|                                     | EHDSPatient.communicationLanguage |            | CodeableConcept |             | 0..*          |
| Patient.DateOfBirth                 | EHDSPatient.dateOfBirth           | TS         | dateTime        | 0..1        | 0..1          |
|                                     | EHDSPatient.maritalStatus         |            | CodeableConcept |             | 0..1          |
| Patient.NameInformation             | EHDSPatient.name                  |            | EHDSHumanName   | 0..1        | 0..*          |
| Patient.PatientIdentificationNumber | EHDSPatient.personalIdentifier    | II         | Identifier      | 0..*        | 1..*          |
|                                     | EHDSPatient.telecom               |            | EHDSTelecom     |             | 0..*          |
| Patient.ContactInformation          |                                   |            |                 | 0..1        |               |
| Patient.DateOfDeath                 |                                   | TS         |                 | 0..1        |               |
| Patient.DeathIndicator              |                                   | BL         |                 | 0..1        |               |
| Patient.MultipleBirthIndicator      |                                   | BL         |                 | 0..1        |               |



## EHDSPatient

### Table

| attribute | value |
|---|---|
| xtehr | EHDSPatient |
| zib | Patient |
| name_zib | Patient |
| path_zib | Patient |
| alias_zib | NL: Patient |
| type_zib |  |
| card._zib |  |
| stereotype_zib | rootconcept |
| id_zib | NL-CM:0.1.1 |
| definition_zib | Root concept of the Patient information model. This root concept contains all data elements of the Patient information model. |
| definitioncode_zib | SNOMED CT: 116154003 Patient |
| id_xtehr | EHDSPatient |
| path_xtehr | EHDSPatient |
| short_xtehr | Patient model |
| definition_xtehr | C.1 - EHDS refined base model for Patient/subject information |
| type_xtehr |  |
| card._xtehr | 0..* |
| binding_xtehr |  |

### Comments



## EHDSPatient.address

### Table

| attribute | value |
|---|---|
| xtehr | EHDSPatient.address |
| zib | Patient.AddressInformation |
| name_zib | AddressInformation |
| path_zib | Patient.AddressInformation |
| alias_zib | NL: Adresgegevens |
| type_zib |  |
| card._zib | 0..* |
| stereotype_zib | data,reference |
| id_zib | NL-CM:0.1.4 |
| definition_zib | Patient's address information. |
| definitioncode_zib |  |
| id_xtehr | EHDSPatient.address |
| path_xtehr | EHDSPatient.address |
| short_xtehr | C.1.5 - Address |
| definition_xtehr | Mailing and home or office addresses. The addresses are always sequences of address parts (e.g. street address line, country, ZIP code, city) even if postal address formats may vary depending on the country. An address may or may not include a specific use code; if this attribute is not present it is assumed to be the default address useful for any purpose. |
| type_xtehr | EHDSAddress |
| card._xtehr | 0..* |
| binding_xtehr |  |

### Comments

* compliant

## EHDSPatient.administrativeGender

### Table

| attribute | value |
|---|---|
| xtehr | EHDSPatient.administrativeGender |
| zib | Patient.Gender |
| name_zib | Gender |
| path_zib | Patient.Gender |
| alias_zib | NL: Geslacht |
| type_zib | CD |
| card._zib | 0..1 |
| stereotype_zib | data |
| id_zib | NL-CM:0.1.9 |
| definition_zib | Patient’s administrative gender. |
| definitioncode_zib | LOINC: 46098-0 Sex |
| id_xtehr | EHDSPatient.administrativeGender |
| path_xtehr | EHDSPatient.administrativeGender |
| short_xtehr | C.1.4 - Administrative gender |
| definition_xtehr | This field must contain a recognized valid value for "administrative gender". If different, "physiological gender" should be communicated elsewhere.  |
| type_xtehr | CodeableConcept |
| card._xtehr | 0..1 |
| binding_xtehr | {'strength': 'preferred', 'description': 'HL7 Administrative Gender'} |

### Comments

* compliant

## EHDSPatient.citizenship

### Table

| attribute | value |
|---|---|
| xtehr | EHDSPatient.citizenship |
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
| id_xtehr | EHDSPatient.citizenship |
| path_xtehr | EHDSPatient.citizenship |
| short_xtehr | C.1.8 - Citizenship (nationality) |
| definition_xtehr | Citizenship/nationality of the patient. |
| type_xtehr | CodeableConcept |
| card._xtehr | 0..* |
| binding_xtehr | {'strength': 'preferred', 'description': 'ISO 3166-1-2'} |

### Comments

* zib Patient heeft geen citizenship
  * er is wel een aparte zib [Nationaliteit](https://zibs.nl/wiki/Nationality-v3.0(2020EN)) hiervoor
  * zib heeft GBA codes, xteht heeft preferred ISO landencodes
  * er is een mapping voor cross-border eHN via NCP

## EHDSPatient.communicationLanguage

### Table

| attribute | value |
|---|---|
| xtehr | EHDSPatient.communicationLanguage |
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
| id_xtehr | EHDSPatient.communicationLanguage |
| path_xtehr | EHDSPatient.communicationLanguage |
| short_xtehr | C.1.9 - Communcation language |
| definition_xtehr | The language which can be used to communicate with the patient about his or her health. |
| type_xtehr | CodeableConcept |
| card._xtehr | 0..* |
| binding_xtehr | {'strength': 'preferred', 'description': 'BCP 47'} |

### Comments

* zib heeft geen communicationLanguage
  * er is wel een zib [LanguageProficiency-v3.2](https://zibs.nl/wiki/LanguageProficiency-v3.2(2020EN))
  * deze zib bevat meer dan alleen de communicationLanguage
  * de zib heeft ISO-639-2 alpha als codering taal
  * xtehr schrijft [BCP 47](https://en.wikipedia.org/wiki/IETF_language_tag) voor, het lijkt erop dat ISO-639-2 een subset daarvan is
  * mogelijk mapping of verder uitzoeken nodig

## EHDSPatient.dateOfBirth

### Table

| attribute | value |
|---|---|
| xtehr | EHDSPatient.dateOfBirth |
| zib | Patient.DateOfBirth |
| name_zib | DateOfBirth |
| path_zib | Patient.DateOfBirth |
| alias_zib | NL: Geboortedatum |
| type_zib | TS |
| card._zib | 0..1 |
| stereotype_zib | data |
| id_zib | NL-CM:0.1.10 |
| definition_zib | Patient’s date of birth. The date of birth is mandatory for a patient. A vague date (such as only the year) is permitted. |
| definitioncode_zib | LOINC: 21112-8 Birth date |
| id_xtehr | EHDSPatient.dateOfBirth |
| path_xtehr | EHDSPatient.dateOfBirth |
| short_xtehr | C.1.3 - Date of birth |
| definition_xtehr | The date of birth of the patient [ISO TS 22220]. As age of the patient might be important for correct interpretation of the test result values, complete date of birth should be provided. |
| type_xtehr | dateTime |
| card._xtehr | 0..1 |
| binding_xtehr |  |

### Comments

* compliant

## EHDSPatient.maritalStatus

### Table

| attribute | value |
|---|---|
| xtehr | EHDSPatient.maritalStatus |
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
| id_xtehr | EHDSPatient.maritalStatus |
| path_xtehr | EHDSPatient.maritalStatus |
| short_xtehr | C.1.7 - Marital status |
| definition_xtehr | Marital (civil) status of a patient |
| type_xtehr | CodeableConcept |
| card._xtehr | 0..1 |
| binding_xtehr | {'strength': 'preferred', 'description': 'HL7 marital-status'} |

### Comments

* de zib kent geen MaritalStatus attribuut
  * er is wel een zib [MaritalStatus-v3.1)](https://zibs.nl/wiki/MaritalStatus-v3.1(2020EN)
  * beiden gebruiken een HL7 codesysteem
  * wel nagaan of dezelfde versie daarvan gebruikt wordt

## EHDSPatient.name

### Table

| attribute | value |
|---|---|
| xtehr | EHDSPatient.name |
| zib | Patient.NameInformation |
| name_zib | NameInformation |
| path_zib | Patient.NameInformation |
| alias_zib | NL: Naamgegevens |
| type_zib |  |
| card._zib | 0..1 |
| stereotype_zib | data,reference |
| id_zib | NL-CM:0.1.6 |
| definition_zib | Patient's full name. |
| definitioncode_zib |  |
| id_xtehr | EHDSPatient.name |
| path_xtehr | EHDSPatient.name |
| short_xtehr | C.1.2 - Name |
| definition_xtehr | Name associated with the patient/subject. Name might consist of name parts, e.g. Given name or names, family name/surname, name prefix etc. |
| type_xtehr | EHDSHumanName |
| card._xtehr | 0..* |
| binding_xtehr |  |

### Comments

* xtehr kent nul of meer namen, de zib nul of een
  * vanuit Patient compliant
  * maar de naam zelf niet
  * zib heeft GBA-model
  * xtehr heeft een eigen naam model

## EHDSPatient.personalIdentifier

### Table

| attribute | value |
|---|---|
| xtehr | EHDSPatient.personalIdentifier |
| zib | Patient.PatientIdentificationNumber |
| name_zib | PatientIdentificationNumber |
| path_zib | Patient.PatientIdentificationNumber |
| alias_zib | NL: Identificatienummer |
| type_zib | II |
| card._zib | 0..* |
| stereotype_zib | data |
| id_zib | NL-CM:0.1.7 |
| definition_zib | The patient’s identification number. In transfer situations, use of the social security number (BSN) must comply with the Use of Social Security Numbers in Healthcare Act (Wbsn-z). In other situations, other number systems can be used, such as internal hospital patient numbers for example. |
| definitioncode_zib |  |
| id_xtehr | EHDSPatient.personalIdentifier |
| path_xtehr | EHDSPatient.personalIdentifier |
| short_xtehr | C.1.1 - Personal identifier |
| definition_xtehr | An identifier of the patient that is unique within a defined scope. Example: National ID (birth number) or National patient identifier for the Czech patient. Multiple identifiers could be provided.  |
| type_xtehr | Identifier |
| card._xtehr | 1..* |
| binding_xtehr |  |

### Comments

* de zib heeft 0..* voor BSN
* xtehr heeft 1..* voor personalIdentifier
* zib kent alleen BSN
* xtehr staat allerlei identifiers toe

## EHDSPatient.telecom

### Table

| attribute | value |
|---|---|
| xtehr | EHDSPatient.telecom |
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
| id_xtehr | EHDSPatient.telecom |
| path_xtehr | EHDSPatient.telecom |
| short_xtehr | C.1.6 - Telecom |
| definition_xtehr | Telecommunication contact information (addresses) associated to a person. Multiple telecommunication addresses might be provided. |
| type_xtehr | EHDSTelecom |
| card._xtehr | 0..* |
| binding_xtehr |  |

### Comments

* zib heeft een ander model voor telecom
* het lijkt compliant te maken

## zib: Patient.ContactInformation

### Table

| attribute | value |
|---|---|
| xtehr |  |
| zib | Patient.ContactInformation |
| name_zib | ContactInformation |
| path_zib | Patient.ContactInformation |
| alias_zib | NL: Contactgegevens |
| type_zib |  |
| card._zib | 0..1 |
| stereotype_zib | data,reference |
| id_zib | NL-CM:0.1.5 |
| definition_zib | Patient’s telephone number(s) or e-mail address(es). |
| definitioncode_zib |  |
| id_xtehr |  |
| path_xtehr |  |
| short_xtehr |  |
| definition_xtehr |  |
| type_xtehr |  |
| card._xtehr |  |
| binding_xtehr |  |

### Comments

* zie boven onder telecom

## zib: Patient.DateOfDeath

### Table

| attribute | value |
|---|---|
| xtehr |  |
| zib | Patient.DateOfDeath |
| name_zib | DateOfDeath |
| path_zib | Patient.DateOfDeath |
| alias_zib | NL: DatumOverlijden |
| type_zib | TS |
| card._zib | 0..1 |
| stereotype_zib | data |
| id_zib | NL-CM:0.1.33 |
| definition_zib | The date on which the patient died. A ‘vague’ date, such as only the year, is permitted. |
| definitioncode_zib | LOINC: 81954-0 Date of death [Date] |
| id_xtehr |  |
| path_xtehr |  |
| short_xtehr |  |
| definition_xtehr |  |
| type_xtehr |  |
| card._xtehr |  |
| binding_xtehr |  |

### Comments

* DateOfDeath zit niet in xtehr logical model

## zib: Patient.DeathIndicator

### Table

| attribute | value |
|---|---|
| xtehr |  |
| zib | Patient.DeathIndicator |
| name_zib | DeathIndicator |
| path_zib | Patient.DeathIndicator |
| alias_zib | NL: OverlijdensIndicator |
| type_zib | BL |
| card._zib | 0..1 |
| stereotype_zib | data |
| id_zib | NL-CM:0.1.32 |
| definition_zib | An indication stating whether the patient has died. |
| definitioncode_zib | SNOMED CT: 397709008 Patient died |
| id_xtehr |  |
| path_xtehr |  |
| short_xtehr |  |
| definition_xtehr |  |
| type_xtehr |  |
| card._xtehr |  |
| binding_xtehr |  |

### Comments

* DeathIndicator zit niet in xtehr logical model

## zib: Patient.MultipleBirthIndicator

### Table

| attribute | value |
|---|---|
| xtehr |  |
| zib | Patient.MultipleBirthIndicator |
| name_zib | MultipleBirthIndicator |
| path_zib | Patient.MultipleBirthIndicator |
| alias_zib | NL: MeerlingIndicator |
| type_zib | BL |
| card._zib | 0..1 |
| stereotype_zib | data |
| id_zib | NL-CM:0.1.31 |
| definition_zib | An indication stating whether the patient is of a multiple birth. |
| definitioncode_zib |  |
| id_xtehr |  |
| path_xtehr |  |
| short_xtehr |  |
| definition_xtehr |  |
| type_xtehr |  |
| card._xtehr |  |
| binding_xtehr |  |

### Comments

* MultipleBirthIndicator zit niet in xtehr logical model