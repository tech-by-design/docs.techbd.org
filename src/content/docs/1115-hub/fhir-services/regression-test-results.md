---
title: Regression Test Results
---

**FHIR Server Base URL for Synthetic Data Exchange**: `https://synthetic.fhir.api.devl.techbd.org`. No authentication requried at this time, will be defined and deployed soon.

### Tech by Design FHIR API test scripts and results

Learn about API endpoints by reviewing [Tech by Design's FHIR API Test Script](/docs.techbd.org/assurance/1115-waiver/ahc-hrsn/screening/regression-test-prime/fhir-service-prime/results/latest/src/fhir-service.test.http). 
- [Latest Test Fixtures](https://github.com/tech-by-design/docs.techbd.org/tree/main/assurance/1115-waiver/ahc-hrsn/screening/regression-test-prime/fhir-service-prime/src/2024-09-27) (generated test cases)
- [Latest Test Results (HTML from httpYac)](/docs.techbd.org/assurance/1115-waiver/ahc-hrsn/screening/regression-test-prime/fhir-service-prime/results/latest/regression-test-results.httpyac.junit.xml.html)
- [Latest Test Results (httpYac raw output)](/docs.techbd.org/assurance/1115-waiver/ahc-hrsn/screening/regression-test-prime/fhir-service-prime/results/latest/regression-test-results.httpyac.txt)
- [Previous Test Results](https://github.com/tech-by-design/docs.techbd.org/tree/main/public/assurance/1115-waiver/ahc-hrsn/screening/regression-test-prime/fhir-service-prime/results/2024/08)


#### Postman-based API test scripts

For developers who prefer to use Postman for API testing and debugging, instead of Tech by Design's [httpYac](https://httpyac.github.io/)-based strategy, you can easily convert [`fhir-service.test.http`](/docs.techbd.org/assurance/1115-waiver/ahc-hrsn/screening/regression-test-prime/fhir-service-prime/results/latest/src/fhir-service.test.http) httpYac file to Postman:

- Open the `fhir-service.test.http` and familiarize yourself with the structure of the file. You will see sections defining HTTP requests, including HTTP methods (GET, POST, etc.), URLs, headers, and body content.
- Open Postman and create a new collection.
- Add a new request to the collection for each HTTP request defined in the `fhir-service.test.http` file:
  - Copy the method (GET, POST, etc.) from the httpYac file and set it in Postman.
  - Copy the URL from the httpYac file and paste it into the Postman request URL field.
  - Set the request headers in Postman by copying the headers from the httpYac file. Ensure each header key and value is correctly set.
  - If the request includes a body, copy the body content from the httpYac file and paste it into the Postman body section. Select the appropriate body type (e.g., raw, JSON, form-data).
  - Be sure to replace variables as necessary

