<?xml version="1.0" encoding="UTF-8"?>
<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" queryBinding="xslt2">
  <sch:ns prefix="f" uri="http://hl7.org/fhir"/>
  <sch:ns prefix="h" uri="http://www.w3.org/1999/xhtml"/>
  <!-- 
    This file contains just the constraints for the profile Medication
    It includes the base constraints for the resource as well.
    Because of the way that schematrons and containment work, 
    you may need to use this schematron fragment to build a, 
    single schematron that validates contained resources (if you have any) 
  -->
  <sch:pattern>
    <sch:title>f:Medication</sch:title>
    <sch:rule context="f:Medication">
      <sch:assert test="count(f:extension[@url = 'http://profiles.ihe.net/PHARM/MPD/StructureDefinition/ihe-ext-medication-productname']) &lt;= 1">extension with URL = 'http://profiles.ihe.net/PHARM/MPD/StructureDefinition/ihe-ext-medication-productname': maximum cardinality of 'extension' is 1</sch:assert>
      <sch:assert test="count(f:extension[@url = 'http://profiles.ihe.net/PHARM/MPD/StructureDefinition/ihe-ext-medication-sizeofitem']) &lt;= 1">extension with URL = 'http://profiles.ihe.net/PHARM/MPD/StructureDefinition/ihe-ext-medication-sizeofitem': maximum cardinality of 'extension' is 1</sch:assert>
      <sch:assert test="count(f:extension[@url = 'http://profiles.ihe.net/PHARM/MPD/StructureDefinition/ihe-ext-medication-unitofpresentation']) &lt;= 1">extension with URL = 'http://profiles.ihe.net/PHARM/MPD/StructureDefinition/ihe-ext-medication-unitofpresentation': maximum cardinality of 'extension' is 1</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>f:Medication/f:ingredient/f:strength</sch:title>
    <sch:rule context="f:Medication/f:ingredient/f:strength">
      <sch:assert test="count(f:id) &lt;= 1">id: maximum cardinality of 'id' is 1</sch:assert>
      <sch:assert test="count(f:extension[@url = 'http://profiles.ihe.net/PHARM/MPD/StructureDefinition/ihe-ext-medication-strengthsubstance']) &lt;= 1">extension with URL = 'http://profiles.ihe.net/PHARM/MPD/StructureDefinition/ihe-ext-medication-strengthsubstance': maximum cardinality of 'extension' is 1</sch:assert>
      <sch:assert test="count(f:extension[@url = 'http://profiles.ihe.net/PHARM/MPD/StructureDefinition/ihe-ext-medication-strengthtype']) &lt;= 1">extension with URL = 'http://profiles.ihe.net/PHARM/MPD/StructureDefinition/ihe-ext-medication-strengthtype': maximum cardinality of 'extension' is 1</sch:assert>
      <sch:assert test="count(f:numerator) &lt;= 1">numerator: maximum cardinality of 'numerator' is 1</sch:assert>
      <sch:assert test="count(f:denominator) &lt;= 1">denominator: maximum cardinality of 'denominator' is 1</sch:assert>
    </sch:rule>
  </sch:pattern>
</sch:schema>
