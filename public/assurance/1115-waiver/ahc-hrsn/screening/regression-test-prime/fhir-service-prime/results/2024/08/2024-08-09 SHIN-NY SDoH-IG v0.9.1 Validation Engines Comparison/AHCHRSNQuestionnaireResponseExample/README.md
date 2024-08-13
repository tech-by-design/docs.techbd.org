## File Evaluation Against Various Validators

### Validation Instructions

Validate the FHIR document using SHIN-NY IG Version 0.9.1 on the following platforms:
1. [Legacy Public Inferno Site](https://inferno.healthit.gov/validator/)
2. [Official Public Site](https://validator.fhir.org/)
4. [HAPI FHIR Server Validation ](https://synthetic.fhir.api.devl.techbd.org/Bundle/$validate)


### Changes Identified in Error Logs Version 0.9.1


#### HAPI FHIR Server version 7.2 Validation 

- No issues identified, please see the results [hapi-fhir-server-version-7-2.md](hapi-fhir-server-version-7-2.md) 

#### HAPI FHIR Server version 6.2 Validation

- We are getting more validation issues using HAPI version 6.2.0 while comparing with HAPI version 7.2.0. please see the results [hapi-fhir-server-version-6-2.md](hapi-fhir-server-version-6-2.md) 


#### Inferno Validation Engine

- Inferno returs meta validation issues and referential integrity issues, please see the results [legacy-Inferno-public-site.md](legacy-Inferno-public-site.md)

#### Official Public Site

- Official validator not returning any referential integrity issues, please see the results  [official-public-site.md](official-public-site.md) 

#### Observations

There are some variations in the errors reported by different validators. 

One common issue we have seen across validators is that the Profile reference is not identified (since it’s not published yet, it is unknown to the validator). 

Basically, this means that, without being published, many IG validations referencing unreachable URIs might be problematic.

For example, the following error is reported:

Location: Bundle.meta.profile[0]
Message : Profile reference 'http://shinny.org/StructureDefinition/SHINNYBundleProfile' has not been checked because it is unknown.

When we run the RI between Patient & Assigning Org, in test file those tests we found the following results:

Inferno API Validation Results:
•	Bundle: Constraint failed: SHINNY-Bundle-Encounter-Location-RI: 'Checks for RI between Encounter & Location' (defined in http://shinny.org/StructureDefinition/SHINNYBundleProfile) on line 1. 
•	Bundle: Constraint failed: SHINNY-Bundle-Patient-Org-RI: 'Checks for RI between Patient & Assigning Org' (defined in http://shinny.org/StructureDefinition/SHINNYBundleProfile) on line 1. 
•	Bundle.meta: Unknown profile http://shinny.org/StructureDefinition/SHINNYMeta on line 4. 

HAPI version 7.2.0 reported no issues detected during validation even through there were supposed to be errors. This means either we’re not calling the functions properly or the HAPI validator doesn’t understand the IG. 

But in HAPI version 6.2.0 we are getting more errors compared to the HAPI version 7.2.0.

HL7 Official API Validation Results:
•	ERROR: Bundle.entry[0].resource/*Patient/PatientExample*/.extension[0]: The extension http://hl7.org/fhir/us/core/StructureDefinition/us-core-race could not be found so is not allowed here".