# File evaluation against Custom 1115 FHIR Server

## Files tested

- [TestCase300.json](TestCase300.json)

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
      "uaValidationStrategy": {
        "issues": [],
        "X-TechBD-FHIR-Validation-Strategy": "{ \"engines\": [\"HAPI\"  ]}"
      },
      "validationResults": [
        {
          "observability": {
            "identity": "org.techbd.orchestrate.fhir.OrchestrationEngine$HapiValidationEngine",
            "name": "HAPI version TODO (FHIR version 4.0.1)",
            "initAt": "2024-06-10T07:18:24.029003798Z",
            "constructedAt": "2024-06-10T07:18:24.053069991Z"
          },
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
                "column": 3853,
                "diagnostics": null
              },
              "message": "cvc-pattern-valid: Value 'cnyscn~bronxxbgu1so3y4' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 3853,
                "diagnostics": null
              },
              "message": "cvc-attribute.3: The value 'cnyscn~bronxxbgu1so3y4' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 5447,
                "diagnostics": null
              },
              "message": "cvc-pattern-valid: Value 'Consent_CNYSCN~bronx-20240417-testcase1-MRN' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 5447,
                "diagnostics": null
              },
              "message": "cvc-attribute.3: The value 'Consent_CNYSCN~bronx-20240417-testcase1-MRN' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 6498,
                "diagnostics": null
              },
              "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_1' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 6498,
                "diagnostics": null
              },
              "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_1' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 8766,
                "diagnostics": null
              },
              "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_2' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 8766,
                "diagnostics": null
              },
              "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_2' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 11000,
                "diagnostics": null
              },
              "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_3' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 11000,
                "diagnostics": null
              },
              "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_3' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 13140,
                "diagnostics": null
              },
              "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_4' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 13140,
                "diagnostics": null
              },
              "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_4' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 15277,
                "diagnostics": null
              },
              "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_5' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 15277,
                "diagnostics": null
              },
              "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_5' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 17426,
                "diagnostics": null
              },
              "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_6' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 17426,
                "diagnostics": null
              },
              "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_6' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 19737,
                "diagnostics": null
              },
              "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_7' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 19737,
                "diagnostics": null
              },
              "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_7' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 22069,
                "diagnostics": null
              },
              "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_8' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 22069,
                "diagnostics": null
              },
              "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_8' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 24375,
                "diagnostics": null
              },
              "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_9' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 24375,
                "diagnostics": null
              },
              "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_9' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 26700,
                "diagnostics": null
              },
              "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_10' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 26700,
                "diagnostics": null
              },
              "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_10' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 29200,
                "diagnostics": null
              },
              "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_11' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 29200,
                "diagnostics": null
              },
              "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_11' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 31331,
                "diagnostics": null
              },
              "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_12' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 31331,
                "diagnostics": null
              },
              "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_12' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 33572,
                "diagnostics": null
              },
              "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_13' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 33572,
                "diagnostics": null
              },
              "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_13' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 35716,
                "diagnostics": null
              },
              "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_14' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 35716,
                "diagnostics": null
              },
              "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_14' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 37767,
                "diagnostics": null
              },
              "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_15' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 37767,
                "diagnostics": null
              },
              "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_15' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 39935,
                "diagnostics": null
              },
              "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_16' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 39935,
                "diagnostics": null
              },
              "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_16' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 42229,
                "diagnostics": null
              },
              "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_17' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 42229,
                "diagnostics": null
              },
              "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_17' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 44648,
                "diagnostics": null
              },
              "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_18' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 44648,
                "diagnostics": null
              },
              "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_18' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 47002,
                "diagnostics": null
              },
              "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_19' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 47002,
                "diagnostics": null
              },
              "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_19' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 49279,
                "diagnostics": null
              },
              "message": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_Grouper1' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
              "severity": "ERROR"
            },
            {
              "location": {
                "line": 1,
                "column": 49279,
                "diagnostics": null
              },
              "message": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_Grouper1' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
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
                    "valueInteger": 3853
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-pattern-valid: Value 'cnyscn~bronxxbgu1so3y4' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
                "location": [
                  "Line[1] Col[3853]",
                  "Line[1] Col[3853]"
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
                    "valueInteger": 3853
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-attribute.3: The value 'cnyscn~bronxxbgu1so3y4' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
                "location": [
                  "Line[1] Col[3853]",
                  "Line[1] Col[3853]"
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
                    "valueInteger": 5447
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-pattern-valid: Value 'Consent_CNYSCN~bronx-20240417-testcase1-MRN' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
                "location": [
                  "Line[1] Col[5447]",
                  "Line[1] Col[5447]"
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
                    "valueInteger": 5447
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-attribute.3: The value 'Consent_CNYSCN~bronx-20240417-testcase1-MRN' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
                "location": [
                  "Line[1] Col[5447]",
                  "Line[1] Col[5447]"
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
                    "valueInteger": 6498
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_1' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
                "location": [
                  "Line[1] Col[6498]",
                  "Line[1] Col[6498]"
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
                    "valueInteger": 6498
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_1' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
                "location": [
                  "Line[1] Col[6498]",
                  "Line[1] Col[6498]"
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
                    "valueInteger": 8766
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_2' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
                "location": [
                  "Line[1] Col[8766]",
                  "Line[1] Col[8766]"
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
                    "valueInteger": 8766
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_2' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
                "location": [
                  "Line[1] Col[8766]",
                  "Line[1] Col[8766]"
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
                    "valueInteger": 11000
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_3' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
                "location": [
                  "Line[1] Col[11000]",
                  "Line[1] Col[11000]"
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
                    "valueInteger": 11000
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_3' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
                "location": [
                  "Line[1] Col[11000]",
                  "Line[1] Col[11000]"
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
                    "valueInteger": 13140
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_4' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
                "location": [
                  "Line[1] Col[13140]",
                  "Line[1] Col[13140]"
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
                    "valueInteger": 13140
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_4' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
                "location": [
                  "Line[1] Col[13140]",
                  "Line[1] Col[13140]"
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
                    "valueInteger": 15277
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_5' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
                "location": [
                  "Line[1] Col[15277]",
                  "Line[1] Col[15277]"
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
                    "valueInteger": 15277
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_5' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
                "location": [
                  "Line[1] Col[15277]",
                  "Line[1] Col[15277]"
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
                    "valueInteger": 17426
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_6' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
                "location": [
                  "Line[1] Col[17426]",
                  "Line[1] Col[17426]"
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
                    "valueInteger": 17426
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_6' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
                "location": [
                  "Line[1] Col[17426]",
                  "Line[1] Col[17426]"
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
                    "valueInteger": 19737
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_7' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
                "location": [
                  "Line[1] Col[19737]",
                  "Line[1] Col[19737]"
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
                    "valueInteger": 19737
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_7' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
                "location": [
                  "Line[1] Col[19737]",
                  "Line[1] Col[19737]"
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
                    "valueInteger": 22069
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_8' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
                "location": [
                  "Line[1] Col[22069]",
                  "Line[1] Col[22069]"
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
                    "valueInteger": 22069
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_8' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
                "location": [
                  "Line[1] Col[22069]",
                  "Line[1] Col[22069]"
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
                    "valueInteger": 24375
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_9' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
                "location": [
                  "Line[1] Col[24375]",
                  "Line[1] Col[24375]"
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
                    "valueInteger": 24375
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_9' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
                "location": [
                  "Line[1] Col[24375]",
                  "Line[1] Col[24375]"
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
                    "valueInteger": 26700
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_10' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
                "location": [
                  "Line[1] Col[26700]",
                  "Line[1] Col[26700]"
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
                    "valueInteger": 26700
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_10' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
                "location": [
                  "Line[1] Col[26700]",
                  "Line[1] Col[26700]"
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
                    "valueInteger": 29200
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_11' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
                "location": [
                  "Line[1] Col[29200]",
                  "Line[1] Col[29200]"
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
                    "valueInteger": 29200
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_11' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
                "location": [
                  "Line[1] Col[29200]",
                  "Line[1] Col[29200]"
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
                    "valueInteger": 31331
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_12' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
                "location": [
                  "Line[1] Col[31331]",
                  "Line[1] Col[31331]"
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
                    "valueInteger": 31331
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_12' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
                "location": [
                  "Line[1] Col[31331]",
                  "Line[1] Col[31331]"
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
                    "valueInteger": 33572
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_13' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
                "location": [
                  "Line[1] Col[33572]",
                  "Line[1] Col[33572]"
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
                    "valueInteger": 33572
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_13' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
                "location": [
                  "Line[1] Col[33572]",
                  "Line[1] Col[33572]"
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
                    "valueInteger": 35716
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_14' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
                "location": [
                  "Line[1] Col[35716]",
                  "Line[1] Col[35716]"
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
                    "valueInteger": 35716
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_14' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
                "location": [
                  "Line[1] Col[35716]",
                  "Line[1] Col[35716]"
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
                    "valueInteger": 37767
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_15' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
                "location": [
                  "Line[1] Col[37767]",
                  "Line[1] Col[37767]"
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
                    "valueInteger": 37767
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_15' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
                "location": [
                  "Line[1] Col[37767]",
                  "Line[1] Col[37767]"
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
                    "valueInteger": 39935
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_16' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
                "location": [
                  "Line[1] Col[39935]",
                  "Line[1] Col[39935]"
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
                    "valueInteger": 39935
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_16' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
                "location": [
                  "Line[1] Col[39935]",
                  "Line[1] Col[39935]"
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
                    "valueInteger": 42229
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_17' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
                "location": [
                  "Line[1] Col[42229]",
                  "Line[1] Col[42229]"
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
                    "valueInteger": 42229
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_17' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
                "location": [
                  "Line[1] Col[42229]",
                  "Line[1] Col[42229]"
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
                    "valueInteger": 44648
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_18' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
                "location": [
                  "Line[1] Col[44648]",
                  "Line[1] Col[44648]"
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
                    "valueInteger": 44648
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_18' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
                "location": [
                  "Line[1] Col[44648]",
                  "Line[1] Col[44648]"
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
                    "valueInteger": 47002
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_19' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
                "location": [
                  "Line[1] Col[47002]",
                  "Line[1] Col[47002]"
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
                    "valueInteger": 47002
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_19' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
                "location": [
                  "Line[1] Col[47002]",
                  "Line[1] Col[47002]"
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
                    "valueInteger": 49279
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-pattern-valid: Value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_Grouper1' is not facet-valid with respect to pattern '[A-Za-z0-9\\-\\.]{1,64}' for type 'id-primitive'.",
                "location": [
                  "Line[1] Col[49279]",
                  "Line[1] Col[49279]"
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
                    "valueInteger": 49279
                  }
                ],
                "severity": "error",
                "code": "processing",
                "diagnostics": "cvc-attribute.3: The value 'dd9f3a5bc72ea5a576a1a9117cd2a34d_obs3_Grouper1' of attribute 'value' on element 'id' is not valid with respect to its type, 'id-primitive'.",
                "location": [
                  "Line[1] Col[49279]",
                  "Line[1] Col[49279]"
                ]
              }
            ]
          },
          "completedAt": "2024-06-10T07:24:22.745536310Z",
          "profileUrl": "https://djq7jdt8kb490.cloudfront.net/1115/StructureDefinition-SHINNYBundleProfile.json",
          "initiatedAt": "2024-06-10T07:24:22.689035553Z",
          "valid": false
        }
      ],
      "device": {
        "deviceId": "10.0.202.168",
        "deviceName": "ip-10-0-202-168.ec2.internal"
      },
      "resourceType": "OperationOutcome"
    }
  }

```