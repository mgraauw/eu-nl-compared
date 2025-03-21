# Condition

| zib                                                   | xtehr                                     | type_zib   | type_xtehr        | card._zib   | card._xtehr   |
|:------------------------------------------------------|:------------------------------------------|:-----------|:------------------|:------------|:--------------|
| Problem                                               | EHDSCondition                             |            |                   |             | 0..*          |
| Problem.ProblemAnatomicalLocation::AnatomicalLocation | EHDSCondition.anatomicLocation            |            | CodeableConcept   | 0..1        | 0..*          |
| Problem.ProblemType                                   | EHDSCondition.category                    | CD         | CodeableConcept   | 0..1        | 0..*          |
| Problem.ProblemStatus                                 | EHDSCondition.clinicalStatus              | CD         | CodeableConcept   | 1           | 0..1          |
| Problem.ProblemName                                   | EHDSCondition.code                        | CD         | CodeableConcept   | 1           | 0..1          |
|                                                       | EHDSCondition.description                 |            | Narrative         |             | 0..1          |
| Problem.VerificationStatus                            | EHDSCondition.diagnosisAssertionStatus    | CD         | CodeableConcept   | 0..1        | 0..1          |
| Problem.ProblemEndDate                                | EHDSCondition.endDate                     | TS         | dateTime          | 0..1        | 0..1          |
|                                                       | EHDSCondition.externalResourceRelatedWith |            | uri               |             | 0..*          |
|                                                       | EHDSCondition.identifier                  |            | Identifier        |             | 0..*          |
| Problem.ProblemStartDate                              | EHDSCondition.onsetDate                   | TS         | dateTime          | 0..1        | 0..1          |
|                                                       | EHDSCondition.participant                 |            | Base              |             | 0..*          |
|                                                       | EHDSCondition.participant.actor           |            | Reference         |             | 1..1          |
|                                                       | EHDSCondition.participant.function        |            | CodeableConcept   |             | 0..1          |
|                                                       | EHDSCondition.patient                     |            | Reference         |             | 1..1          |
|                                                       | EHDSCondition.resolutionCircumstances     |            | CodeableReference |             | 0..*          |
|                                                       | EHDSCondition.severity                    |            | CodeableConcept   |             | 0..1          |
|                                                       | EHDSCondition.stage                       |            | CodeableConcept   |             | 0..*          |
| Problem.Comment                                       |                                           | ST         |                   | 0..1        |               |
| Problem.FurtherSpecificationProblemName               |                                           | ST         |                   | 0..1        |               |



## EHDSCondition

### Table

| attribute | value |
|---|---|
| xtehr | EHDSCondition |
| zib | Problem |
| alias_zib | NL: Probleem |
| binding_xtehr |  |
| card._xtehr | 0..* |
| card._zib |  |
| definition_xtehr | C.15 - EHDS refined base model for A clinical condition, problem, diagnosis, or other event, situation, issue, or clinical concept that has risen to a level of concern. |
| definition_zib | Root concept of the Problem information model.
A problem describes a situation with regard to an individual’s health and/or welfare. This situation can be described by the patient  himselve (in the form of a complaint) or by their healthprofessional (in the form of a diagnosis, for example). |
| definitioncode_zib |  |
| id_xtehr | EHDSCondition |
| id_zib | NL-CM:5.1.1 |
| name_zib | Problem |
| path_xtehr | EHDSCondition |
| path_zib | Problem |
| short_xtehr | Condition model |
| stereotype_zib | rootconcept |
| type_xtehr |  |
| type_zib |  |

### Comments



## EHDSCondition.anatomicLocation

### Table

