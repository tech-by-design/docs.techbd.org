## File Evaluation Against Various Validators

### Validation Instructions

Validate the FHIR document using SHIN-NY IG Version 0.9.1 on the following platforms:
1. [Legacy Public Inferno Site](https://inferno.healthit.gov/validator/)
2. [Official Public Site](https://validator.fhir.org/)
4. [TechBD Validation API](https://synthetic.fhir.api.devl.techbd.org/Bundle/$validate)


### Changes Identified in Error Logs Version 0.9.1


#### TechBD Validation API

- No issues identified, please refer [custom-115-fhir-server.md](custom-115-fhir-server.md)  

#### Inferno Validation Engine

- Inferno returs meta validation issues and referential integrity issues, please refer [legacy-Inferno-public-site.md](legacy-Inferno-public-site.md)

#### Official Public Site

- Official validator not returniong any referential integrity issues,please refer  [official-public-site.md](official-public-site.md) 