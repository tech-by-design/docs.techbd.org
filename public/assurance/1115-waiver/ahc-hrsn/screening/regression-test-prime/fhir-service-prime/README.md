# 1115 Waiver HRSN Screening Assurance Results

## Overview
This repository includes a GitHub Actions workflow specifically designed for generating regression test results. Users can execute this workflow to validate changes and ensure the integrity of updates.

## Running the Regression Tests
To run the regression tests, you can trigger the manual GitHub Actions workflow available in this repository. The results of the tests are structured and stored as follows:

- Source files: `assurance/1115-waiver/ahc-hrsn/screening/regression-test-prime/fhir-service-prime/src/YYYY-MM-DD`
- Test results: `public/assurance/1115-waiver/ahc-hrsn/screening/regression-test-prime/fhir-service-prime/results/YYYY/MM/YYYY-MM-DD-HH-MM-SS`
- Latest results symlink `.../fhir-service-prime/results/latest` to `...fhir-service-prime/results/YYYY/MM/YYYY-MM-DD-HH-MM-SS` (most recently generated)

