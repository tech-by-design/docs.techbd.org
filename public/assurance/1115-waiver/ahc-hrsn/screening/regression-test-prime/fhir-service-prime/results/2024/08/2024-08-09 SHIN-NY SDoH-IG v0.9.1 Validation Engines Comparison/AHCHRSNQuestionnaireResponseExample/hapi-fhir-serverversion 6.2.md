# File evaluation against Hapi FHIR Server Version 6.2

## Files tested

- [AHCHRSNQuestionnaireResponseExample.json](AHCHRSNQuestionnaireResponseExample.json)

## NYeC expectations

```json
{
  "testcase": AHCHRSNQuestionnaireResponseExample,
  "csvoutputS3Bucket": "certification-engine-output",
  "testcasetype": "POSITIVE",
  "expectedResult": "AHCHRSNQuestionnaireResponseExample should succcessfully be processed by the QE and forwarded to NYeC.  The MPI for the patient should be added to the Patient resource."
}
```

## Results

```json

Validation failed with issues:
Severity: ERROR
Location: Bundle.type
Message : The value provided ('transaction') is not in the value set 'BundleType' (http://hl7.org/fhir/ValueSet/bundle-type|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[0].resource.ofType(Patient).text.status
Message : The value provided ('generated') is not in the value set 'NarrativeStatus' (http://hl7.org/fhir/ValueSet/narrative-status|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: INFORMATION
Location: Bundle.entry[0].resource.ofType(Patient).extension[0]
Message : Unknown extension http://hl7.org/fhir/us/core/StructureDefinition/us-core-race

Severity: INFORMATION
Location: Bundle.entry[0].resource.ofType(Patient).extension[1]
Message : Unknown extension http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity

Severity: INFORMATION
Location: Bundle.entry[0].resource.ofType(Patient).extension[2]
Message : Unknown extension http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex

Severity: WARNING
Location: Bundle.entry[0].resource.ofType(Patient).identifier[0].type
Message : None of the codings provided are in the value set 'IdentifierType' (http://hl7.org/fhir/ValueSet/identifier-type), and a coding should come from this value set unless it has no suitable code (note that the validator cannot judge what is suitable) (codes = http://terminology.hl7.org/CodeSystem/v2-0203#MR)

Severity: WARNING
Location: Bundle.entry[0].resource.ofType(Patient).identifier[1].type
Message : None of the codings provided are in the value set 'IdentifierType' (http://hl7.org/fhir/ValueSet/identifier-type), and a coding should come from this value set unless it has no suitable code (note that the validator cannot judge what is suitable) (codes = http://terminology.hl7.org/CodeSystem/v2-0203#MA)

Severity: WARNING
Location: Bundle.entry[0].resource.ofType(Patient).identifier[1].assigner
Message : Entry 4 matches the reference Organization/InsuranceExample by type and id but it's fullUrl http://shinny.org/InsuranceExample does not match the full target URL http://Organization/InsuranceExample by Bundle resolution rules

Severity: WARNING
Location: Bundle.entry[0].resource.ofType(Patient).identifier[2].type
Message : None of the codings provided are in the value set 'IdentifierType' (http://hl7.org/fhir/ValueSet/identifier-type), and a coding should come from this value set unless it has no suitable code (note that the validator cannot judge what is suitable) (codes = http://terminology.hl7.org/CodeSystem/v2-0203#SS)

Severity: ERROR
Location: Bundle.entry[0].resource.ofType(Patient).telecom[0].system
Message : The value provided ('phone') is not in the value set 'ContactPointSystem' (http://hl7.org/fhir/ValueSet/contact-point-system|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[0].resource.ofType(Patient).telecom[0].use
Message : The value provided ('home') is not in the value set 'ContactPointUse' (http://hl7.org/fhir/ValueSet/contact-point-use|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[0].resource.ofType(Patient).gender
Message : The value provided ('male') is not in the value set 'AdministrativeGender' (http://hl7.org/fhir/ValueSet/administrative-gender|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[0].resource.ofType(Patient).meta.profile[0]
Message : Profile reference 'http://shinny.org/StructureDefinition/shinny-patient' has not been checked because it is unknown

Severity: ERROR
Location: Bundle.entry[0].request.method
Message : The value provided ('POST') is not in the value set 'HTTPVerb' (http://hl7.org/fhir/ValueSet/http-verb|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[1].resource.ofType(Encounter).text.status
Message : The value provided ('generated') is not in the value set 'NarrativeStatus' (http://hl7.org/fhir/ValueSet/narrative-status|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[1].resource.ofType(Encounter).status
Message : The value provided ('finished') is not in the value set 'EncounterStatus' (http://hl7.org/fhir/ValueSet/encounter-status|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: WARNING
Location: Bundle.entry[1].resource.ofType(Encounter).class
Message : The Coding provided (http://terminology.hl7.org/CodeSystem/v3-ActCode#FLD) is not in the value set http://terminology.hl7.org/ValueSet/v3-ActEncounterCode, and a code should come from this value set unless it has no suitable code (note that the validator cannot judge what is suitable).  (error message = Validation failed)

Severity: WARNING
Location: Bundle.entry[1].resource.ofType(Encounter).subject
Message : Entry 0 matches the reference Patient/PatientExample by type and id but it's fullUrl http://shinny.org/PatientExample does not match the full target URL http://Patient/PatientExample by Bundle resolution rules

Severity: ERROR
Location: Bundle.entry[1].resource.ofType(Encounter).meta.profile[0]
Message : Profile reference 'http://shinny.org/StructureDefinition/shinny-encounter' has not been checked because it is unknown

Severity: ERROR
Location: Bundle.entry[1].resource.ofType(Encounter).meta.profile[1]
Message : Profile reference 'http://shinny.org/StructureDefinition/shin-ny-encounter' has not been checked because it is unknown

Severity: ERROR
Location: Bundle.entry[1].request.method
Message : The value provided ('POST') is not in the value set 'HTTPVerb' (http://hl7.org/fhir/ValueSet/http-verb|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[2].resource.ofType(Consent).text.status
Message : The value provided ('generated') is not in the value set 'NarrativeStatus' (http://hl7.org/fhir/ValueSet/narrative-status|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[2].resource.ofType(Consent).status
Message : The value provided ('active') is not in the value set 'ConsentState' (http://hl7.org/fhir/ValueSet/consent-state-codes|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: WARNING
Location: Bundle.entry[2].resource.ofType(Consent).scope
Message : None of the codings provided are in the value set 'Consent Scope Codes' (http://hl7.org/fhir/ValueSet/consent-scope), and a coding should come from this value set unless it has no suitable code (note that the validator cannot judge what is suitable) (codes = null#treatment)

Severity: WARNING
Location: Bundle.entry[2].resource.ofType(Consent).scope.coding[0]
Message : A code with no system has no defined meaning. A system should be provided

Severity: WARNING
Location: Bundle.entry[2].resource.ofType(Consent).category[0]
Message : None of the codings provided are in the value set 'Consent Category Codes' (http://hl7.org/fhir/ValueSet/consent-category), and a coding should come from this value set unless it has no suitable code (note that the validator cannot judge what is suitable) (codes = null#59284-0)

Severity: WARNING
Location: Bundle.entry[2].resource.ofType(Consent).category[0].coding[0]
Message : A code with no system has no defined meaning. A system should be provided

Severity: WARNING
Location: Bundle.entry[2].resource.ofType(Consent).patient
Message : Entry 0 matches the reference Patient/PatientExample by type and id but it's fullUrl http://shinny.org/PatientExample does not match the full target URL http://Patient/PatientExample by Bundle resolution rules

Severity: ERROR
Location: Bundle.entry[2].resource.ofType(Consent).provision.type
Message : The value provided ('permit') is not in the value set 'ConsentProvisionType' (http://hl7.org/fhir/ValueSet/consent-provision-type|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[2].resource.ofType(Consent).meta.profile[0]
Message : Profile reference 'http://shinny.org/StructureDefinition/shinny-Consent' has not been checked because it is unknown

Severity: ERROR
Location: Bundle.entry[2].resource.ofType(Consent).meta.profile[1]
Message : Profile reference 'http://shinny.org/StructureDefinition/shinny-consent' has not been checked because it is unknown

Severity: ERROR
Location: Bundle.entry[2].request.method
Message : The value provided ('POST') is not in the value set 'HTTPVerb' (http://hl7.org/fhir/ValueSet/http-verb|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[3].resource.ofType(Organization).text.status
Message : The value provided ('generated') is not in the value set 'NarrativeStatus' (http://hl7.org/fhir/ValueSet/narrative-status|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: WARNING
Location: Bundle.entry[3].resource.ofType(Organization).identifier[0].type
Message : None of the codings provided are in the value set 'IdentifierType' (http://hl7.org/fhir/ValueSet/identifier-type), and a coding should come from this value set unless it has no suitable code (note that the validator cannot judge what is suitable) (codes = null#null)

Severity: ERROR
Location: Bundle.entry[3].resource.ofType(Organization).meta.profile[0]
Message : Profile reference 'http://shinny.org/StructureDefinition/shin-ny-organization' has not been checked because it is unknown

Severity: ERROR
Location: Bundle.entry[3].request.method
Message : The value provided ('POST') is not in the value set 'HTTPVerb' (http://hl7.org/fhir/ValueSet/http-verb|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[4].resource.ofType(Organization).text.status
Message : The value provided ('generated') is not in the value set 'NarrativeStatus' (http://hl7.org/fhir/ValueSet/narrative-status|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: WARNING
Location: Bundle.entry[4].resource.ofType(Organization).identifier[0].type
Message : None of the codings provided are in the value set 'IdentifierType' (http://hl7.org/fhir/ValueSet/identifier-type), and a coding should come from this value set unless it has no suitable code (note that the validator cannot judge what is suitable) (codes = null#null)

Severity: ERROR
Location: Bundle.entry[4].resource.ofType(Organization).meta.profile[0]
Message : Profile reference 'http://shinny.org/StructureDefinition/shin-ny-organization' has not been checked because it is unknown

Severity: ERROR
Location: Bundle.entry[4].request.method
Message : The value provided ('POST') is not in the value set 'HTTPVerb' (http://hl7.org/fhir/ValueSet/http-verb|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[5].resource.ofType(Observation).text.status
Message : The value provided ('generated') is not in the value set 'NarrativeStatus' (http://hl7.org/fhir/ValueSet/narrative-status|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[5].resource.ofType(Observation).status
Message : The value provided ('final') is not in the value set 'ObservationStatus' (http://hl7.org/fhir/ValueSet/observation-status|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[5].resource.ofType(Observation).category[0].coding[0]
Message : Unknown Code System 'http://hl7.org/fhir/us/sdoh-clinicalcare/CodeSystem/SDOHCC-CodeSystemTemporaryCodes'

Severity: ERROR
Location: Bundle.entry[5].resource.ofType(Observation).category[0].coding[1]
Message : Unknown Code System 'http://hl7.org/fhir/us/sdoh-clinicalcare/CodeSystem/SDOHCC-CodeSystemTemporaryCodes'

Severity: ERROR
Location: Bundle.entry[5].resource.ofType(Observation).category[0].coding[2]
Message : Unknown Code System 'http://hl7.org/fhir/us/sdoh-clinicalcare/CodeSystem/SDOHCC-CodeSystemTemporaryCodes'

Severity: WARNING
Location: Bundle.entry[5].resource.ofType(Observation).subject
Message : Entry 0 matches the reference Patient/PatientExample by type and id but it's fullUrl http://shinny.org/PatientExample does not match the full target URL http://Patient/PatientExample by Bundle resolution rules

Severity: WARNING
Location: Bundle.entry[5].resource.ofType(Observation).encounter
Message : Entry 1 matches the reference Encounter/EncounterExample by type and id but it's fullUrl http://shinny.org/EncounterExample does not match the full target URL http://Encounter/EncounterExample by Bundle resolution rules

Severity: WARNING
Location: Bundle.entry[5].resource.ofType(Observation).interpretation[0]
Message : None of the codings provided are in the value set 'Observation Interpretation Codes' (http://hl7.org/fhir/ValueSet/observation-interpretation), and a coding should come from this value set unless it has no suitable code (note that the validator cannot judge what is suitable) (codes = http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation#POS)

Severity: WARNING
Location: Bundle.entry[5].resource.ofType(Observation).hasMember[0]
Message : Entry 6 matches the reference Observation/ObservationResponseHousingInstability71802-3 by type and id but it's fullUrl http://shinny.org/ObservationResponseHousingInstability71802-3 does not match the full target URL http://Observation/ObservationResponseHousingInstability71802-3 by Bundle resolution rules

Severity: WARNING
Location: Bundle.entry[5].resource.ofType(Observation).hasMember[1]
Message : Entry 7 matches the reference Observation/ObservationResponseInadequateHousing96778-6 by type and id but it's fullUrl http://shinny.org/ObservationResponseInadequateHousing96778-6 does not match the full target URL http://Observation/ObservationResponseInadequateHousing96778-6 by Bundle resolution rules

Severity: WARNING
Location: Bundle.entry[5].resource.ofType(Observation).derivedFrom[0]
Message : Entry 11 matches the reference QuestionnaireResponse/QuestionnaireResponse-123 by type and id but it's fullUrl http://shinny.org/QuestionnaireResponse-123 does not match the full target URL http://QuestionnaireResponse/QuestionnaireResponse-123 by Bundle resolution rules

Severity: WARNING
Location: Bundle.entry[5].resource.ofType(Observation).derivedFrom[0].type
Message : The value provided ('QuestionnaireResponse') is not in the value set 'ResourceType' (http://hl7.org/fhir/ValueSet/resource-types), and a code should come from this value set unless it has no suitable code (note that the validator cannot judge what is suitable)  (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[5].resource.ofType(Observation).meta.profile[0]
Message : Profile reference 'http://shinny.org/StructureDefinition/shin-ny-observation-screening-response' has not been checked because it is unknown

Severity: ERROR
Location: Bundle.entry[5].resource.ofType(Observation).meta.profile[1]
Message : Profile reference 'http://hl7.org/fhir/us/sdoh-clinicalcare/StructureDefinition/SDOHCC-ObservationScreeningResponse' has not been checked because it is unknown

Severity: ERROR
Location: Bundle.entry[5].request.method
Message : The value provided ('POST') is not in the value set 'HTTPVerb' (http://hl7.org/fhir/ValueSet/http-verb|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[6].resource.ofType(Observation).text.status
Message : The value provided ('generated') is not in the value set 'NarrativeStatus' (http://hl7.org/fhir/ValueSet/narrative-status|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[6].resource.ofType(Observation).status
Message : The value provided ('final') is not in the value set 'ObservationStatus' (http://hl7.org/fhir/ValueSet/observation-status|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[6].resource.ofType(Observation).category[0].coding[0]
Message : Unknown Code System 'http://hl7.org/fhir/us/sdoh-clinicalcare/CodeSystem/SDOHCC-CodeSystemTemporaryCodes'

Severity: WARNING
Location: Bundle.entry[6].resource.ofType(Observation).subject
Message : Entry 0 matches the reference Patient/PatientExample by type and id but it's fullUrl http://shinny.org/PatientExample does not match the full target URL http://Patient/PatientExample by Bundle resolution rules

Severity: ERROR
Location: Bundle.entry[6].resource.ofType(Observation).meta.profile[0]
Message : Profile reference 'http://shinny.org/StructureDefinition/shin-ny-observation-screening-response' has not been checked because it is unknown

Severity: ERROR
Location: Bundle.entry[6].resource.ofType(Observation).meta.profile[1]
Message : Profile reference 'http://hl7.org/fhir/us/sdoh-clinicalcare/StructureDefinition/SDOHCC-ObservationScreeningResponse' has not been checked because it is unknown

Severity: ERROR
Location: Bundle.entry[6].request.method
Message : The value provided ('POST') is not in the value set 'HTTPVerb' (http://hl7.org/fhir/ValueSet/http-verb|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[7].resource.ofType(Observation).text.status
Message : The value provided ('generated') is not in the value set 'NarrativeStatus' (http://hl7.org/fhir/ValueSet/narrative-status|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[7].resource.ofType(Observation).status
Message : The value provided ('final') is not in the value set 'ObservationStatus' (http://hl7.org/fhir/ValueSet/observation-status|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[7].resource.ofType(Observation).category[0].coding[0]
Message : Unknown Code System 'http://hl7.org/fhir/us/sdoh-clinicalcare/CodeSystem/SDOHCC-CodeSystemTemporaryCodes'

Severity: WARNING
Location: Bundle.entry[7].resource.ofType(Observation).subject
Message : Entry 0 matches the reference Patient/PatientExample by type and id but it's fullUrl http://shinny.org/PatientExample does not match the full target URL http://Patient/PatientExample by Bundle resolution rules

Severity: WARNING
Location: Bundle.entry[7].resource.ofType(Observation).interpretation[0]
Message : None of the codings provided are in the value set 'Observation Interpretation Codes' (http://hl7.org/fhir/ValueSet/observation-interpretation), and a coding should come from this value set unless it has no suitable code (note that the validator cannot judge what is suitable) (codes = http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation#POS)

Severity: ERROR
Location: Bundle.entry[7].resource.ofType(Observation).meta.profile[0]
Message : Profile reference 'http://shinny.org/StructureDefinition/shin-ny-observation-screening-response' has not been checked because it is unknown

Severity: ERROR
Location: Bundle.entry[7].resource.ofType(Observation).meta.profile[1]
Message : Profile reference 'http://hl7.org/fhir/us/sdoh-clinicalcare/StructureDefinition/SDOHCC-ObservationScreeningResponse' has not been checked because it is unknown

Severity: ERROR
Location: Bundle.entry[7].request.method
Message : The value provided ('POST') is not in the value set 'HTTPVerb' (http://hl7.org/fhir/ValueSet/http-verb|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[8].resource.ofType(Observation).text.status
Message : The value provided ('generated') is not in the value set 'NarrativeStatus' (http://hl7.org/fhir/ValueSet/narrative-status|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[8].resource.ofType(Observation).status
Message : The value provided ('final') is not in the value set 'ObservationStatus' (http://hl7.org/fhir/ValueSet/observation-status|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[8].resource.ofType(Observation).category[0].coding[0]
Message : Unknown Code System 'http://hl7.org/fhir/us/sdoh-clinicalcare/CodeSystem/SDOHCC-CodeSystemTemporaryCodes'

Severity: ERROR
Location: Bundle.entry[8].resource.ofType(Observation).category[0].coding[1]
Message : Unknown Code System 'http://hl7.org/fhir/us/sdoh-clinicalcare/CodeSystem/SDOHCC-CodeSystemTemporaryCodes'

Severity: WARNING
Location: Bundle.entry[8].resource.ofType(Observation).subject
Message : Entry 0 matches the reference Patient/PatientExample by type and id but it's fullUrl http://shinny.org/PatientExample does not match the full target URL http://Patient/PatientExample by Bundle resolution rules

Severity: WARNING
Location: Bundle.entry[8].resource.ofType(Observation).encounter
Message : Entry 1 matches the reference Encounter/EncounterExample by type and id but it's fullUrl http://shinny.org/EncounterExample does not match the full target URL http://Encounter/EncounterExample by Bundle resolution rules

Severity: WARNING
Location: Bundle.entry[8].resource.ofType(Observation).interpretation[0]
Message : None of the codings provided are in the value set 'Observation Interpretation Codes' (http://hl7.org/fhir/ValueSet/observation-interpretation), and a coding should come from this value set unless it has no suitable code (note that the validator cannot judge what is suitable) (codes = http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation#POS)

Severity: WARNING
Location: Bundle.entry[8].resource.ofType(Observation).hasMember[0]
Message : Entry 9 matches the reference Observation/ObservationResponseFinancialInsecurity76513-1 by type and id but it's fullUrl http://shinny.org/ObservationResponseFinancialInsecurity76513-1 does not match the full target URL http://Observation/ObservationResponseFinancialInsecurity76513-1 by Bundle resolution rules

Severity: WARNING
Location: Bundle.entry[8].resource.ofType(Observation).hasMember[1]
Message : Entry 10 matches the reference Observation/ObservationResponseEmploymentStatus96780-2 by type and id but it's fullUrl http://shinny.org/ObservationResponseEmploymentStatus96780-2 does not match the full target URL http://Observation/ObservationResponseEmploymentStatus96780-2 by Bundle resolution rules

Severity: WARNING
Location: Bundle.entry[8].resource.ofType(Observation).derivedFrom[0]
Message : Entry 11 matches the reference QuestionnaireResponse/QuestionnaireResponse-123 by type and id but it's fullUrl http://shinny.org/QuestionnaireResponse-123 does not match the full target URL http://QuestionnaireResponse/QuestionnaireResponse-123 by Bundle resolution rules

Severity: WARNING
Location: Bundle.entry[8].resource.ofType(Observation).derivedFrom[0].type
Message : The value provided ('QuestionnaireResponse') is not in the value set 'ResourceType' (http://hl7.org/fhir/ValueSet/resource-types), and a code should come from this value set unless it has no suitable code (note that the validator cannot judge what is suitable)  (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[8].resource.ofType(Observation).meta.profile[0]
Message : Profile reference 'http://shinny.org/StructureDefinition/shin-ny-observation-screening-response' has not been checked because it is unknown

Severity: ERROR
Location: Bundle.entry[8].resource.ofType(Observation).meta.profile[1]
Message : Profile reference 'http://hl7.org/fhir/us/sdoh-clinicalcare/StructureDefinition/SDOHCC-ObservationScreeningResponse' has not been checked because it is unknown

Severity: ERROR
Location: Bundle.entry[8].request.method
Message : The value provided ('POST') is not in the value set 'HTTPVerb' (http://hl7.org/fhir/ValueSet/http-verb|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[9].resource.ofType(Observation).text.status
Message : The value provided ('generated') is not in the value set 'NarrativeStatus' (http://hl7.org/fhir/ValueSet/narrative-status|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[9].resource.ofType(Observation).status
Message : The value provided ('final') is not in the value set 'ObservationStatus' (http://hl7.org/fhir/ValueSet/observation-status|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[9].resource.ofType(Observation).category[0].coding[0]
Message : Unknown Code System 'http://hl7.org/fhir/us/sdoh-clinicalcare/CodeSystem/SDOHCC-CodeSystemTemporaryCodes'

Severity: WARNING
Location: Bundle.entry[9].resource.ofType(Observation).subject
Message : Entry 0 matches the reference Patient/PatientExample by type and id but it's fullUrl http://shinny.org/PatientExample does not match the full target URL http://Patient/PatientExample by Bundle resolution rules

Severity: WARNING
Location: Bundle.entry[9].resource.ofType(Observation).interpretation[0]
Message : None of the codings provided are in the value set 'Observation Interpretation Codes' (http://hl7.org/fhir/ValueSet/observation-interpretation), and a coding should come from this value set unless it has no suitable code (note that the validator cannot judge what is suitable) (codes = http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation#POS)

Severity: ERROR
Location: Bundle.entry[9].resource.ofType(Observation).meta.profile[0]
Message : Profile reference 'http://shinny.org/StructureDefinition/shin-ny-observation-screening-response' has not been checked because it is unknown

Severity: ERROR
Location: Bundle.entry[9].resource.ofType(Observation).meta.profile[1]
Message : Profile reference 'http://hl7.org/fhir/us/sdoh-clinicalcare/StructureDefinition/SDOHCC-ObservationScreeningResponse' has not been checked because it is unknown

Severity: ERROR
Location: Bundle.entry[9].request.method
Message : The value provided ('POST') is not in the value set 'HTTPVerb' (http://hl7.org/fhir/ValueSet/http-verb|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[10].resource.ofType(Observation).text.status
Message : The value provided ('generated') is not in the value set 'NarrativeStatus' (http://hl7.org/fhir/ValueSet/narrative-status|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[10].resource.ofType(Observation).status
Message : The value provided ('final') is not in the value set 'ObservationStatus' (http://hl7.org/fhir/ValueSet/observation-status|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[10].resource.ofType(Observation).category[0].coding[0]
Message : Unknown Code System 'http://hl7.org/fhir/us/sdoh-clinicalcare/CodeSystem/SDOHCC-CodeSystemTemporaryCodes'

Severity: WARNING
Location: Bundle.entry[10].resource.ofType(Observation).subject
Message : Entry 0 matches the reference Patient/PatientExample by type and id but it's fullUrl http://shinny.org/PatientExample does not match the full target URL http://Patient/PatientExample by Bundle resolution rules

Severity: WARNING
Location: Bundle.entry[10].resource.ofType(Observation).interpretation[0]
Message : None of the codings provided are in the value set 'Observation Interpretation Codes' (http://hl7.org/fhir/ValueSet/observation-interpretation), and a coding should come from this value set unless it has no suitable code (note that the validator cannot judge what is suitable) (codes = http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation#POS)

Severity: ERROR
Location: Bundle.entry[10].resource.ofType(Observation).meta.profile[0]
Message : Profile reference 'http://shinny.org/StructureDefinition/shin-ny-observation-screening-response' has not been checked because it is unknown

Severity: ERROR
Location: Bundle.entry[10].resource.ofType(Observation).meta.profile[1]
Message : Profile reference 'http://hl7.org/fhir/us/sdoh-clinicalcare/StructureDefinition/SDOHCC-ObservationScreeningResponse' has not been checked because it is unknown

Severity: ERROR
Location: Bundle.entry[10].request.method
Message : The value provided ('POST') is not in the value set 'HTTPVerb' (http://hl7.org/fhir/ValueSet/http-verb|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[11].resource.ofType(QuestionnaireResponse).text.status
Message : The value provided ('generated') is not in the value set 'NarrativeStatus' (http://hl7.org/fhir/ValueSet/narrative-status|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.entry[11].resource.ofType(QuestionnaireResponse).status
Message : The value provided ('completed') is not in the value set 'QuestionnaireResponseStatus' (http://hl7.org/fhir/ValueSet/questionnaire-answers-status|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: WARNING
Location: Bundle.entry[11].resource.ofType(QuestionnaireResponse).subject
Message : Entry 0 matches the reference Patient/PatientExample by type and id but it's fullUrl http://shinny.org/PatientExample does not match the full target URL http://Patient/PatientExample by Bundle resolution rules

Severity: WARNING
Location: Bundle.entry[11].resource.ofType(QuestionnaireResponse).encounter
Message : Entry 1 matches the reference Encounter/EncounterExample by type and id but it's fullUrl http://shinny.org/EncounterExample does not match the full target URL http://Encounter/EncounterExample by Bundle resolution rules

Severity: WARNING
Location: Bundle.entry[11].resource.ofType(QuestionnaireResponse)
Message : The questionnaire 'http://shinny.org/fhir/Questionnaire/hrsn-questionnaire' could not be resolved, so no validation can be performed against the base questionnaire

Severity: ERROR
Location: Bundle.entry[11].resource.ofType(QuestionnaireResponse).meta.profile[0]
Message : Profile reference 'http://shinny.org/StructureDefinition/shinny-questionnaire-response' has not been checked because it is unknown

Severity: ERROR
Location: Bundle.entry[11].request.method
Message : The value provided ('POST') is not in the value set 'HTTPVerb' (http://hl7.org/fhir/ValueSet/http-verb|4.0.1), and a code is required from this value set) (error message = Validation failed)

Severity: ERROR
Location: Bundle.meta.profile[0]
Message : Profile reference 'http://shinny.org/StructureDefinition/SHINNYBundleProfile' has not been checked because it is unknown

```