| attribute | value |
|---|---|
| xtehr | EHDSCondition.anatomicLocation |
| zib | Problem.ProblemAnatomicalLocation::AnatomicalLocation |
| alias_zib | NL: ProbleemAnatomischeLocatie::AnatomischeLocatie |
| binding_xtehr | {'strength': 'preferred', 'description': 'SNOMED CT'} |
| card._xtehr | 0..* |
| card._zib | 0..1 |
| definition_xtehr | The anatomical location including laterality where this condition manifests itself. |
| definition_zib | Anatomical location which is the focus of the problem. |
| definitioncode_zib | SNOMED CT: 405813007 Procedure site - Direct |
| id_xtehr | EHDSCondition.anatomicLocation |
| id_zib | NL-CM:5.1.14 |
| name_zib | ProblemAnatomicalLocation::AnatomicalLocation |
| path_xtehr | EHDSCondition.anatomicLocation |
| path_zib | Problem.ProblemAnatomicalLocation::AnatomicalLocation |
| short_xtehr | C.15.10 - Anatomic location |
| stereotype_zib | data,reference |
| type_xtehr | CodeableConcept |
| type_zib |  |

### Comments



## EHDSCondition.category

### Table

| attribute | value |
|---|---|
| xtehr | EHDSCondition.category |
| zib | Problem.ProblemType |
| alias_zib | NL: ProbleemType |
| binding_xtehr |  |
| card._xtehr | 0..* |
| card._zib | 0..1 |
| definition_xtehr | Category or categories of the problem. |
| definition_zib | The type of problem; see the concept description. |
| definitioncode_zib |  |
| id_xtehr | EHDSCondition.category |
| id_zib | NL-CM:5.1.8 |
| name_zib | ProblemType |
| path_xtehr | EHDSCondition.category |
| path_zib | Problem.ProblemType |
| short_xtehr | C.15.6 - Category |
| stereotype_zib | data |
| type_xtehr | CodeableConcept |
| type_zib | CD |

### Comments



## EHDSCondition.clinicalStatus

### Table

| attribute | value |
|---|---|
| xtehr | EHDSCondition.clinicalStatus |
| zib | Problem.ProblemStatus |
| alias_zib | NL: ProbleemStatus |
| binding_xtehr | {'strength': 'preferred', 'description': 'HL7 Condtion-clinical'} |
| card._xtehr | 0..1 |
| card._zib | 1 |
| definition_xtehr | Status of the condition/problem (active, resolved, inactive, ...) |
| definition_zib | The problem status describes the condition of the problem: 
1.  Active problems are problems of which the patient experiences symptoms or for which evidence exists. 
    <li>Problems with the status 'Inactive' refer to problems that don't affect the patient anymore or that of which there is no evidence of existence anymore. 
2.  Problems with the status 'Inactive' refer to problems that don't affect the patient anymore or that of which there is no evidence of existence anymore.  |
| definitioncode_zib |  |
| id_xtehr | EHDSCondition.clinicalStatus |
| id_zib | NL-CM:5.1.4 |
| name_zib | ProblemStatus |
| path_xtehr | EHDSCondition.clinicalStatus |
| path_zib | Problem.ProblemStatus |
| short_xtehr | C.15.7 - Clinical status |
| stereotype_zib | data |
| type_xtehr | CodeableConcept |
| type_zib | CD |

### Comments



## EHDSCondition.code

### Table

| attribute | value |
|---|---|
| xtehr | EHDSCondition.code |
| zib | Problem.ProblemName |
| alias_zib | NL: ProbleemNaam |
| binding_xtehr | {'strength': 'preferred', 'description': 'ICD-10*, SNOMED CT, Orphacode if rare disease is diagnosed'} |
| card._xtehr | 0..1 |
| card._zib | 1 |
| definition_xtehr | Code identifying the condition, problem or diagnosis |
| definition_zib | The problem name defines the problem. Depending on the setting, different code systems can be used. The ProblemNameCodelist provides an overview of the possible code systems. |
| definitioncode_zib |  |
| id_xtehr | EHDSCondition.code |
| id_zib | NL-CM:5.1.3 |
| name_zib | ProblemName |
| path_xtehr | EHDSCondition.code |
| path_zib | Problem.ProblemName |
| short_xtehr | C.15.3 - Code |
| stereotype_zib | data |
| type_xtehr | CodeableConcept |
| type_zib | CD |

