from frictionless import Package

# Define your schema
schema = {
  "name": "my-dataset",
  "resources": [
    {
      "name": "qe_admin_data",
      "path": "data/QE_ADMIN_DATA_qcs-test-20240603-testcase4.csv",
      "schema": {
        "fields": [
          {"name": "PAT_MRN_ID", "type": "string", "constraints": {"required": True}},
          {"name": "FACILITY_ID", "type": "string", "constraints": {"required": True}},
          {"name": "FACILITY_LONG_NAME", "type": "string", "constraints": {"required": True, "pattern": "^[a-zA-Z\\s]+$"}},
          {"name": "ORGANIZATION_TYPE", "type": "string", "constraints": {"required": True, "enum":["prov","dept","team","govt","ins","pay","edu","reli","crs","cg","bus","other","laboratory","imaging","pharmacy","health-information-network","health-data-aggregator"]}},
          {"name": "FACILITY_ADDRESS1", "type": "string", "constraints": {"required": True}},
          {"name": "FACILITY_ADDRESS2", "type": "string"},
          {"name": "FACILITY_CITY", "type": "string"},
          {"name": "FACILITY_STATE", "type": "string", "constraints": {"enum":["FACILITY_STATE", "NY", "New York"]}},
          {"name": "FACILITY_ZIP", "type": "string", "constraints": {"required": True}},
          {"name": "VISIT_PART_2_FLAG", "type": "string", "constraints": {"required": True, "enum":["Yes", "No"]}},
          {"name": "VISIT_OMH_FLAG", "type": "string", "constraints": {"required": True, "enum":["Yes", "No"]}},
          {"name": "VISIT_OPWDD_FLAG", "type": "string", "constraints": {"required": True, "enum":["Yes", "No"]}}
        ],
        "primaryKey": ["PAT_MRN_ID"]
      },
      "dialect": {
        "delimiter": "|"
      }
    },
    {
      "name": "screening_data",
      "path": "data/SCREENING_qcs-test-20240603-testcase4.csv",
      "schema": {
        "fields": [
          {"name": "PAT_MRN_ID", "type": "string", "constraints": {"required": True}},
          {"name": "FACILITY_ID", "type": "string", "constraints": {"required": True}},
          {"name": "ENCOUNTER_ID", "type": "string"},
          {"name": "ENCOUNTER_CLASS_CODE", "type": "string", "constraints": {"required": True}},
          {"name": "ENCOUNTER_CLASS_CODE_DESCRIPTION", "type": "string"},
          {"name": "ENCOUNTER_CLASS_CODE_SYSTEM", "type": "string", "constraints": {"required": True, "enum": ["http://terminology.hl7.org/CodeSystem/v3-ActCode"]}},
          {"name": "ENCOUNTER_STATUS_CODE", "type": "string", "constraints": {"required": True}},
          {"name": "ENCOUNTER_STATUS_CODE_DESCRIPTION", "type": "string"},
          {"name": "ENCOUNTER_STATUS_CODE_SYSTEM", "type": "string", "constraints": {"required": True, "enum": ["http://hl7.org/fhir/encounter-status"]}},
          {"name": "ENCOUNTER_TYPE_CODE", "type": "string"},
          {"name": "ENCOUNTER_TYPE_CODE_DESCRIPTION", "type": "string"},
          {"name": "ENCOUNTER_TYPE_CODE_SYSTEM", "type": "string", "constraints": {"enum": ["SNOMED-CT", "snomed-ct", "Snomed-ct", "SNOMED", "snomed", "Snomed", "http://snomed.info/sct"]} },
          {"name": "SCREENING_STATUS_CODE", "type": "string", "constraints": {"required": True}},
          {"name": "SCREENING_STATUS_CODE_DESCRIPTION", "type": "string"},
          {"name": "SCREENING_STATUS_CODE_SYSTEM", "type": "string", "constraints": {"required": True, "enum": ["http://hl7.org/fhir/observation-status"]}},
          {"name": "SCREENING_CODE", "type": "string", "constraints": {"required": True, "enum": ["96777-8", "97023-6"]}},
          {"name": "SCREENING_CODE_DESCRIPTION", "type": "string", "constraints": {"required": True, "enum": ["Accountable health communities (AHC) health-related social needs (HRSN) supplemental questions","accountable health communities (AHC) health-related social needs (HRSN) supplemental questions","Accountable health communities (AHC) health-related social needs screening (HRSN) tool","accountable health communities (AHC) health-related social needs screening (HRSN) tool","NYS AHC HRSN screening"]}},
          {"name": "SCREENING_CODE_SYSTEM_NAME", "type": "string", "constraints": {"required": True, "enum": ["LN", "ln", "LOINC", "loinc", "http://loinc.org", "NYS standard","NYS Standard"]}},
          {"name": "RECORDED_TIME", "type": "datetime", "constraints": {"required": True}},
          {"name": "QUESTION_CODE", "type": "string", "constraints": {"required": True}},
          {"name": "QUESTION_CODE_DESCRIPTION", "type": "string", "constraints": {"required": True}},
          {"name": "QUESTION_CODE_SYSTEM_NAME", "type": "string", "constraints": {"required": True, "enum": ["LN","LOINC","http://loinc.org"]}},
          {"name": "UCUM_UNITS", "type": "string"},
          {"name": "SDOH_DOMAIN", "type": "string", "constraints": {"required": True}},
          {"name": "PARENT_QUESTION_CODE", "type": "string"},
          {"name": "ANSWER_CODE", "type": "string", "constraints": {"required": True}},
          {"name": "ANSWER_CODE_DESCRIPTION", "type": "string", "constraints": {"required": True}},
          {"name": "ANSWER_CODE_SYSTEM_NAME", "type": "string", "constraints": {"required": True, "enum": ["LN","LOINC","http://loinc.org"]}},
          {"name": "POTENTIAL_NEED_INDICATED", "type": "string", "constraints": {"required": True, "enum": ["Yes","No","NA","yes","no","na"]}}
        ],
        "foreignKeys": [
          {
            "fields": ["PAT_MRN_ID"],
            "reference": {
              "resource": "qe_admin_data",
              "fields": ["PAT_MRN_ID"]
            }
          }
        ]
      },
      "dialect": {
        "delimiter": "|"
      }
    },
    {
      "name": "demographic_data",
      "path": "data/DEMOGRAPHIC_DATA_qcs-test-20240603-testcase4.csv",
      "schema": {
        "fields": [
          {"name": "MPI_ID", "type": "string", "constraints": {"required": True}},
          {"name": "PAT_MRN_ID", "type": "string", "constraints": {"required": True}},
          {"name": "FACILITY_ID", "type": "string", "constraints": {"required": True}},
          {"name": "CONSENT", "type": "string", "constraints": {"required": True, "enum": ["Yes", "YES", "yes", "Y", "y", "No", "NO", "no","N", "n","Unknown", "UNKNOWN", "unknown","UNK", "Unk", "unk"]}},
          {"name": "FIRST_NAME", "type": "string", "constraints": {"required": True, "pattern":"^[A-Za-z]+$"}},
          {"name": "MIDDLE_NAME", "type": "string", "constraints": {"pattern":"^[A-Za-z]+$"}},
          {"name": "LAST_NAME", "type": "string", "constraints": {"required": True, "pattern":"^[A-Za-z]+$"}},
          {"name": "ADMINISTRATIVE_SEX_CODE", "type": "string", "constraints": {"required": True}},
          {"name": "ADMINISTRATIVE_SEX_CODE_DESCRIPTION", "type": "string"},
          {"name": "ADMINISTRATIVE_SEX_CODE_SYSTEM", "type": "string", "constraints": {"required": True}},
          {"name": "SEX_AT_BIRTH_CODE", "type": "string", "constraints": {"required": True}},
          {"name": "SEX_AT_BIRTH_CODE_DESCRIPTION", "type": "string"},
          {"name": "SEX_AT_BIRTH_CODE_SYSTEM", "type": "string"},
          {"name": "PAT_BIRTH_DATE", "type": "date"},
          {"name": "ADDRESS1", "type": "string"},
          {"name": "ADDRESS2", "type": "string"},
          {"name": "CITY", "type": "string", "constraints": {"required": True}},
          {"name": "STATE", "type": "string", "constraints": {"required": True, "enum":["NY", "ny", "New York","new york", "NEW YORK"]}},
          {"name": "ZIP", "type": "string", "constraints": {"required": True, "pattern": "^\\d{5}(\\d{4})?$"}},
          {"name": "PHONE", "type": "string"},
          {"name": "SSN", "type": "string"},        
          {"name": "GENDER_IDENTITY_CODE", "type": "string"},
          {"name": "GENDER_IDENTITY_CODE_DESCRIPTION", "type": "string"},
          {"name": "GENDER_IDENTITY_CODE_SYSTEM_NAME", "type": "string", "constraints": {"required": True, "enum":["SNOMED-CT","SNOMED","http://snomed.info/sct"]}},
          {"name": "SEXUAL_ORIENTATION_CODE", "type": "string"},
          {"name": "SEXUAL_ORIENTATION_CODE_DESCRIPTION", "type": "string"},
          {"name": "SEXUAL_ORIENTATION_CODE_SYSTEM_NAME", "type": "string", "constraints": {"required": True, "enum":["SNOMED-CT","SNOMED","http://snomed.info/sct"]}},
          {"name": "PREFERRED_LANGUAGE_CODE", "type": "string"},
          {"name": "PREFERRED_LANGUAGE_CODE_DESCRIPTION", "type": "string"},
          {"name": "PREFERRED_LANGUAGE_CODE_SYSTEM_NAME", "type": "string", "constraints": {"required": True, "enum":["ISO","ISO 639-2","http://hl7.org/fhir/us/core/ValueSet/simple-language"]}},
          {"name": "RACE_CODE", "type": "string"},
          {"name": "RACE_CODE_DESCRIPTION", "type": "string"},
          {"name": "RACE_CODE_SYSTEM_NAME", "type": "string", "constraints": {"required": True, "enum":["CDC","CDCRE","urn:oid:2.16.840.1.113883.6.238"]}},
          {"name": "ETHNICITY_CODE", "type": "string"},
          {"name": "ETHNICITY_CODE_DESCRIPTION", "type": "string"},
          {"name": "ETHNICITY_CODE_SYSTEM_NAME", "type": "string", "constraints": {"required": True, "enum":["CDC","CDCRE","urn:oid:2.16.840.1.113883.6.238"]}},
          {"name": "MEDICAID_CIN", "type": "string", "constraints": {"pattern": "^[A-Za-z]{2}\\d{5}[A-Za-z]$"}}
        ],
        "foreignKeys": [
          {
            "fields": ["PAT_MRN_ID"],
            "reference": {
              "resource": "qe_admin_data",
              "fields": ["PAT_MRN_ID"]
            }
          }
        ]
      },
      "dialect": {
        "delimiter": "|"
      }
    }
  ]
}


# Create and validate the package
package = Package(schema)

# Validate the package
errors = package.validate()

# Check for validation errors
if errors:
    print("Schema validation errors:", errors)
else:
    print("Schema is valid!")
