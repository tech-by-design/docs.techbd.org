---
title: Overview
---

**Tech By Design** serves as a comprehensive service portal that offers a user-friendly interface for reviewing, tracking, and analyzing FHIR submissions. It supports Submitting Clinical Networks (SCNs) and Quality Entities (QEs) by facilitating issue resolution and communication.

Tech by Design provides an HTTP API interface for accepting FHIR bundles, validating them according to the SHIN-NY Implementation Guide (IG), and sending the validated FHIR bundles to the data lake for submission. The application allows users to review interactions and monitor various metrics for each submission, offering a detailed view of the submission process. 

Tech by Design Hub acts as a tool for analyzing data quality, troubleshooting, and performance tracking. It is a multi-tenant web application designed to streamline access and management of various health information exchange activities for the Qualified Entities (QEs) in New York. This platform serves as a central hub for NYeC and QE executives and staff members to log in and access dashboards, interactions, diagnostics, documentation, support, and profile management.

#### Tech by Design Portal URLs
- **Development**: [https://synthetic.fhir.api.devl.techbd.org/](https://synthetic.fhir.api.devl.techbd.org/)
- **Staging**: [https://synthetic.fhir.api.stage.techbd.org/](https://synthetic.fhir.api.stage.techbd.org/)

---

#### Objectives

1. **Unified Dashboard**: Provide a comprehensive dashboard summarizing recent activities across the organization when a specific QE logs in or summarizing across QEs when NYeC or Tech by Design staff login (“super users”).
2. **Interaction Management**: Display detailed summaries and grid views of network interactions, starting with SFTP and HTTP protocols.
3. **Diagnostics and Validation**: Offer detailed insights into the validation and processing of various file types. The output from `orchctl.ts` and FHIR validation engines is the starting point.
4. **Documentation Access**: Centralize developer and end-user documentation, including API endpoints and Swagger UI.
5. **Support and Feedback**: Facilitate access to FAQs and support ticket submission.
6. **Profile Management**: Enable users to manage their personal and organizational accounts.

---

#### Target Audience
- Tech by Design senior executives and staff
- NYeC senior executives and staff
- QE executives and staff members
- **Future**: QE downstream partners? We should design our system for a “closed ecosystem” between NY DoH, NYeC, QEs, and Tech by Design for now but keep in mind that downstream partners might be allowed in as well.

---

#### Tech Stack

- **Backend**: Java 21 (moving to Java 22 ASAP, staying up to date regularly) with all modern Java features, Spring Boot 3.3 (staying up to date regularly), annotation-driven configuration (no XML, no JSON, limited YAML only when required).
- **Frontend**: HTML5 and minimal JavaScript via Thymeleaf, advanced JavaScript via HTMx, Tailwind CSS for styling and UX.
- **Database**: PostgreSQL 16 with JSONB core and numerous extensions on AWS RDS.
- **API**: RESTful for external integration, HATEOAS for internal web app use, auto-generated Swagger UI for all documentation.
- **File Management**: Apache Commons VFS.
- **Security**: CAS with GitHub integration, and later NYeC / QEs’ Azure AD with Role-based access control (RBAC).
