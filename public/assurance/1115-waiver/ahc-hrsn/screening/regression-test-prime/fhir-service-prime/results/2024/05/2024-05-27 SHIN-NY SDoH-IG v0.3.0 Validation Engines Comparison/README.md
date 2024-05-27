## File evaluation against various validators

* Validate against legacy public inferno site SHIN-NY IG Version 4.0 (Local Instance).
* Validate against new official public site SHIN-NY IG Version 4.0 (Local Instance).
* Validate against new official local docker site SHIN-NY IG Version 4.0 (Local Instance).
* Validate against custom 1115 FHIR server  SHIN-NY IG Version 4.0 (Local Instance).

### updates from SHIN-NY IG Version 3.0 and SHIN-NY IG Version 4.0(draft)

* Added Bundle more constraints.
* bundle.total - max value is set to 1 from 0.
* bundle.link - max value is set to * from 0.
* bundle.entry.search - max value is set to 1 from 0.
* bundle.entry.request.method - changed to `POST` from `POST| DELETE`.
* bundle.entry.request.ifnonMatch - max value is set to 1 from 0.
* bundle.entry.request.ifMatch - max value is set to 1 from 0.
* bundle.entry.request.ifNoneExit - max value is set to 1 from 0.
* bundle.entry.response.location - max value is set to 1 from 0.
* bundle.entry.response.etag  - max value is set to 1 from 0.
* bundle.signature  -  value is set to 1 from 0.
* bundle.entry.responselastModified - max value is set to 1 from 0.