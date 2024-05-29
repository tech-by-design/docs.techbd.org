# File Evaluation Against Various Validators

## Validation on Different Platforms

### Legacy Public Inferno Site
- **URL**: [Inferno Validator](https://inferno.healthit.gov/validator/)
- **Issues Identified (SHIN-NY IG 0.4.0)**:
  - Missing `Bundle.timestamp`.
  - Bundle must include one `Patient` and one `Encounter`.
  - Ensure the presence of required resources: Bundle, Encounter, Patient, Organization, SDOHCC Observation Screening Response, and SDOHCC Consent.

### Official Public Site
- **URL**: [Official FHIR Validator](https://validator.fhir.org/)
- **Issues Identified**:
  - No additional issues compared to version 0.3.0.

### Official Local Docker Site
- **Validation using a locally hosted FHIR validator**
- **Issues Identified**:
  - No additional issues compared to version 0.3.0.

### Custom 1115 FHIR Server
- **URL**: [Custom 1115 FHIR Server](https://n9r2j0ii52.execute-api.ap-south-1.amazonaws.com/Prod/Bundle/$validate)
- **Issues Identified**:
  - Structural error due to an invalid `lastUpdated` date format.

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

## Changes Identified in Error Logs Compared to Version 0.3.0

### Legacy Inferno Public Site
#### SHIN-NY IG 0.3.0
- Missing `Bundle.timestamp`.
- `Bundle.total` exceeds allowed value.

#### SHIN-NY IG 0.4.0
- Missing `Bundle.timestamp`.
- Bundle must include `Patient` and `Encounter`.
- Missing required resources: Bundle, Encounter, Patient, Organization, SDOHCC Observation Screening Response, SDOHCC Consent.

#### Resolution Steps:
- Add `Bundle.timestamp`.
- Ensure at least one `Patient` and one `Encounter` are included.
- Include the required resources.

### Custom 1115 FHIR Server
#### Issue:
- Incorrect `lastUpdated` format.

#### Resolution:
- Correct `lastUpdated` format to `YYYY-MM-DDTHH:MM:SS.sssZ`.

## File to Be Tested
- [fhir-fixture-nyec-crossroads-scn-TestCase301.json](fhir-fixture-nyec-crossroads-scn-TestCase301.json)

## Steps for Correcting the FHIR Document

1. **Add `Bundle.timestamp`**:
    ```json
    "timestamp": "2024-05-28T10:07:42.914Z"
    ```

2. **Ensure One `Patient` and One `Encounter`**:
    - Add or ensure existing entries for `Patient` and `Encounter` within the Bundle.

3. **Include Required Resources**:
    - Ensure the Bundle contains entries for: Bundle, Encounter, Patient, Organization, SDOHCC Observation Screening Response, and SDOHCC Consent.

4. **Correct `lastUpdated` Format**:
    - Change the format to ISO 8601:
        ```json
        "lastUpdated": "2023-10-28T10:07:42.914Z"
        ```

By addressing these issues and updates, you can ensure the FHIR document will pass validation on the different platforms for SHIN-NY IG Version 0.4.0.
