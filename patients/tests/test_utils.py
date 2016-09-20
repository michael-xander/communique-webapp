from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

import csv, os

from communique.base_settings import BASE_DIR

from patients.utils.utils_views import *


class PatientsUtilsTestCase(TestCase):
    """
    Test cases for the util functions of the Patients app
    """
    file_path = BASE_DIR + '/patients/tests/data/'
    test_files = [
        file_path + 'patient-import.csv'
    ]

    def setUp(self):
        with open(self.test_files[0], 'w', encoding='utf-8') as csvfile:
            fieldnames = ORDERED_UPLOAD_COLUMNS
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerow({PATIENT_ID_UPLOAD_COLUMN:'A001', LAST_NAME_UPLOAD_COLUMN:'Snow',
                             OTHER_NAMES_UPLOAD_COLUMN:'Jon', HEALTH_CENTRE_UPLOAD_COLUMN:"St. Michael's Hospital",
                             DOB_UPLOAD_COLUMN:'2001/11/15', ADDRESS_UPLOAD_COLUMN:'Long Street',
                             SEX_UPLOAD_COLUMN:'Male',TREATMENT_START_DATE_UPLOAD_COLUMN:'2001/01/01',
                             INTERIM_OUTCOME_UPLOAD_COLUMN:'Clinic treatment' })

    def tearDown(self):
        # delete any created files
        for file_name in self.test_files:
            os.remove(file_name)

    def test_get_patient_sex(self):
        """
        Test case for the get_patient_sex function
        """
        self.assertEqual(Patient.MALE, get_patient_sex('male'))
        self.assertEqual(Patient.MALE, get_patient_sex('Male'))
        self.assertEqual(Patient.MALE, get_patient_sex('  MAle'))

        self.assertEqual(Patient.FEMALE, get_patient_sex('female'))
        self.assertEqual(Patient.FEMALE, get_patient_sex('Female'))
        self.assertEqual(Patient.FEMALE, get_patient_sex('   FEmalE'))

        self.assertEqual(None, get_patient_sex('umbrella'))

    def test_get_date(self):
        """
        Test case for the get_date function
        """
        date = datetime.date(2008, 3, 29)
        self.assertEqual(date, get_date('2008/03/29', "%Y/%m/%d"))

        self.assertEqual(date, get_date('29/03/2008', "%d/%m/%Y"))

    def test_import_patients_from_file(self):
        """
        Test case for the import_patients_from_file function
        """

        with open(self.test_files[0], 'rb') as csvfile:
            uploaded_file = SimpleUploadedFile('file.csv', csvfile.read(), content_type='text/plain')

        # Check that there aren't any patients in the database at the moment
        self.assertEqual(Patient.objects.count(), 0)

        user = User.objects.create_superuser(username='jon_snow', email='jonsnow@gmail.com', password='p@55words')

        import_patients_from_file(uploaded_file, user)

        self.assertEqual(Patient.objects.count(), 1)


