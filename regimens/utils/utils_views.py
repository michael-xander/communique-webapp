import csv


def write_regimens_to_csv(given_file, regimens_list, date_format, date_format_str):
    """
    A function that writes a list of regimens to a given file
    :param given_file: The file to which the regimens are written to
    :param regimens_list: The list of regimens to write to file
    :param date_format: The format in which dates should be written to file
    :param date_format_str: The string representation of the date format e.g dd-mm-yyyy
    """
    fieldnames = ['id', 'patient_id', 'drugs', 'notes', 'date_started ({0})'.format(date_format_str),
                  'date_ended ({0})'.format(date_format_str), 'date_created ({0})'.format(date_format_str), 'created_by',
                  'date_last_modified ({0})'.format(date_format_str), 'last_modified_by']
    writer = csv.DictWriter(given_file, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()

    for regimen in regimens_list:
        drugs = ''
        for drug in regimen.drugs.all():
            if drugs == '':
                drugs = '{0}'.format(drug)
            else:
                drugs = '{0}, {1}'.format(drugs, drug)

        writer.writerow({fieldnames[0]:regimen.id, fieldnames[1]:regimen.patient.identifier, fieldnames[2]:drugs,
                         fieldnames[3]:regimen.notes, fieldnames[4]:regimen.date_started.strftime(date_format),
                         fieldnames[5]:regimen.date_ended.strftime(date_format),
                         fieldnames[6]:regimen.date_created.strftime(date_format), fieldnames[7]:regimen.created_by,
                         fieldnames[8]:regimen.date_last_modified.strftime(date_format),
                         fieldnames[9]:regimen.last_modified_by})