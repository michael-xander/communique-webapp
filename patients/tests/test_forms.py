from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

import csv, os

from patients.forms import PatientUploadFileForm
from patients.models import Patient
from patients.utils.utils_forms import *

from communique.base_settings import BASE_DIR


class PatientUploadFileFormTestCase(TestCase):
    """
    Test cases for the form handling uploading patient information.
    """
    file_path = BASE_DIR + '/patients/tests/data/'
    test_files = [
        file_path + 'correct.csv',
        file_path + 'missing-column.csv',
        file_path + 'switched-columns.csv',
        file_path + 'missing-field.csv',
        file_path + 'existing-patient.csv'
    ]

    def setUp(self):
        # set up files to be used in testing
        # the expected file format i.e the file is delimited with ';'
        with open(self.test_files[0], 'w', encoding='utf-8') as csvfile:
            fieldnames = ORDERED_UPLOAD_COLUMNS
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerow({PATIENT_ID_UPLOAD_COLUMN:'A001', LAST_NAME_UPLOAD_COLUMN:'Snow',
                             OTHER_NAMES_UPLOAD_COLUMN:'Jon', HEALTH_CENTRE_UPLOAD_COLUMN:"St. Michael's Hospital",
                             DOB_UPLOAD_COLUMN:'01/01/2001', ADDRESS_UPLOAD_COLUMN:'Long Street',
                             SEX_UPLOAD_COLUMN:'Male',TREATMENT_START_DATE_UPLOAD_COLUMN:'01/01/2001',
                             INTERIM_OUTCOME_UPLOAD_COLUMN:'Clinic treatment' })

        # a file with a missing column
        with open(self.test_files[1], 'w', encoding='utf-8') as csvfile:
            fieldnames = [PATIENT_ID_UPLOAD_COLUMN, LAST_NAME_UPLOAD_COLUMN, OTHER_NAMES_UPLOAD_COLUMN,
                          HEALTH_CENTRE_UPLOAD_COLUMN, DOB_UPLOAD_COLUMN, ADDRESS_UPLOAD_COLUMN,
                          TREATMENT_START_DATE_UPLOAD_COLUMN, INTERIM_OUTCOME_UPLOAD_COLUMN]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()

            writer.writerow({PATIENT_ID_UPLOAD_COLUMN: 'A001', LAST_NAME_UPLOAD_COLUMN: 'Snow',
                             OTHER_NAMES_UPLOAD_COLUMN: 'Jon', HEALTH_CENTRE_UPLOAD_COLUMN: "St. Michael's Hospital",
                             DOB_UPLOAD_COLUMN: '01/01/2001', ADDRESS_UPLOAD_COLUMN: 'Long Street',
                             TREATMENT_START_DATE_UPLOAD_COLUMN: '01/01/2001', INTERIM_OUTCOME_UPLOAD_COLUMN:'Clinic treatment'})

        # a file with switched columns
        with open(self.test_files[2], 'w', encoding='utf-8') as csvfile:
            fieldnames = [LAST_NAME_UPLOAD_COLUMN, PATIENT_ID_UPLOAD_COLUMN, OTHER_NAMES_UPLOAD_COLUMN,
                          HEALTH_CENTRE_UPLOAD_COLUMN, DOB_UPLOAD_COLUMN, SEX_UPLOAD_COLUMN, ADDRESS_UPLOAD_COLUMN,
                          TREATMENT_START_DATE_UPLOAD_COLUMN, INTERIM_OUTCOME_UPLOAD_COLUMN]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()

            writer.writerow({PATIENT_ID_UPLOAD_COLUMN: 'A001', LAST_NAME_UPLOAD_COLUMN: 'Snow',
                             OTHER_NAMES_UPLOAD_COLUMN: 'Jon', HEALTH_CENTRE_UPLOAD_COLUMN: "St. Michael's Hospital",
                             DOB_UPLOAD_COLUMN: '01/01/2001', ADDRESS_UPLOAD_COLUMN: 'Long Street',
                             SEX_UPLOAD_COLUMN: 'Male', TREATMENT_START_DATE_UPLOAD_COLUMN: '01/01/2001',
                             INTERIM_OUTCOME_UPLOAD_COLUMN: 'Clinic treatment'})

        # a file with one of the required fields missing
        with open(self.test_files[3], 'w', encoding='utf-8') as csvfile:
            fieldnames = ORDERED_UPLOAD_COLUMNS
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()

            writer.writerow({LAST_NAME_UPLOAD_COLUMN: 'Snow', OTHER_NAMES_UPLOAD_COLUMN: 'Jon',
                             HEALTH_CENTRE_UPLOAD_COLUMN: "St. Michael's Hospital", DOB_UPLOAD_COLUMN: '01/01/2001',
                             ADDRESS_UPLOAD_COLUMN: 'Long Street', SEX_UPLOAD_COLUMN: 'Male',
                             TREATMENT_START_DATE_UPLOAD_COLUMN: '01/01/2001',
                             INTERIM_OUTCOME_UPLOAD_COLUMN: 'Clinic treatment'})

        Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE, identifier='A002')

        # a file containing an ID for an existing patient
        with open(self.test_files[4], 'w', encoding='utf-8') as csvfile:
            fieldnames = ORDERED_UPLOAD_COLUMNS
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()

            writer.writerow({PATIENT_ID_UPLOAD_COLUMN: 'A002', LAST_NAME_UPLOAD_COLUMN: 'Snow',
                             OTHER_NAMES_UPLOAD_COLUMN: 'Jon', HEALTH_CENTRE_UPLOAD_COLUMN: "St. Michael's Hospital",
                             DOB_UPLOAD_COLUMN: '01/01/2001', ADDRESS_UPLOAD_COLUMN: 'Long Street',
                             SEX_UPLOAD_COLUMN: 'Male', TREATMENT_START_DATE_UPLOAD_COLUMN: '01/01/2001',
                             INTERIM_OUTCOME_UPLOAD_COLUMN: 'Clinic treatment'})

    def tearDown(self):
        # delete the created files
        for file_name in self.test_files:
            os.remove(file_name)

    def test_validation(self):
        """
        Tests that validation is carried out to ensure that the expected columns are provided to be parsed
        """
        form = PatientUploadFileForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

        with open(self.test_files[0], 'rb') as csvfile:
            file_data = {'uploaded_file': SimpleUploadedFile('file.csv', csvfile.read(), content_type='text/plain')}

        form = PatientUploadFileForm({}, file_data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

        with open(self.test_files[1], 'rb') as csvfile:
            file_data = {'uploaded_file':SimpleUploadedFile('file.csv', csvfile.read(),
                                                            content_type='text/plain')}

        form = PatientUploadFileForm({}, file_data)
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())

        with open(self.test_files[2], 'rb') as csvfile:
            file_data = {'uploaded_file': SimpleUploadedFile('file.csv', csvfile.read(),
                                                             content_type='text/plain')}

        form = PatientUploadFileForm({}, file_data)
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())

        with open(self.test_files[3], 'rb') as csvfile:
            file_data = {'uploaded_file': SimpleUploadedFile('file.csv', csvfile.read(),
                                                             content_type='text/plain')}

        form = PatientUploadFileForm({}, file_data)
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())

        with open(self.test_files[4], 'rb') as csvfile:
            file_data = {'uploaded_file': SimpleUploadedFile('file.csv', csvfile.read(),
                                                             content_type='text/plain')}

        form = PatientUploadFileForm({}, file_data)
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())
