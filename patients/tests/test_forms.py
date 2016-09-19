from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

import csv, os

from patients.forms import PatientUploadFileForm
from communique.base_settings import BASE_DIR


class PatientUploadFileFormTestCase(TestCase):
    """
    Test cases for the form handling uploading patient information.
    """
    file_path = BASE_DIR + '/patients/tests/data/'

    def setUp(self):
        # set up files to be used in testing
        # the expected file format i.e the file is delimited with ';'
        with open(self.file_path + 'upload.csv', 'w', encoding='utf-8') as csvfile:
            fieldnames = ['patient_id', 'last_name', 'names', 'health_centre', 'dob', 'address', 'treatment_start_date',
                          'interim_outcome']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerow({'patient_id':'A001', 'last_name':'Snow', 'names':'Jon',
                             'health_centre':"St. Michael's Hospital", 'dob':'01/01/2001', 'address':'Long Street',
                             'treatment_start_date':'01/01/2001', 'interim_outcome':'Clinic treatment' })

    def tearDown(self):
        # delete the created files
        os.remove(self.file_path + 'upload.csv')

    def test_validation(self):
        """
        Tests that validation is carried out to ensure that the expected columns are provided to be parsed
        """
        form = PatientUploadFileForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

        with open(self.file_path + 'upload.csv', 'rb') as csvfile:
            file_data = {'uploaded_file': SimpleUploadedFile('upload.csv', csvfile.read(), content_type='text/plain')}

        form = PatientUploadFileForm({}, file_data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())
