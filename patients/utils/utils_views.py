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


def write_enrollments_to_csv(given_file, enrollment_list, date_format):
    """
    A function that writes a list of enrollments to a given file
    :param given_file: The file to which the enrollments are written
    :param enrollment_list: The list of enrollments to write to file
    :param date_format: The format in which dates should be written to file
    """
    fieldnames = ['id', 'program', 'program_id', 'patient_id', 'date_enrolled (dd-mm-yyyy)', 'comment',
                  'date_created (dd-mm-yyyy)', 'created_by', 'date_last_modified (dd-mm-yyyy)', 'modified_by']
    writer = csv.DictWriter(given_file, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()

    for enrollment in enrollment_list:
        program = enrollment.program
        patient = enrollment.patient
        writer.writerow({'id':enrollment.id, 'program':program, 'program_id':program.id,
                         'patient_id':patient.identifier,
                         'date_enrolled (dd-mm-yyyy)':enrollment.date_enrolled.strftime(date_format),
                         'comment':enrollment.comment,
                         'date_created (dd-mm-yyyy)':enrollment.date_created.strftime(date_format),
                         'created_by':enrollment.created_by,
                         'date_last_modified (dd-mm-yyyy)':enrollment.date_last_modified.strftime(date_format),
                         'modified_by':enrollment.last_modified_by})


def write_outcomes_to_csv(given_file, outcome_list, date_format):
    """
    A function that writes a list of patient outcomes to a given file
    :param given_file: The file to which the outcomes are writtern
    :param outcome_list: The list of enrollments to write to file
    :param date_format: The format in which dates should be written to file
    """
    fieldnames = ['id', 'outcome_type', 'outcome_type_id', 'patient_id', 'outcome_date (dd-mm-yyyy)', 'notes',
                  'date_created (dd-mm-yyyy)', 'created_by', 'date_last_modified (dd-mm-yyyy)', 'modified_by']
    writer = csv.DictWriter(given_file, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()

    for outcome in outcome_list:
        patient = outcome.patient
        outcome_type = outcome.outcome_type
        writer.writerow({'id':outcome.id, 'outcome_type':outcome_type, 'outcome_type_id':outcome_type.id,
                         'patient_id':patient.identifier,
                         'outcome_date (dd-mm-yyyy)':outcome.outcome_date.strftime(date_format), 'notes':outcome.notes,
                         'date_created (dd-mm-yyyy)':outcome.date_created.strftime(date_format),
                         'created_by':outcome.created_by,
                         'date_last_modified (dd-mm-yyyy)':outcome.date_last_modified.strftime(date_format),
                         'modified_by':outcome.last_modified_by})


