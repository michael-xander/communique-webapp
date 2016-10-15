import csv


def write_adverse_events_to_csv(given_file, events_list, date_format, date_format_str):
    """
    A function that writes a list of adverse events to a given file
    :param given_file: The file to which the adverse events will be writter
    :param events_list: The list of adverse events to be written to file
    :param date_format: The format in which dates should be written to file
    :param date_format_str: The string representation of the date format e.g dd-mm-yyyy
    """

    fieldnames = ['id', 'patient_id', 'adverse_event_type', 'adverse_event_type_id',
                  'event_date ({0})'.format(date_format_str), 'notes', 'date_created ({0})'.format(date_format_str),
                  'created_by', 'date_last_modified ({0})'.format(date_format_str), 'last_modified_by']
    writer = csv.DictWriter(given_file ,fieldnames=fieldnames, delimiter=';')
    writer.writeheader()

    for event in events_list:
        event_type = event.adverse_event_type
        patient = event.patient
        writer.writerow({fieldnames[0]:event.id, fieldnames[1]:patient.identifier, fieldnames[2]:event_type,
                         fieldnames[3]:event_type.id, fieldnames[4]:event.event_date.strftime(date_format),
                         fieldnames[5]:event.notes, fieldnames[6]:event.date_created.strftime(date_format),
                         fieldnames[7]:event.created_by, fieldnames[8]:event.date_last_modified.strftime(date_format),
                         fieldnames[9]:event.last_modified_by})
