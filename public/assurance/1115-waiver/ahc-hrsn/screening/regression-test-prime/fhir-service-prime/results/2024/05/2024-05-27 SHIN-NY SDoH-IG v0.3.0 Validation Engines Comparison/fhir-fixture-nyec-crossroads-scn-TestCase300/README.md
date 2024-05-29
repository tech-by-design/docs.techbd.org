## File Evaluation Against Various Validators

### Validation Instructions

Validate the FHIR document using SHIN-NY IG Version 0.4.0 on the following platforms:
1. [Legacy Public Inferno Site](https://inferno.healthit.gov/validator/)
2. [Official Public Site](https://validator.fhir.org/)
3. Official Local Docker Site
4. [Custom 1115 FHIR Server](https://n9r2j0ii52.execute-api.ap-south-1.amazonaws.com/Prod/Bundle/$validate)

### Updates from SHIN-NY IG Version 0.3.0 to SHIN-NY IG Version 0.4.0

- Added more bundle constraints.
- `bundle.total`: max value changed to 1 from 0.
- `bundle.link`: max value changed to * from 0.
- `bundle.entry.search`: max value changed to 1 from 0.
- `bundle.entry.request.method`: changed to `POST` from `POST | DELETE`.
- `bundle.entry.request.ifnonMatch`: max value changed to 1 from 0.
- `bundle.entry.request.ifMatch`: max value changed to 1 from 0.
- `bundle.entry.request.ifNoneExist`: max value changed to 1 from 0.
- `bundle.entry.response.location`: max value changed to 1 from 0.
- `bundle.entry.response.etag`: max value changed to 1 from 0.
- `bundle.signature`: max value changed to 1 from 0.
- `bundle.entry.response.lastModified`: max value changed to 1 from 0.

### File Tested

- [fhir-fixture-nyec-crossroads-scn-TestCase300.json](fhir-fixture-nyec-crossroads-scn-TestCase300.json)

### Changes Identified in Error Logs Compared to Version 0.3.0

#### Legacy Inferno Public Site

- **SHIN-NY IG Version 0.3.0**
    ```
    Bundle: Bundle.link: max allowed = 0, but found 1 (from http://shinny.org/StructureDefinition/SHINNYBundleProfile|0.3.0) on line 1.
    Bundle: Bundle.timestamp: minimum required = 1, but only found 0 (from http://shinny.org/StructureDefinition/SHINNYBundleProfile|0.3.0) on line 1.
    Bundle: Bundle.total: max allowed = 0, but found 1 (from http://shinny.org/StructureDefinition/SHINNYBundleProfile|0.3.0) on line 1.
    ```
- **SHIN-NY IG Version 0.4.0**
    ```
    Bundle: Bundle.timestamp: minimum required = 1, but only found 0 (from http://shinny.org/StructureDefinition/SHINNYBundleProfile|0.4.0) on line 1.
    Bundle: Constraint failed: SHINNY-Bundle-1: 'Every bundle should always have one and only one 'Patient' & 'Encounter'' (defined in http://shinny.org/StructureDefinition/SHINNYBundleProfile) on line 1.
    Bundle: Constraint failed: SHINNY-Bundle-2: 'Bundle contains the following resources at minimum: Bundle, Encounter, Patient, Organization, SDOHCC Observation Screening Response, SDOHCC Consent' (defined in http://shinny.org/StructureDefinition/SHINNYBundleProfile) on line 1.
    ```
- **Resolution**
    - Add `Bundle.timestamp` information in the FHIR document.
    - Ensure there is one `Patient` and one `Encounter` information in the FHIR document.
    - Include the following resources in the FHIR document: Bundle, Encounter, Patient, Organization, SDOHCC Observation Screening Response, and SDOHCC Consent.

#### Official Public Validator

- No differences were noted between the error logs for SHIN-NY IG Versions 0.3.0 and 0.4.0.

#### Official Local Docker Site

- No differences were noted between the error logs for SHIN-NY IG Versions 0.3.0 and 0.4.0.

#### Custom 1115 FHIR Server

- No differences were noted between the error logs for SHIN-NY IG Versions 0.3.0 and 0.4.0.

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
