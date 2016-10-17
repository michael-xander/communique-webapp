import csv


def write_admissions_to_csv(given_file, admissions_list, date_format, date_format_str):
    """
    A function that writes a list of admissions to a given file
    :param given_file: The file to which the admissions are written to
    :param admissions_list: The list of admissions to write to file
    :param date_format: The format in which dates should be written to file
    :param date_format_str: The string representation of the date format e.g dd-mm-yyyy
    """
    fieldnames = ['id', 'patient_id', 'admission_date ({0})'.format(date_format_str),
                  'discharge_date ({0})'.format(date_format_str), 'health_centre', 'notes', 'created_by',
                  'date_created ({0})'.format(date_format_str), 'last_modified_by',
                  'date_last_modified ({0})'.format(date_format_str)]
    writer = csv.DictWriter(given_file, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()

    for admission in admissions_list:
        patient = admission.patient

        # check if the admission has a discharge date
        if admission.discharge_date:
            discharge_date = admission.discharge_date.strftime(date_format)
        else:
            discharge_date = ''

        writer.writerow({fieldnames[0]:admission.id, fieldnames[1]:patient.identifier,
                         fieldnames[2]:admission.admission_date.strftime(date_format), fieldnames[3]:discharge_date,
                         fieldnames[4]:admission.health_centre, fieldnames[5]:admission.notes,
                         fieldnames[6]:admission.created_by, fieldnames[7]:admission.date_created.strftime(date_format),
                         fieldnames[8]:admission.last_modified_by,
                         fieldnames[9]:admission.date_last_modified.strftime(date_format)})
