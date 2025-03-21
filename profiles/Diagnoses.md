# Diagnoses
## Relevant artifacts:
* zib2017:
    * [Problem](https://zibs.nl/wiki/Problem-v4.0(2017EN))
    * [profile zib-Problem](https://simplifier.net/packages/nictiz.fhir.nl.stu3.zib2017/2.2.20/files/2741966)
* zib2020:
    * [Problem](https://zibs.nl/wiki/Problem-v4.4(2020EN))
    * [Profile zib-Problem](https://simplifier.net/packages/nictiz.fhir.nl.r4.zib2020/0.11.0-beta.1/files/2628252)
    * [Profile nl-core-Problem](https://simplifier.net/packages/nictiz.fhir.nl.r4.nl-core/0.11.0-beta.1/files/2628599)
* zib2024 (pre-publication):
    * [Condition](https://zibs.nl/wiki/Condition-v1.0(2024EN)) (wordt "Aandoening")
    * [DiagnistischInzicht](https://zibs.nl/wiki/DiagnosticInsight-v1.0(2024EN))
    * [Symptom](https://zibs.nl/wiki/Symptom-v1.0(2024EN))
    * Profiles are still under construction
* EHDS:
    * [EHDSCondition](https://build.fhir.org/ig/Xt-EHR/xt-ehr-common/StructureDefinition-EHDSCondition.html) (logical model)
    * [EPS ClosedProblem](https://build.fhir.org/ig/hl7-eu/eps/StructureDefinition-ClosedProblem.html) (logical model)
    * [EPS Problem](https://build.fhir.org/ig/hl7-eu/eps/StructureDefinition-Problem.html) (logical model, current problems)
    * [ConditionUvIps](https://build.fhir.org/ig/HL7/fhir-ips/StructureDefinition-Condition-uv-ips.html) (IPS 2)
    * [ConditionEuEps](https://build.fhir.org/ig/hl7-eu/eps/StructureDefinition-condition-eu-eps.html) (EU PS, based on IPS 2)

## In general
In the IPS, the section "Problems" is mandatory. The ConditionUvIps profile is used for this purpose. When there are no (known) problems, this is communicated using a Condition with `Condition.code` set to _no-problem-info_ or _no-known-problems_. So within the IPS, the Condition resource can be used to indicate that there are _no_ problems. In the ballot version of the IPS 2, this changes a bit; no known problems are communicated using `.section.emptyReason` in the Composition, ór using a Condition where `Condition.code` is populated with SNOMED 160245001 (No current problems or disability). 

The section "Past problems" is optional. The same profile is used as for current problems. However, it seems like the intent is not to use a Condition to indicate that there are no past problems -- for the IPS 2, the code is specifically about _current_ problems. Clear guidance is missing however.

Highlights of this profile:

1. `Condition.code` is mandatory.
2. `Condition.clinicalStatus` is mandatory.
3. `Condition.subject` must be a Patient according to the IPS profile.
4. `mustSupport` flags are present on `.clinicalStatus`, `.category`, `.severity`, `.code`, `.subject` and `.onsetDateDate`.
5. Some terminology bindings are added, none of them _required_._

The EPS also mentions "Problem", and has sections for current and past problems as well. For this purpose, the ConditionEuEps-profiel is used, which is derived from the ConditionUvIps profile. Highlights:

1. `Condition.severity` has a _required_ binding to a ValieSet woth six SNOMED concepts.
2. `Condition.onset[x]` and `Condition.abatement[x]` are constrained to data type _dateTime_.
3. An optional pre-adopt is present for `Condition.participant` (and constrained to 0..1)
4. Two optional extensions are added: for supporting info (as DocumentReference) and for status reason (as string).

For zib2017, there's one profile. Highlights:

1. `Condition.clinicalStatus` is required, and an extension is present for exchanging an additional SNOMED code for "active" or "inactive".
2. On `Condition.verificationStatus`, an extension is present for additional SNOMED codes from the zib.
3. On `Condition.category`, a SNOMED ValueSet is bound (_extensible_).
4. `Condition.code` is mandatory.
5. On `Condition.bodySite`, an optional extension for laterality is present.
6. `Condition.onset[x]` and `Condition.abatement[x]` are constrained to data type _dateTime_.
7. On `Condition.asserter`, an optional extension is present for the practitioner role.

For zib2020, there is one profile (or two, if you consider zib- and nl-core-):

1. On `Condition.clinicalStatus` a ConceptMap is present to translate between zib and FHIR ValueSets.
2. On `Condition.verificationStatus`, the requirement has been added to exchange the zib value next to the FHIR value.
3. On `Condition.code`, a _required_ binding is present to the zib ValueSet (which is very broad).
4. `Condition.bodySite` is restricted to 0..1.
5. `Condition.note` is constrained to 0..1.

Voor 2024, there are no profiles yet. Howver, the zib modeling becomes a lot complexer, which could result in a non-straightforwared mapping to FHIR:

1. The zibs separate the condition itself froms any diagnoses about it. A straightforward mapping of this model would result in multuple Conditions for the same "problem"; one containing the problem type (the diagnosis) and one containing things like the period present (the condition itself).
2. Furthermore, a straightforward mapping could result in "diagnosis" Conditions that are in the past while the "condition" Condition is still active.
3. Furthermore, zib Symptom might result in Conditions as well.

## zib2017
### Does the zib profile fit in the EU profile?
* The zib2017 profile has optional extensions not recognized by the European profiles, which might be required for the full interpretion of all the data.
* The constraints on `.clinicalStatus`, `.code`, `.onset[x]` and `abatement[x]` align.
* The European profile has a _required_ binding on `.severity`, which the zib profile hasn't. The default _preferred_ binding here fits within the European ValueSet. `.severity` itself if optional in both cases.
* The ValueSet bound on `Condition.category` has a different axis than the one in the European profile. It doesn't preclude the use of the European codes.
* There's a soft conflict for the ValueSets on `Condition.code`. The zib might use code systems nog present in the _preferred_ binding in the European profile.

Conclusion: a zib compliant instance will be valid European instance, but doesn't necessarily adhere to preferred terminology. 

### Does the EU profile fit in the zib profile?
* The European profile has optional extensions not recognized by the zib profile.
* The constraints on `.clinicalStatus`, `.code`, `.onset[x]` and `abatement[x]` align.
* There's a soft conflict on the ValueSets on `Condition.code`. The EU profile includes negation codes which are not present in the zib profile.
* The ValueSet bound on `Condition.category` has a different axis than the one in the zib profile. It doesn't preclude the use of the zib codes.

Conclusion: a EU compliant instance will be a valid zib instance, but doesn't necessarily adhere to the preferred terminology, especially regarding negations.

### Are there any conflicts?
* The zib doesn't specify the use of `Condition.severity`, but if it is populated for other reasons, a conflict may arise with the _required_ European ValueSet.

## zib2020
### Does the zib profile fit in the EU profile?
* According to the zib profile, `Condition.code` and `Condition.clinicalStatus` may be absent, whereas the EU profile requires these concepts.
* According to the zib profile, `.onset[x]` and `.abatement[x]` may be using a variety of data types, whereas the EU profile restricts them to just _dateTime_.
* The European profile has a _required_ binding on `.severity`, which the zib profile hasn't. The default _preferred_ binding here fits within the European ValueSet. `.severity` itself if optional in both cases.
* There's a soft conflict for the ValueSets on `Condition.code`. The zib might use code systems nog present in the _preferred_ binding in the European profile.

Conclusion: a zib compliant instance might miss data required by the EU profile and might use other data types. In addition, it might not adhere to the preferred terminology.

### Does the EU profile fit in the zib profile?
* The European profile has optional extensions not recognized by the zib profile.
* The European profile doesn't impose cardinality restrictions on `.note` and `.bodySite`, whereas the zib profile does.
* There's a soft conflict on the ValueSets on `Condition.code`. The EU profile includes negation codes which are not present in the zib profile.
* The ValueSet bound on `Condition.category` has a different axis than the one in the zib profile. It doesn't preclude the use of the zib codes.

Conclusion: a EU compliant instance will most likely be a valid zib instance, although conflicts could arise on the number of `.note`'s and `.bodySite`'s. It also doesn't necessarily adhere to the preferred terminology, especially regarding negations.

### Are there any conflicts?
* The zib doesn't specify the use of `Condition.severity`, but if it is populated for other reasons, a conflict may arise with the _required_ European ValueSet.

## zib2024
The profiles don't exist yet, but there's a large potential for conflictis.