## File Evaluation Against Various Validators

### Validation Instructions

Validate the FHIR document using SHIN-NY IG Version 0.9.1 on the following platforms:
1. [Legacy Public Inferno Site](https://inferno.healthit.gov/validator/)
2. [Official Public Site](https://validator.fhir.org/)
4. [HAPI FHIR Server Validation ](https://synthetic.fhir.api.devl.techbd.org/Bundle/$validate)


### Changes Identified in Error Logs Version 0.9.1


#### HAPI FHIR Server Validation

- No issues identified, please see the results [custom-115-fhir-server.md](custom-115-fhir-server.md)  

#### Inferno Validation Engine

- Inferno returs meta validation issues and referential integrity issues, please see the results [legacy-Inferno-public-site.md](legacy-Inferno-public-site.md)

#### Official Public Site

- Official validator not returning any referential integrity issues, please see the results  [official-public-site.md](official-public-site.md) 