### Comments



## EHDSCondition.description

### Table

| attribute | value |
|---|---|
| xtehr | EHDSCondition.description |
| zib |  |
| alias_zib |  |
| binding_xtehr |  |
| card._xtehr | 0..1 |
| card._zib |  |
| definition_xtehr | Condition specification in narrative form |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSCondition.description |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSCondition.description |
| path_zib |  |
| short_xtehr | C.15.2 - Description |
| stereotype_zib |  |
| type_xtehr | Narrative |
| type_zib |  |

### Comments



## EHDSCondition.diagnosisAssertionStatus

### Table

| attribute | value |
|---|---|
| xtehr | EHDSCondition.diagnosisAssertionStatus |
| zib | Problem.VerificationStatus |
| alias_zib | NL: VerificatieStatus |
| binding_xtehr | {'strength': 'preferred', 'description': 'HL7 Condition-ver-status'} |
| card._xtehr | 0..1 |
| card._zib | 0..1 |
| definition_xtehr | Assertion about the certainty associated with a diagnosis. Diagnostic and/or clinical evidence of condition. |
| definition_zib | Clinical status of the problem or the diagnosis. |
| definitioncode_zib | SNOMED CT: 408729009 Finding context |
| id_xtehr | EHDSCondition.diagnosisAssertionStatus |
| id_zib | NL-CM:5.1.10 |
| name_zib | VerificationStatus |
| path_xtehr | EHDSCondition.diagnosisAssertionStatus |
| path_zib | Problem.VerificationStatus |
| short_xtehr | C.15.15 - Diagnosis assertion status |
| stereotype_zib | data |
| type_xtehr | CodeableConcept |
| type_zib | CD |

### Comments



## EHDSCondition.endDate

### Table

| attribute | value |
|---|---|
| xtehr | EHDSCondition.endDate |
| zib | Problem.ProblemEndDate |
| alias_zib | NL: ProbleemEindDatum |
| binding_xtehr |  |
| card._xtehr | 0..1 |
| card._zib | 0..1 |
| definition_xtehr | The date or estimated date that the condition resolved or went into remission. |
| definition_zib | Date on which the disorder to which the problem applies, is considered not to be present anymore.This datum needs not to be the same as the date of the change in problem status. A ‘vague’ date, such as only the year or the month and the year, is permitted. |
| definitioncode_zib |  |
| id_xtehr | EHDSCondition.endDate |
| id_zib | NL-CM:5.1.9 |
| name_zib | ProblemEndDate |
| path_xtehr | EHDSCondition.endDate |
| path_zib | Problem.ProblemEndDate |
| short_xtehr | C.15.5 - End date |
| stereotype_zib | data |
| type_xtehr | dateTime |
| type_zib | TS |

### Comments



## EHDSCondition.externalResourceRelatedWith

### Table

| attribute | value |
|---|---|
| xtehr | EHDSCondition.externalResourceRelatedWith |
| zib |  |
| alias_zib |  |
| binding_xtehr |  |
| card._xtehr | 0..* |
| card._zib |  |
| definition_xtehr | Identify the External Resource which may be specifically relatedto the problem, for example a link between a rare disease problemand the corresponding guidelines. |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSCondition.externalResourceRelatedWith |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSCondition.externalResourceRelatedWith |
| path_zib |  |
| short_xtehr | C.15.14 - External Resourcerelated with |
| stereotype_zib |  |
| type_xtehr | uri |
| type_zib |  |

### Comments



## EHDSCondition.identifier

### Table

