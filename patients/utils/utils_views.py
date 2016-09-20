import csv
from io import StringIO
import datetime

from patients.models import Patient
from .utils_forms import *


def get_patient_sex(value_str):
    """
    Returns the patient sex value of the provided string
    :param value_str: The description of the sex i.e male/female or Male/Female
    :return: The patient sex value i.e M/F or none if provided string is neither male or female
    """
    value = value_str.strip().lower()

    if value == 'male':
        sex = Patient.MALE
    elif value == 'female':
        sex = Patient.FEMALE
    else:
        sex = None
    return sex


def get_date(date_str, date_format):
    """
    Create a date object from the a date string and specified format
    :param date_str: The date as a string
    :param date_format: The date format the string is in
    :return: The date as an object
    """
    return datetime.datetime.strptime(date_str, date_format).date()


def import_patients_from_file(import_file, user):
    """
    A function that creates patients from a file provided
    :param import_file: The file containing the patient details. This file would have been read in binary format.
    :param user: The user providing the file
    """
    csvf = StringIO(import_file.read().decode())
    reader = csv.DictReader(csvf, delimiter=';')

    patient_list = []
    # create patients from data in the rows:
    for row in reader:
        patient = Patient()
        for column in ORDERED_UPLOAD_COLUMNS:
            # if the value of this column is filled in
            column_value = row[column].strip()
            if column_value:
                if column == PATIENT_ID_UPLOAD_COLUMN:
                    patient.identifier = column_value
                elif column == LAST_NAME_UPLOAD_COLUMN:
                    patient.last_name = column_value
                elif column == OTHER_NAMES_UPLOAD_COLUMN:
                    patient.other_names = column_value
                elif column == HEALTH_CENTRE_UPLOAD_COLUMN:
                    patient.reference_health_centre = column_value
                elif column == DOB_UPLOAD_COLUMN:
                    patient.birth_date = get_date(column_value, "%Y/%m/%d")
                elif column == SEX_UPLOAD_COLUMN:
                    patient.sex = get_patient_sex(column_value)
                elif column == ADDRESS_UPLOAD_COLUMN:
                    patient.location = column_value
                elif column == TREATMENT_START_DATE_UPLOAD_COLUMN:
                    patient.treatment_start_date = get_date(column_value, "%Y/%m/%d")
                elif column == INTERIM_OUTCOME_UPLOAD_COLUMN:
                    patient.interim_outcome = column_value

        patient.created_by = user
        patient.last_modified_by = user
        patient_list.append(patient)

    Patient.objects.bulk_create(patient_list)



