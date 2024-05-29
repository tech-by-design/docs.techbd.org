# File evaluation against Custom 1115 FHIR Server

## Files tested

- [fhir-fixture-nyec-crossroads-scn-TestCase301.json](fhir-fixture-nyec-crossroads-scn-TestCase301.json)

## NYeC expectations

```json
{
  "testcase": 301,
  "csvoutputS3Bucket": "certification-engine-output",
  "testcasetype": "POSITIVE",
  "expectedResult": "Test Case 301 should succcessfully be processed by the QE and forwarded to NYeC.  The MPI for the patient should be added to the Patient resource."
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
              "line": null,
              "column": null,
              "diagnostics": "ca.uhn.fhir.parser.DataFormatException"
            },
            "message": "HAPI-1821: [element=\"lastUpdated\"] Invalid attribute value \"2023-10-28 10:07:42.9149210\": Invalid date/time format: \"2023-10-28 10:07:42.9149210\": Expected character 'T' at index 10 but found  ",
            "severity": "FATAL"
          }
        ],
        "operationOutcome": null,
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
      "deviceId": "",
      "deviceName": ""
    }
  }
}
```