| attribute | value |
|---|---|
| xtehr | EHDSCondition.identifier |
| zib |  |
| alias_zib |  |
| binding_xtehr |  |
| card._xtehr | 0..* |
| card._zib |  |
| definition_xtehr | Condition identifier |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSCondition.identifier |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSCondition.identifier |
| path_zib |  |
| short_xtehr | C.15.1 - Identifier |
| stereotype_zib |  |
| type_xtehr | Identifier |
| type_zib |  |

### Comments



## EHDSCondition.onsetDate

### Table

| attribute | value |
|---|---|
| xtehr | EHDSCondition.onsetDate |
| zib | Problem.ProblemStartDate |
| alias_zib | NL: ProbleemBeginDatum |
| binding_xtehr |  |
| card._xtehr | 0..1 |
| card._zib | 0..1 |
| definition_xtehr | Onset date of a problem/condition |
| definition_zib | Onset of the symptom, complaint, functional limitation, complication or date of diagnosis. A ‘vague’ date, such as only the year or the month and the year, is permitted. |
| definitioncode_zib |  |
| id_xtehr | EHDSCondition.onsetDate |
| id_zib | NL-CM:5.1.6 |
| name_zib | ProblemStartDate |
| path_xtehr | EHDSCondition.onsetDate |
| path_zib | Problem.ProblemStartDate |
| short_xtehr | C.15.4 - Onset date |
| stereotype_zib | data |
| type_xtehr | dateTime |
| type_zib | TS |

### Comments



## EHDSCondition.participant

### Table

| attribute | value |
|---|---|
| xtehr | EHDSCondition.participant |
| zib |  |
| alias_zib |  |
| binding_xtehr |  |
| card._xtehr | 0..* |
| card._zib |  |
| definition_xtehr | Who or what participated in the activities related to the condition and how they were involved. |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSCondition.participant |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSCondition.participant |
| path_zib |  |
| short_xtehr | C.15.13 - Participant |
| stereotype_zib |  |
| type_xtehr | Base |
| type_zib |  |

### Comments



## EHDSCondition.participant.actor

### Table

| attribute | value |
|---|---|
| xtehr | EHDSCondition.participant.actor |
| zib |  |
| alias_zib |  |
| binding_xtehr |  |
| card._xtehr | 1..1 |
| card._zib |  |
| definition_xtehr | Identify the Health Professional who may be specifically related to the condition, e.g., as a preferred contact. |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSCondition.participant.actor |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSCondition.participant.actor |
| path_zib |  |
| short_xtehr | C.15.13.2 - Actor |
| stereotype_zib |  |
| type_xtehr | Reference |
| type_zib |  |

### Comments



## EHDSCondition.participant.function

### Table

| attribute | value |
|---|---|
| xtehr | EHDSCondition.participant.function |
| zib |  |
| alias_zib |  |
| binding_xtehr | {'strength': 'preferred', 'description': 'To be specified'} |
| card._xtehr | 0..1 |
| card._zib |  |
| definition_xtehr | Type of participant involvement. |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSCondition.participant.function |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSCondition.participant.function |
| path_zib |  |
| short_xtehr | C.15.13.1 - Function |
| stereotype_zib |  |
| type_xtehr | CodeableConcept |
| type_zib |  |

### Comments



## EHDSCondition.patient

### Table

| attribute | value |
|---|---|
| xtehr | EHDSCondition.patient |
| zib |  |
| alias_zib |  |
| binding_xtehr |  |
| card._xtehr | 1..1 |
| card._zib |  |
| definition_xtehr | Indicates the patient or group who the condition record is associated with. |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSCondition.patient |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSCondition.patient |
| path_zib |  |
| short_xtehr | C.15.12 - Subject |
| stereotype_zib |  |
| type_xtehr | Reference |
| type_zib |  |

### Comments



## EHDSCondition.resolutionCircumstances

### Table

