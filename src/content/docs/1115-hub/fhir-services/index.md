---
title: FHIR-as-a-Service Solution
description: Introduction to HL7 FHIR and TechBD's FHIR-as-a-Service Solutions
sidebar:
  label: Home
---

TechBD's FHIR-as-a-Service solutions offer QEs a flexible and powerful way to
enhance their healthcare data exchange capabilities. Whether through
white-labeled services or API Gateway integration, TechBD provides the
infrastructure and support needed to ensure seamless, secure, and compliant data
interoperability.

## Overview

TechBD's FHIR-as-a-Service solutions offer two primary methods for QEs to
integrate and use these capabilities:

1. **White-Labeled Capability**: QEs can directly use TechBD's FHIR servers by
   aliasing them with their own DNS (using CNAME records). This allows QEs to
   present the service under their own brand while leveraging TechBD's robust
   infrastructure.
2. **API Gateway Mode**: QEs with their own FHIR servers can use them as API
   Gateways to proxy TechBD's FHIR services. This method integrates TechBD's
   solutions through the QEs' existing firewalls, providing a seamless extension
   of their current capabilities.

By utilizing TechBD's services, QEs benefit from a reliable, scalable, and
compliant FHIR solution that enhances their data exchange capabilities without
the need for significant in-house infrastructure investment.

**Data flow using QE CNAME Alias**

<pre class="mermaid">
sequenceDiagram
  autonumber

  participant SCN
  participant TechBD as QE TechBD Whitelabel
  participant TechBD_Database as TechBD Database
  participant DataLake as NYeC SHIN-NY Data Lake

  SCN->>TechBD: Sends FHIR JSON
  
  TechBD->>TechBD: Validates JSON using NYeC SHIN-NY IG
  TechBD->>TechBD: Might filter or rewrite diagnostics if requested by NYeC
  TechBD->>TechBD_Database: Stores payload and diagnostics
  TechBD->>SCN: Returns validation diagnostics
  SCN->>SCN: Takes any action they desire

  TechBD->>TechBD: Might transform JSON if requested by NYeC
  TechBD->>DataLake: POST FHIR JSON Data Lake (async)
  DataLake->>TechBD_Database: Stores Results (async)
</pre>

**Data flow using QE's own API Gateway**

<pre class="mermaid">
sequenceDiagram
  autonumber

  participant SCN
  participant QE
  participant TechBD
  participant TechBD_Database as TechBD Database
  participant DataLake as NYeC SHIN-NY Data Lake

  SCN->>QE: Sends FHIR JSON
  
  QE-->>TechBD: Forwards FHIR JSON

  TechBD->>TechBD: Validates JSON using NYeC SHIN-NY IG
  TechBD->>TechBD: Might filter or rewrite diagnostics if requested by NYeC
  TechBD->>TechBD_Database: Stores payload and diagnostics
  TechBD->>QE: Returns validation diagnostics
  QE-->>SCN: Forwards response
  SCN->>SCN: Takes any action they desire

  TechBD->>TechBD: Might transform JSON if requested by NYeC
  TechBD->>DataLake: POST FHIR JSON Data Lake (async)
  DataLake->>TechBD_Database: Stores Results (async)

  QE->>TechBD_Database: Queries Results whenever it desires (useful to find out the result of the data lake submission)
</pre>


## Technology Strategy

TechBD's FHIR-as-a-Service solutions are designed to be highly accessible and
easy to integrate with existing systems. Here's how to get started:

#### White-Labeled Capability

1. **DNS Configuration**: Set up a CNAME record in your DNS to alias TechBD's
   FHIR server endpoints. This will route requests from your domain to TechBD's
   infrastructure.
2. **Authentication**: Uses TechBD's built-authentication capabilities as-is.
3. **API Endpoints**: Uses TechBD's defined endpoints as-is.

#### API Gateway Mode

1. **Set Up Your FHIR Server**: Ensure your FHIR server is configured to act as
   an API Gateway.
2. **Proxy Configuration**: Configure your server to forward requests to
   TechBD's FHIR endpoints. This typically involves setting up routing rules
   that direct specific FHIR API calls to TechBD's infrastructure.
3. **Firewall and Security**: Ensure that your firewall rules allow for secure
   communication between your server and TechBD's endpoints. Implement necessary
   security measures like TLS/SSL.
4. **API Usage**: Once set up, use the FHIR API as usual. Your server will proxy
   the requests to TechBD, and you can handle responses within your existing
   infrastructure.

### API Overview

- **FHIR Server Base URL**: [`https://synthetic.fhir.api.devl.techbd.org`](https://synthetic.fhir.api.devl.techbd.org/metadata)
- **FHIR Server Capabilities**: [`https://synthetic.fhir.api.devl.techbd.org/metadata`](https://synthetic.fhir.api.devl.techbd.org/metadata) (returns XML)
- **Authentication**: None at this time, will be defined and deployed soon.
- **Bundle Endpoints**:
  - **Validate Bundle**: `/Bundle/$validate`
  - **Submit Bundle to SHIN-NY Data Lake**: `/Bundle`
- **Browse Requests and Responses**: [/admin/diagnostics](https://synthetic.fhir.api.devl.techbd.org/admin/diagnostics)

Learn more about all of the endpoints by reviewing [TechBD's FHIR API Test Script](/docs.techbd.org/assurance/1115-waiver/ahc-hrsn/screening/regression-test-prime/fhir-service-prime/results/latest/src/fhir-service.test.http) and most recent [TechBD's FHIR API Test Script Results](/docs.techbd.org/1115-hub/fhir-services/regression-test-results/). 