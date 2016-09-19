from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

import csv, os

from patients.forms import PatientUploadFileForm
from patients.models import Patient

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
            fieldnames = ['patient_id', 'last_name', 'names', 'health_centre', 'dob', 'address', 'treatment_start_date',
                          'interim_outcome']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerow({'patient_id':'A001', 'last_name':'Snow', 'names':'Jon',
                             'health_centre':"St. Michael's Hospital", 'dob':'01/01/2001', 'address':'Long Street',
                             'treatment_start_date':'01/01/2001', 'interim_outcome':'Clinic treatment' })

        # a file with a missing column
        with open(self.test_files[1], 'w', encoding='utf-8') as csvfile:
            fieldnames = ['patient_id', 'last_name', 'names', 'health_centre', 'dob', 'address', 'treatment_start_date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()

            writer.writerow({'patient_id': 'A001', 'last_name': 'Snow', 'names': 'Jon',
                             'health_centre': "St. Michael's Hospital", 'dob': '01/01/2001', 'address': 'Long Street',
                             'treatment_start_date': '01/01/2001'})

        # a file with switched columns
        with open(self.test_files[2], 'w', encoding='utf-8') as csvfile:
            fieldnames = ['last_name', 'patient_id', 'names', 'health_centre', 'dob', 'address', 'treatment_start_date',
                          'interim_outcome']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()

            writer.writerow({'patient_id': 'A001', 'last_name': 'Snow', 'names': 'Jon',
                            'health_centre': "St. Michael's Hospital", 'dob': '01/01/2001', 'address': 'Long Street',
                            'treatment_start_date': '01/01/2001'})

        # a file with one of the required fields missing
        with open(self.test_files[3], 'w', encoding='utf-8') as csvfile:
            fieldnames = ['patient_id', 'last_name', 'names', 'health_centre', 'dob', 'address', 'treatment_start_date',
                          'interim_outcome']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()

            writer.writerow({'last_name': 'Snow', 'names': 'Jon','health_centre': "St. Michael's Hospital",
                             'dob': '01/01/2001', 'address': 'Long Street','treatment_start_date': '01/01/2001'})

        Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE, identifier='A002')

        # a file containing an ID for an existing patient
        with open(self.test_files[4], 'w', encoding='utf-8') as csvfile:
            fieldnames = ['patient_id', 'last_name', 'names', 'health_centre', 'dob', 'address', 'treatment_start_date',
                          'interim_outcome']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerow({'patient_id': 'A002', 'last_name': 'Snow', 'names': 'Jon',
                             'health_centre': "St. Michael's Hospital", 'dob': '01/01/2001', 'address': 'Long Street',
                             'treatment_start_date': '01/01/2001', 'interim_outcome': 'Clinic treatment'})

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