| attribute | value |
|---|---|
| xtehr | EHDSCondition.resolutionCircumstances |
| zib |  |
| alias_zib |  |
| binding_xtehr |  |
| card._xtehr | 0..* |
| card._zib |  |
| definition_xtehr | Describes the reason for which the status of the problem changed from current to inactive (e.g. surgical procedure, medical treatment, etc.). This field includes "free text" if the resolution circumstances are not already included in other fields such as surgical procedure, medical device, etc., e.g. hepatic cystectomy (this will be the resolution circumstances for the problem "hepatic cyst" and will be included in surgical procedures). |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSCondition.resolutionCircumstances |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSCondition.resolutionCircumstances |
| path_zib |  |
| short_xtehr | C.15.8 - Resolution circumstances |
| stereotype_zib |  |
| type_xtehr | CodeableReference |
| type_zib |  |

### Comments



## EHDSCondition.severity

### Table

| attribute | value |
|---|---|
| xtehr | EHDSCondition.severity |
| zib |  |
| alias_zib |  |
| binding_xtehr | {'strength': 'preferred', 'description': 'HL7 Condtion-severity'} |
| card._xtehr | 0..1 |
| card._zib |  |
| definition_xtehr | A subjective assessment of the severity of the condition as evaluated by the clinician. |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSCondition.severity |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSCondition.severity |
| path_zib |  |
| short_xtehr | C.15.9 - Severity |
| stereotype_zib |  |
| type_xtehr | CodeableConcept |
| type_zib |  |

### Comments



## EHDSCondition.stage

### Table

| attribute | value |
|---|---|
| xtehr | EHDSCondition.stage |
| zib |  |
| alias_zib |  |
| binding_xtehr | {'strength': 'preferred', 'description': 'e.g. TNM, ICD-O-3, Bi-Rads, Li-Rads, …'} |
| card._xtehr | 0..* |
| card._zib |  |
| definition_xtehr | Stage/grade usually assessed formally using a specific staging/grading system. Multiple assessment systems could be used. |
| definition_zib |  |
| definitioncode_zib |  |
| id_xtehr | EHDSCondition.stage |
| id_zib |  |
| name_zib |  |
| path_xtehr | EHDSCondition.stage |
| path_zib |  |
| short_xtehr | C.15.11 - Stage |
| stereotype_zib |  |
| type_xtehr | CodeableConcept |
| type_zib |  |

### Comments



## zib: Problem.Comment

### Table

| attribute | value |
|---|---|
| xtehr |  |
| zib | Problem.Comment |
| alias_zib | NL: Toelichting |
| binding_xtehr |  |
| card._xtehr |  |
| card._zib | 0..1 |
| definition_xtehr |  |
| definition_zib | Comment by the one who determined or updated the Problem. |
| definitioncode_zib | LOINC: 48767-8 Annotation comment [Interpretation] Narrative |
| id_xtehr |  |
| id_zib | NL-CM:5.1.5 |
| name_zib | Comment |
| path_xtehr |  |
| path_zib | Problem.Comment |
| short_xtehr |  |
| stereotype_zib | data |
| type_xtehr |  |
| type_zib | ST |

### Comments



## zib: Problem.FurtherSpecificationProblemName

### Table

| attribute | value |
|---|---|
| xtehr |  |
| zib | Problem.FurtherSpecificationProblemName |
| alias_zib | NL: NadereSpecificatieProbleemNaam |
| binding_xtehr |  |
| card._xtehr |  |
| card._zib | 0..1 |
| definition_xtehr |  |
| definition_zib | Further specification of problem name when it is recorded via a thesaurus or code system in which the required level of detail is not (yet) available. |
| definitioncode_zib |  |
| id_xtehr |  |
| id_zib | NL-CM:5.1.13 |
| name_zib | FurtherSpecificationProblemName |
| path_xtehr |  |
| path_zib | Problem.FurtherSpecificationProblemName |
| short_xtehr |  |
| stereotype_zib | data |
| type_xtehr |  |
| type_zib | ST |

### Comments

