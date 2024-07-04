# File Evaluation Against Various Validators

### Validation Instructions
Validate the FHIR document using SHIN-NY IG Version 0.4.0 on the following platforms:
1. [Legacy Public Inferno Site](https://inferno.healthit.gov/validator/)
2. [Official Public Site](https://validator.fhir.org/)
3. Official Local Docker Site
4. [Custom 1115 FHIR Server](https://n9r2j0ii52.execute-api.ap-south-1.amazonaws.com/Prod/Bundle/$validate)
 

## Validation on Different Platforms

### Updates from SHIN-NY IG Version 0.6.0 to SHIN-NY IG Version 0.7.0

- Added more bundle constraints.
- Bundle.meta
- Bundle.type
- Bundle.timestamp
- Bundle.entry
- Bundle.entry.request
- Bundle.entry.request.method
- 
### Changes Identified in Error Logs Compared to Version 0.7.0


#### Custom 1115 FHIR Server

- Issues with `id-primitive` compared to IG Version 0.6.0. 
### File Tested

- [TestCase302.json](TestCase302.json)


#### Custom 1115 FHIR Server

- No differences were noted between the error logs for SHIN-NY IG Versions 0.3.0 and 0.4.0.
- Date time related issues are solved in 0.5.0 compared to Version 0.4.0.
- Issues with `id-primitive` compared to IG Version 0.4.0. 

### Resolution

**Most issues are related to `id-primitive` 

#### `id-primitive`

- The `id` primitive in FHIR must adhere to specific constraints to ensure uniqueness and consistency:
    - **Type**: String
    - **Length**: 1 to 64 characters
    - **Allowed Characters**:
        - Lowercase alphabetic characters (a-z)
        - Numeric characters (0-9)
        - Hyphen (-)
        - Dot (.)
        - Underscore (_)
    - **Regular Expression Pattern**: `^[A-Za-z0-9\-\.]{1,64}$`