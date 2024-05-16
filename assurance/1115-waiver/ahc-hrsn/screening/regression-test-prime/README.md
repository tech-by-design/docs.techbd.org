# 1115 Waiver HRSN Screening Assurance Results

The work products in this direcotry generate regression test results. 

## Running the Regression Tests via GitHub Actions

1. Go to [docs.techbd.org GitHub Action](https://github.com/tech-by-design/docs.techbd.org/actions/workflows/regression-test.yml)
2. Pull down the `Run workflow` combo box and then tap `Run workflow`.

## Running the Regression Tests Locally

```bash
# assuming you're in the project root
$ ./assurance/1115-waiver/ahc-hrsn/screening/regression-test-prime/regression-test.sh
```

`regression-test.sh` assumes the following locations (pay special attention to `YYYY-MM-DD`):

- Canonical FHIR source files: `assurance/1115-waiver/ahc-hrsn/screening/regression-test-prime/fhir-service-prime/src/YYYY-MM-DD`
- Generated FHIR test results: `public/assurance/1115-waiver/ahc-hrsn/screening/regression-test-prime/fhir-service-prime/results/YYYY/MM/YYYY-MM-DD-HH-MM-SS`
- FHIR test source files symlink in Generated FHIR test results: `...fhir-service-prime/results/YYYY/MM/YYYY-MM-DD-HH-MM-SS/src` will link to FHIR test source files directory (for convenient access)
- Latest results symlink `...fhir-service-prime/results/latest` to `...fhir-service-prime/results/YYYY/MM/YYYY-MM-DD-HH-MM-SS` (for convenient access to most recently generated test case directory)

## Directory Structure

- [FHIR Service (Prime)](./fhir-service-prime/) contains regression test suites and fixtures for TechBD's FHIR Server.
- TODO: `sftp-service-prime` contains regression test suites and fixtures for TechBD's SFTP Server.