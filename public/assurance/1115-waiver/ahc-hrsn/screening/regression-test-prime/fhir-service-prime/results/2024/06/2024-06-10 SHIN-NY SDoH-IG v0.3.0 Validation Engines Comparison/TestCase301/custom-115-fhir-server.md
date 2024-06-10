# File evaluation against Custom 1115 FHIR Server

## Files tested

- [TestCase301.json](TestCase301.json)

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
                "line": null,
                "column": null,
                "diagnostics": "ca.uhn.fhir.parser.DataFormatException"
              },
              "message": "HAPI-1821: [element=\"gender\"] Invalid attribute value \"UN\": Unknown AdministrativeGender code 'UN'",
              "severity": "FATAL"
            }
          ],
          "operationOutcome": null,
          "completedAt": "2024-06-10T07:28:53.702106248Z",
          "profileUrl": "https://djq7jdt8kb490.cloudfront.net/1115/StructureDefinition-SHINNYBundleProfile.json",
          "initiatedAt": "2024-06-10T07:28:53.700570476Z",
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