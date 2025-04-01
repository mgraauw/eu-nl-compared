# Condition resources
## zib-Problem (2017) <-> Condition-uv-ips

x Condition-eu-eps (eps) does not seem to fit in zib-Problem (zib2017)
* x Condition.clinicalStatus: required in zib-Problem but optional in Condition-eu-eps.
* . Condition.category: The IPS codes are a refinement of the FHIR base codes, and the ValueSets are on different axes. They can co-exists without interfering.
* ~ Condition.code: The binding of the EPS ValueSet less restrictive than the zib, but the zib includes all of SNOMED plus several other concepts. In theory, an EPS compliant instance might use a code system not recognized by the zib that overlaps with a code from the extensible bound zib ValueSet, so strictly speaking such an instance is incompatible.
* x Condition.code: extensible ValueSet in zib-Problem is more restrictive than preferred binding in Condition-eu-eps.
* ~ Condition.bodySite: The EPS ValueSet is bound preferrable and includes all of SNOMED, while the zib ValueSet expects (extensible binding) only codes from a branch of SNOMED.
* x Condition.bodySite: extensible ValueSet in zib-Problem is more restrictive than preferred binding in Condition-eu-eps.
