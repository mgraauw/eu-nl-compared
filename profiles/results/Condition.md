# Condition resources
## zib-Problem (2017) <-> Condition-uv-ips
x zib-Problem (zib2017) does not seem to fit in Condition-eu-eps (eps)
* + Condition.category: The IPS codes are a refinement of the FHIR base codes, and the ValueSets are on different axes. They can co-exists without interfering.
* x Condition.severity: required Valueset in Condition-eu-eps is more restrictive than zib-Problem.
* + Condition.code: The zib defines more code systems while the EPS only defines SNOMED to be used. However, the EPS binding is only preferred, so it should handle other code systems without problem. In addition, the EPS ValueSet is more specific than the zib when it is about SNOMED, but for all intents and purposes they are probably compatible.

x Condition-eu-eps (eps) does not seem to fit in zib-Problem (zib2017)
* x Condition.clinicalStatus: required in zib-Problem but optional in Condition-eu-eps.
* + Condition.category: The IPS codes are a refinement of the FHIR base codes, and the ValueSets are on different axes. They can co-exists without interfering.
* + Condition.code: The binding of the EPS ValueSet is only preferred, while the zib has an extensible binding. An EPS compliant instance thus might use a code not in the zib ValueSet but overlapping with a code in the ValueSet, breaking the definition of extensible. However, the zib ValueSet includes all of SNOMED plus several other entire code systems, so this is highly hypothetical.
* ~ Condition.bodySite: The zib expects (extensible binding) only codes from a branch of SNOMED, while the EPS allows for a wider use of SNOMED-codes and other code systems.


## zib-Problem (2020) <-> Condition-uv-ips
x zib-Problem (zib2020) does not seem to fit in Condition-eu-eps (eps)
* ~ The EPS profile is used only for (past or current) 'problems', while the zib has a broader aim (problems, complaints, diagnoses, findings, complications). This restriction isn't enforced though.
* ~ Condition.category: Due to bindings strengths and slicing there's no actual conflict. However, the EPS profile aims for only Conditions categorized as 'problems' while the zib aims for broader use. In addition, the zib (profile) aims for categories coded in SNOMED while the EPS profile aims for HL7 or LOINC.
* x Condition.severity: required Valueset in Condition-eu-eps is more restrictive than zib-Problem.
* x Condition.code: required in Condition-eu-eps but optional in zib-Problem.
* + Condition.code: The zib has a required binding, but the EPS only has a preferred binding, so a zib instance is compatible. The zib focuses on SNOMED and ICD-10, while the EPS only includes SNOMED.
* x Condition.onset[x]: Condition-eu-eps restricts types to {'dateTime'}, which is narrower than the allowed types in zib-Problem.
* x Condition.abatement[x]: Condition-eu-eps restricts types to {'dateTime'}, which is narrower than the allowed types in zib-Problem.

x Condition-eu-eps (eps) does not seem to fit in zib-Problem (zib2020)
* ~ Condition.category: Due to bindings strengths and slicing there's no actual conflict. However, the EPS profile aims for only Conditions categorized as 'problems' while the zib aims for broader use. In addition, the zib (profile) aims for categories coded in SNOMED while the EPS profile aims for HL7 or LOINC.
* x Condition.code: required Valueset in zib-Problem is more restrictive than Condition-eu-eps.
* x Condition.bodySite: restricted to 1 in zib-Problem but unrestricted in Condition-eu-eps.
* x Condition.bodySite: required Valueset in zib-Problem is more restrictive than Condition-eu-eps.
* x Condition.note: restricted to 1 in zib-Problem but unrestricted in Condition-eu-eps.
