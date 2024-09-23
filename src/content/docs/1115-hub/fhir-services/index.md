---
title: FHIR-as-a-Service Solution
description: Introduction to HL7 FHIR and Tech by Design's FHIR-as-a-Service Solutions
sidebar:
  label: Home
---

Tech by Design's FHIR-as-a-Service solutions offer QEs a flexible and powerful way to
enhance their healthcare data exchange capabilities. Whether through
white-labeled services or API Gateway integration, Tech by Design provides the
infrastructure and support needed to ensure seamless, secure, and compliant data
interoperability.

## QE Integration Options

Tech by Design's FHIR-as-a-Service solutions offer two primary methods for QEs to
integrate and use these capabilities:

1. **Instant-start White-Labeled Mode**: QEs can directly use Tech by Design's FHIR servers by
   aliasing them with their own DNS (using CNAME records). This allows QEs to
   present the service under their own brand while leveraging Tech by Design's robust
   infrastructure.
2. **API Gateway Mode**: QEs with their own FHIR servers can use them as API
   Gateways to proxy Tech by Design's FHIR services. This method integrates Tech by Design's
   solutions through the QEs' existing firewalls, providing a seamless extension
   of their current capabilities.

By utilizing Tech by Design's services, QEs benefit from a reliable, scalable, and
compliant FHIR solution that enhances their data exchange capabilities without
the need for significant in-house infrastructure investment.

## Technology Strategy

Tech by Design's FHIR-as-a-Service solutions are designed to be highly accessible and
easy to integrate with existing systems. Here's how to get started:

#### Instant-start White-Labeled Mode

1. **DNS Configuration**: Set up a CNAME record in your DNS to alias Tech by Design's
   FHIR server endpoints. This will route requests from your domain to Tech by Design's
   infrastructure.
2. **Authentication**: Uses Tech by Design's built-authentication capabilities as-is.
3. **API Endpoints**: Uses Tech by Design's defined endpoints as-is.

- **Pros**:
  - Quick deployment requires a one-time DNS server update by Ops personnel and
    minimizes the need for developer or engineering talent.
  - Minimal infrastructure overhead dramatically simplifies QE operations.
  - All observability (logging), authentication, security, and functionality is
    handled by Tech by Design.

- **Cons**:
  - Limited customization options may hinder some QE developer needs.

<pre class="mermaid">
sequenceDiagram
  autonumber

  participant SCN
  participant Tech by Design as QE Tech by Design Whitelabel
  participant Tech by Design_Database as Tech by Design Database
  participant DataLake as NYeC SHIN-NY Data Lake

  SCN->>Tech by Design: Sends FHIR JSON
  
  Tech by Design->>Tech by Design: Validates JSON using NYeC SHIN-NY IG
  Tech by Design->>Tech by Design: Might filter or rewrite diagnostics if requested by NYeC
  Tech by Design->>Tech by Design_Database: Stores payload and diagnostics
  Tech by Design->>SCN: Returns validation diagnostics
  SCN->>SCN: Takes any action they desire

  Tech by Design->>Tech by Design: Might transform JSON if requested by NYeC
  Tech by Design->>DataLake: POST FHIR JSON Data Lake (async)
  DataLake->>Tech by Design_Database: Stores Results (async)
</pre>

#### API Gateway Mode

1. **Set Up Your FHIR Server**: Ensure your FHIR server is configured to act as
   an API Gateway.
2. **Proxy Configuration**: Configure your server to forward requests to
   Tech by Design's FHIR endpoints. This typically involves setting up routing rules
   that direct specific FHIR API calls to Tech by Design's infrastructure.
3. **Firewall and Security**: Ensure that your firewall rules allow for secure
   communication between your server and Tech by Design's endpoints. Implement necessary
   security measures like TLS/SSL.
4. **API Usage**: Once set up, use the FHIR API as usual. Your server will proxy
   the requests to Tech by Design, and you can handle responses within your existing
   infrastructure.

- **Pros**:
  - Greater control enhances both developer and operations experiences.
  - Customizable request handling supports complex implementations.

- **Cons**:
  - Higher complexity and cost can strain QE resources.
  - QE has increased responsibility for observability (logging), maintenance and
    security.

<pre class="mermaid">
sequenceDiagram
  autonumber

  participant SCN
  participant QE
  participant Tech by Design
  participant Tech by Design_Database as Tech by Design Database
  participant DataLake as NYeC SHIN-NY Data Lake

  SCN->>QE: Sends FHIR JSON
  
  QE-->>Tech by Design: Forwards FHIR JSON

  Tech by Design->>Tech by Design: Validates JSON using NYeC SHIN-NY IG
  Tech by Design->>Tech by Design: Might filter or rewrite diagnostics if requested by NYeC
  Tech by Design->>Tech by Design_Database: Stores payload and diagnostics
  Tech by Design->>QE: Returns validation diagnostics
  QE-->>SCN: Forwards response
  SCN->>SCN: Takes any action they desire

  Tech by Design->>Tech by Design: Might transform JSON if requested by NYeC
  Tech by Design->>DataLake: POST FHIR JSON Data Lake (async)
  DataLake->>Tech by Design_Database: Stores Results (async)

  QE->>Tech by Design_Database: Queries Results whenever it desires (useful to find out the result of the data lake submission)
</pre>
