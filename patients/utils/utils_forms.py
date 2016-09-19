# the column names for the patient upload file
PATIENT_ID_UPLOAD_COLUMN = 'patient_id'
LAST_NAME_UPLOAD_COLUMN = 'last_name'
OTHER_NAMES_UPLOAD_COLUMN = 'names'
HEALTH_CENTRE_UPLOAD_COLUMN = 'health_centre'
DOB_UPLOAD_COLUMN = 'dob'
SEX_UPLOAD_COLUMN = 'sex'
ADDRESS_UPLOAD_COLUMN = 'address'
TREATMENT_START_DATE_UPLOAD_COLUMN = 'treatment_start_date'
INTERIM_OUTCOME_UPLOAD_COLUMN = 'interim_outcome'

# the columns in their expected order
ORDERED_UPLOAD_COLUMNS = [PATIENT_ID_UPLOAD_COLUMN, LAST_NAME_UPLOAD_COLUMN, OTHER_NAMES_UPLOAD_COLUMN,
                          HEALTH_CENTRE_UPLOAD_COLUMN, DOB_UPLOAD_COLUMN, SEX_UPLOAD_COLUMN, ADDRESS_UPLOAD_COLUMN,
                          TREATMENT_START_DATE_UPLOAD_COLUMN, INTERIM_OUTCOME_UPLOAD_COLUMN]