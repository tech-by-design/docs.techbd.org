# File Evaluation Against Various Validators

### Validation Instructions
Validate the FHIR document using SHIN-NY IG Version 0.4.0 on the following platforms:
1. [Legacy Public Inferno Site](https://inferno.healthit.gov/validator/)
2. [Official Public Site](https://validator.fhir.org/)
3. Official Local Docker Site
4. [Custom 1115 FHIR Server](https://n9r2j0ii52.execute-api.ap-south-1.amazonaws.com/Prod/Bundle/$validate)
 

## Validation on Different Platforms

## Updates from SHIN-NY IG 0.3.0 to 0.4.0

- **New Constraints**:
  - `bundle.total` max value increased from 0 to 1.
  - `bundle.link` max value increased from 0 to *.
  - `bundle.entry.search` max value increased from 0 to 1.
  - `bundle.entry.request.method` changed from `POST|DELETE` to `POST`.
  - `bundle.entry.request.ifNoneMatch` max value increased from 0 to 1.
  - `bundle.entry.request.ifMatch` max value increased from 0 to 1.
  - `bundle.entry.request.ifNoneExist` max value increased from 0 to 1.
  - `bundle.entry.response.location` max value increased from 0 to 1.
  - `bundle.entry.response.etag` max value increased from 0 to 1.
  - `bundle.signature` max value increased from 0 to 1.
  - `bundle.entry.response.lastModified` max value increased from 0 to 1.
- 
### Updates from SHIN-NY IG Version 0.4.0 to SHIN-NY IG Version 0.5.0

- Added more bundle constraints.

### File Tested

- [TestCase301.json](TestCase301.json)


## Changes Identified in Error Logs Compared to Version 0.3.0


## Legacy Public Inferno Site

- **SHIN-NY IG Version 0.3.0**
  
 ```
 Missing `Bundle.timestamp.
 Bundle must include one `Patient` and one `Encounter`
 Ensure the presence of required resources: Bundle, Encounter, Patient, Organization, SDOHCC Observation Screening Response, and SDOHCC Consent.

```
- **SHIN-NY IG Version 0.5.0**
  

#### Issues Resolved
```
 Bundle: Constraint failed: SHINNY-Bundle-1: 'Every bundle should always have one and only one 'Patient' & 'Encounter'' (defined in http://shinny.org/StructureDefinition/SHINNYBundleProfile) on line 1. 

 ```
#### New Issues identified
```
Bundle: Constraint failed: SHINNY-Bundle-4: 'Ensure that the Encounter resource has a status code; Ensure that the Encounter resource has a status code' (defined in http://shinny.org/StructureDefinition/SHINNYBundleProfile) on line 1. 
Bundle: Constraint failed: SHINNY-Bundle-5: 'Ensure that the Encounter resource has a class code; Ensure that the Encounter resource has a class code system' (defined in http://shinny.org/StructureDefinition/SHINNYBundleProfile) on line 1. 
Bundle: Constraint failed: SHINNY-Bundle-text-existence: 'All ObservationScreeningResponse (questions & answers) must have a text field present.' (defined in http://shinny.org/StructureDefinition/SHINNYBundleProfile) on line 1. 
Bundle.type: A definition for CodeSystem 'http://hl7.org/fhir/ValueSet/bundle-type' could not be found, so the code cannot be validated on line 4. 

```
- **Resolution**
    - Add Encounter Class,status,subject, class code etc.  
    - Include the following resources in the FHIR document: Bundle, Encounter, Patient, Organization, SDOHCC Observation Screening Response, and SDOHCC Consent.

#### Official Public Validator

- No differences were noted between the error logs for SHIN-NY IG Versions 0.3.0 and 0.4.0.
- Date time related issues are solved in 0.5.0 compared to 0.4.0.

#### Official Local Docker Site

- No differences were noted between the error logs for SHIN-NY IG Versions 0.3.0 and 0.4.0.
- Date time related issues are solved in 0.5.0 compared to 0.4.0.

#### Custom 1115 FHIR Server

- No differences were noted between the error logs for SHIN-NY IG Versions 0.3.0 and 0.4.0.
- Date time related issues are solved in 0.5.0 compared to Version 0.4.0.
- Issues with `id-primitive` compared to IG Version 0.4.0. 

### Resolution

**Most issues are related to `id-primitive` and `dateTime-primitive` constraints.**

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

#### `dateTime-primitive`

- The `dateTime` primitive in FHIR follows a pattern derived from ISO 8601. It can represent:
    - **Full Date and Time**: `YYYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]`
    - **Date Only**: `YYYY-MM-DD`
    - **Year and Month**: `YYYY-MM`
    - **Year Only**: `YYYY`
- **Components**:
    - **YYYY**: Four-digit year
    - **MM**: Two-digit month (01-12)
    - **DD**: Two-digit day of the month (01-31)
    - **T**: Literal character 'T' used as a separator between the date and time parts
    - **hh**: Two-digit hour (00-23)
    - **mm**: Two-digit minute (00-59)
    - **ss**: Two-digit second (00-59)
    - **Z**: Indicates UTC (Coordinated Universal Time) if present
    - **(+|-)hh**: Time zone offset from UTC