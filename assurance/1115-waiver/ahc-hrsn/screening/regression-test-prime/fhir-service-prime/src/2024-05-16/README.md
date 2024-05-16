## Steps to test the .http files through CLI

```bash
$ npm install -g httpyac
$ cd assurance/1115-waiver/ahc-hrsn/screening/regression-test-prime/fhir-service-prime/src/YYYY-MM-DD
$ HOST=https://synthetic.fhir.api.devl.techbd.org httpyac send fhir-service.test.http --all
```

For more complete example, see [regression-test.sh](../../../regression-test.sh)

### `fhir-service.test.http`

This is the REST-API execution file performs the actual test. It interacts
with two primary API endpoints (`/Bundle/$validate` & `/Bundle/`) to ensure they are
functioning as expected. 

#### Running httpYac tests in Postman

For developers who prefer to use Postman for API testing and debugging, you can easily convert `fhir-service.test.http` httpYac file to Postman:

- Open the `fhir-service.test.http` and familiarize yourself with the structure of the file. You will see sections defining HTTP requests, including HTTP methods (GET, POST, etc.), URLs, headers, and body content.
- Open Postman and create a new collection.
- Add a new request to the collection for each HTTP request defined in the `fhir-service.test.http` file:
  - Copy the method (GET, POST, etc.) from the httpYac file and set it in Postman.
  - Copy the URL from the httpYac file and paste it into the Postman request URL field.
  - Set the request headers in Postman by copying the headers from the httpYac file. Ensure each header key and value is correctly set.
  - If the request includes a body, copy the body content from the httpYac file and paste it into the Postman body section. Select the appropriate body type (e.g., raw, JSON, form-data).
  - Be sure to replace variables as necessary

### `fhir-fixture-shinny-impl-guide-sample.json`

This JSON file contains sample data compliant with the implementation guidelines
of our FHIR service. It is used within the .http tests to simulate valid data
submission.

### `fhir-fixture-unhappy-path-01.json`

This JSON file provides deliberately flawed FHIR data used to test the error
handling capabilities of our FHIR service endpoints.

### `fhir-fixture-shinny-bronx-unhappy-path.json`

This JSON file from Bronx provides the FHIR data which has some errors.

### `fhir-fixture-shinny-healtheconnections-unhappy-path.json`

This JSON file from Healtheconnections provides the FHIR data which has some
errors.
