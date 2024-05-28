## File evaluation against various validators

* Validate the FHIR document on the [Legacy Public Inferno Site](https://inferno.healthit.gov/validator/) using SHIN-NY IG Version 0.4.0.
* Validate the FHIR document on the [Official Public Site](https://validator.fhir.org/) using SHIN-NY IG Version 0.4.0.
* Validate the FHIR document on the Official Local Docker Site using SHIN-NY IG Version 0.4.0.
* Validate the FHIR document on the [Custom 1115 FHIR Server](https://n9r2j0ii52.execute-api.ap-south-1.amazonaws.com/Prod/Bundle/$validate) using SHIN-NY IG Version 0.4.0.
  
### updates from SHIN-NY IG Version 0.3.0 and SHIN-NY IG Version 0.4.0

* Added more bundle constraints.
* bundle.total - max value is set to 1 from 0.
* bundle.link - max value is set to * from 0.
* bundle.entry.search - max value is set to 1 from 0.
* bundle.entry.request.method - changed to `POST` from `POST| DELETE`.
* bundle.entry.request.ifnonMatch - max value is set to 1 from 0.
* bundle.entry.request.ifMatch - max value is set to 1 from 0.
* bundle.entry.request.ifNoneExit - max value is set to 1 from 0.
* bundle.entry.response.location - max value is set to 1 from 0.
* bundle.entry.response.etag  - max value is set to 1 from 0.
* bundle.signature  -  max value is set to 1 from 0.
* bundle.entry.responselastModified - max value is set to 1 from 0.
  