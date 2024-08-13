#  File evaluation against Hapi FHIR Server Version 7.2

## Files tested

- [AHCHRSNQuestionnaireResponseExample.json](AHCHRSNQuestionnaireResponseExample.json)

## NYeC expectations

```json
{
  "testcase": AHCHRSNQuestionnaireResponseExample,
  "csvoutputS3Bucket": "certification-engine-output",
  "testcasetype": "POSITIVE",
  "expectedResult": "AHCHRSNQuestionnaireResponseExample should succcessfully be processed by the QE and forwarded to NYeC.  The MPI for the patient should be added to the Patient resource."
}
```

## Results

```json
{
  "OperationOutcome": {
    "validationResults": [
      {
        "issues": [],
        "completedAt": 1723267394.3404713,
        "initiatedAt": 1723267394.1553183,
        "profileUrl": "https://djq7jdt8kb490.cloudfront.net/1115/StructureDefinition-SHINNYBundleProfile.json",
        "observability": {
          "identity": "org.techbd.orchestrate.fhir.OrchestrationEngine$HapiValidationEngine",
          "name": "HAPI version 7.2.0 (TODO:get from API instead of hard coding) (FHIR version 4.0.1)",
          "initAt": 1723195090.583773,
          "constructedAt": 1723195090.6018205
        },
        "operationOutcome": {
          "resourceType": "OperationOutcome",
          "issue": [
            {
              "severity": "information",
              "code": "informational",
              "diagnostics": "No issues detected during validation"
            }
          ]
        },
        "valid": true
      }
    ],
    "device": {
      "deviceId": "10.0.237.118",
      "deviceName": "ip-10-0-237-118.ec2.internal"
    },
    "resourceType": "OperationOutcome"
  }
}

```