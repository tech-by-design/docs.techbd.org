# File evaluation against Custom 1115 FHIR Server

## Files tested

- [fhir-fixture-nyec-crossroads-scn-TestCase300.json](fhir-fixture-nyec-crossroads-scn-TestCase300.json)

## NYeC expectations

```json
{
  "testcase": 300,
  "csvoutputS3Bucket": "certification-engine-output",
  "testcasetype": "POSITIVE",
  "expectedResult": "Test Case 300 should succcessfully be processed by the QE and forwarded to NYeC.  The MPI for the patient should be added to the Patient resource."
}
```

## Results

```json

{
  "OperationOutcome": {
    "resourceType": "OperationOutcome",
    "validationResults": [
      {
        "profileUrl": "http://10.10.11.187/StructureDefinition-SHINNYBundleProfile.json",
        "issues": [
          {
            "location": {
              "line": 1,
              "column": 91,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value '0978bab8-c510-455c-8f10-f6772c0143f6_1793' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 91,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value '0978bab8-c510-455c-8f10-f6772c0143f6_1793' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 876,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'CNYSCN~bronx-20240417-testcase1-MRN' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 876,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'CNYSCN~bronx-20240417-testcase1-MRN' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 4117,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'cnyscn~bronxxbgu1so3y4' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 4117,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'cnyscn~bronxxbgu1so3y4' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 5711,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'Consent_CNYSCN~bronx-20240417-testcase1-MRN' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 5711,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'Consent_CNYSCN~bronx-20240417-testcase1-MRN' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 6762,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_1' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 6762,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_1' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 8431,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 8431,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 9024,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_2' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 9024,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_2' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 10670,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 10670,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 11252,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_3' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 11252,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_3' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 12806,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 12806,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 13386,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_4' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 13386,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_4' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 14926,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 14926,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 15517,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_5' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 15517,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_5' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 17071,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 17071,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 17660,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_6' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 17660,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_6' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 19372,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 19372,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 19965,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_7' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 19965,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_7' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 21711,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 21711,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 22291,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_8' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 22291,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_8' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 24011,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 24011,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 24591,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_9' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 24591,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_9' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 26329,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 26329,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 26910,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_10' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 26910,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_10' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 28821,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 28821,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 29404,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_11' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 29404,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_11' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 30931,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 30931,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 31529,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_12' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 31529,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_12' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 33160,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 33160,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 33764,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_13' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 33764,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_13' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 35293,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 35293,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 35902,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_14' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 35902,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_14' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 37434,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 37434,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 37947,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_15' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 37947,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_15' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 39520,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 39520,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 40109,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_16' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 40109,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_16' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 41808,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 41808,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 42397,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_17' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 42397,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_17' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 44215,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 44215,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 44810,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_18' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 44810,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_18' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 46553,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 46553,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 47158,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_19' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 47158,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_19' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 48685,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 48685,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 49429,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_Grouper1' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 49429,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_Grouper1' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 52402,
              "diagnostics": null
            },
            "message": "cvc-pattern-valid: Value '2005-02-18T00:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
            "severity": "ERROR"
          },
          {
            "location": {
              "line": 1,
              "column": 52402,
              "diagnostics": null
            },
            "message": "cvc-attribute.3: The value '2005-02-18T00:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
            "severity": "ERROR"
          }
        ],
        "operationOutcome": {
          "resourceType": "OperationOutcome",
          "issue": [
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 91
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value '0978bab8-c510-455c-8f10-f6772c0143f6_1793' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[91]",
                "Line[1] Col[91]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 91
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value '0978bab8-c510-455c-8f10-f6772c0143f6_1793' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[91]",
                "Line[1] Col[91]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 876
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'CNYSCN~bronx-20240417-testcase1-MRN' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[876]",
                "Line[1] Col[876]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 876
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'CNYSCN~bronx-20240417-testcase1-MRN' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[876]",
                "Line[1] Col[876]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 4117
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'cnyscn~bronxxbgu1so3y4' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[4117]",
                "Line[1] Col[4117]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 4117
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'cnyscn~bronxxbgu1so3y4' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[4117]",
                "Line[1] Col[4117]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 5711
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'Consent_CNYSCN~bronx-20240417-testcase1-MRN' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[5711]",
                "Line[1] Col[5711]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 5711
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'Consent_CNYSCN~bronx-20240417-testcase1-MRN' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[5711]",
                "Line[1] Col[5711]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 6762
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_1' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[6762]",
                "Line[1] Col[6762]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 6762
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_1' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[6762]",
                "Line[1] Col[6762]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 8431
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[8431]",
                "Line[1] Col[8431]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 8431
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[8431]",
                "Line[1] Col[8431]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 9024
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_2' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[9024]",
                "Line[1] Col[9024]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 9024
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_2' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[9024]",
                "Line[1] Col[9024]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 10670
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[10670]",
                "Line[1] Col[10670]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 10670
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[10670]",
                "Line[1] Col[10670]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 11252
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_3' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[11252]",
                "Line[1] Col[11252]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 11252
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_3' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[11252]",
                "Line[1] Col[11252]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 12806
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[12806]",
                "Line[1] Col[12806]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 12806
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[12806]",
                "Line[1] Col[12806]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 13386
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_4' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[13386]",
                "Line[1] Col[13386]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 13386
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_4' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[13386]",
                "Line[1] Col[13386]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 14926
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[14926]",
                "Line[1] Col[14926]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 14926
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[14926]",
                "Line[1] Col[14926]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 15517
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_5' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[15517]",
                "Line[1] Col[15517]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 15517
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_5' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[15517]",
                "Line[1] Col[15517]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 17071
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[17071]",
                "Line[1] Col[17071]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 17071
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[17071]",
                "Line[1] Col[17071]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 17660
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_6' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[17660]",
                "Line[1] Col[17660]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 17660
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_6' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[17660]",
                "Line[1] Col[17660]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 19372
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[19372]",
                "Line[1] Col[19372]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 19372
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[19372]",
                "Line[1] Col[19372]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 19965
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_7' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[19965]",
                "Line[1] Col[19965]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 19965
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_7' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[19965]",
                "Line[1] Col[19965]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 21711
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[21711]",
                "Line[1] Col[21711]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 21711
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[21711]",
                "Line[1] Col[21711]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 22291
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_8' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[22291]",
                "Line[1] Col[22291]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 22291
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_8' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[22291]",
                "Line[1] Col[22291]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 24011
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[24011]",
                "Line[1] Col[24011]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 24011
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[24011]",
                "Line[1] Col[24011]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 24591
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_9' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[24591]",
                "Line[1] Col[24591]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 24591
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_9' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[24591]",
                "Line[1] Col[24591]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 26329
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[26329]",
                "Line[1] Col[26329]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 26329
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[26329]",
                "Line[1] Col[26329]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 26910
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_10' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[26910]",
                "Line[1] Col[26910]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 26910
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_10' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[26910]",
                "Line[1] Col[26910]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 28821
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[28821]",
                "Line[1] Col[28821]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 28821
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[28821]",
                "Line[1] Col[28821]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 29404
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_11' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[29404]",
                "Line[1] Col[29404]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 29404
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_11' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[29404]",
                "Line[1] Col[29404]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 30931
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[30931]",
                "Line[1] Col[30931]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 30931
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[30931]",
                "Line[1] Col[30931]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 31529
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_12' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[31529]",
                "Line[1] Col[31529]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 31529
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_12' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[31529]",
                "Line[1] Col[31529]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 33160
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[33160]",
                "Line[1] Col[33160]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 33160
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[33160]",
                "Line[1] Col[33160]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 33764
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_13' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[33764]",
                "Line[1] Col[33764]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 33764
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_13' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[33764]",
                "Line[1] Col[33764]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 35293
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[35293]",
                "Line[1] Col[35293]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 35293
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[35293]",
                "Line[1] Col[35293]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 35902
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_14' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[35902]",
                "Line[1] Col[35902]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 35902
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_14' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[35902]",
                "Line[1] Col[35902]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 37434
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[37434]",
                "Line[1] Col[37434]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 37434
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[37434]",
                "Line[1] Col[37434]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 37947
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_15' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[37947]",
                "Line[1] Col[37947]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 37947
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_15' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[37947]",
                "Line[1] Col[37947]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 39520
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[39520]",
                "Line[1] Col[39520]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 39520
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[39520]",
                "Line[1] Col[39520]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 40109
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_16' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[40109]",
                "Line[1] Col[40109]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 40109
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_16' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[40109]",
                "Line[1] Col[40109]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 41808
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[41808]",
                "Line[1] Col[41808]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 41808
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[41808]",
                "Line[1] Col[41808]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 42397
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_17' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[42397]",
                "Line[1] Col[42397]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 42397
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_17' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[42397]",
                "Line[1] Col[42397]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 44215
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[44215]",
                "Line[1] Col[44215]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 44215
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[44215]",
                "Line[1] Col[44215]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 44810
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_18' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[44810]",
                "Line[1] Col[44810]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 44810
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_18' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[44810]",
                "Line[1] Col[44810]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 46553
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[46553]",
                "Line[1] Col[46553]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 46553
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[46553]",
                "Line[1] Col[46553]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 47158
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_19' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[47158]",
                "Line[1] Col[47158]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 47158
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_19' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[47158]",
                "Line[1] Col[47158]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 48685
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value '1969-12-31T19:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[48685]",
                "Line[1] Col[48685]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 48685
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value '1969-12-31T19:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[48685]",
                "Line[1] Col[48685]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 49429
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_Grouper1' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "location": [
                "Line[1] Col[49429]",
                "Line[1] Col[49429]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 49429
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_Grouper1' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "location": [
                "Line[1] Col[49429]",
                "Line[1] Col[49429]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 52402
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-pattern-valid: Value '2005-02-18T00:00:00' is not facet-valid with respect to pattern '([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[0-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\\.[0-9]+)?(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?' for type 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[52402]",
                "Line[1] Col[52402]"
              ]
            },
            {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line",
                  "valueInteger": 1
                },
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-col",
                  "valueInteger": 52402
                }
              ],
              "severity": "error",
              "code": "processing",
              "diagnostics": "cvc-attribute.3: The value '2005-02-18T00:00:00' of attribute 'value' on element 'effectiveDateTime' is not valid with respect to its type, 'dateTime-primitive'.",
              "location": [
                "Line[1] Col[52402]",
                "Line[1] Col[52402]"
              ]
            }
          ]
        },
        "engine": "HAPI",
        "valid": false
      },
      {
        "profileUrl": "http://10.10.11.187/StructureDefinition-SHINNYBundleProfile.json",
        "issues": [],
        "operationOutcome": null,
        "engine": "HL7",
        "valid": true
      },
      {
        "profileUrl": "http://10.10.11.187/StructureDefinition-SHINNYBundleProfile.json",
        "issues": [],
        "operationOutcome": null,
        "engine": "INFERNO",
        "valid": true
      }
    ],
    "device": {
      "deviceId": "127.0.1.1",
      "deviceName": "vinod-OptiPlex"
    }
  }
}
```