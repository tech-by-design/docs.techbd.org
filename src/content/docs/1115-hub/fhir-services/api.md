---
title: API Endpoints
---

- **FHIR Server Base URL**: [`https://synthetic.fhir.api.devl.techbd.org`](https://synthetic.fhir.api.devl.techbd.org/metadata)
- **Swagger API Documentation URL**: [`https://synthetic.fhir.api.devl.techbd.org/dx/docs/api/swagger-v3/swagger-ui/index.html`](https://synthetic.fhir.api.devl.techbd.org/dx/docs/api/swagger-v3/swagger-ui/index.html)
- **FHIR Server Capabilities**: [`https://synthetic.fhir.api.devl.techbd.org/metadata`](https://synthetic.fhir.api.devl.techbd.org/metadata) (returns XML)
- **Authentication**: None at this time, will be defined and deployed soon.
- **Bundle Endpoints**:
  - **Validate Bundle**: `/Bundle/$validate`
  - **Submit Bundle to SHIN-NY Data Lake**: `/Bundle`
- **Browse Requests and Responses**: [/admin/diagnostics](https://synthetic.fhir.api.devl.techbd.org/admin/diagnostics)

Learn more about all of the endpoints by reviewing [TechBD's FHIR API Test Script](/docs.techbd.org/assurance/1115-waiver/ahc-hrsn/screening/regression-test-prime/fhir-service-prime/results/latest/src/fhir-service.test.http) and most recent [TechBD's FHIR API Test Script Results](/docs.techbd.org/1115-hub/fhir-services/regression-test-results/). 

### Architecture

![FHIR Server Architecture](/docs.techbd.org/content/docs/1115-hub/fhir-services/qcs-fhir-service.drawio.svg)