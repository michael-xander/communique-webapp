import csv


def write_sessions_to_csv(given_file, session_list, date_format, date_format_str):
    """
    A function that writes a list of counselling sessions to a given file
    :param given_file: The file to which the counselling sessions will be written
    :param session_list: The list of counselling sessions to write to file
    :param date_format: The format in which dates should be written to file
    :param date_format_str: The string representation of the date format string e.g dd-mm-yyyy
    """

    fieldnames = ['id', 'session_type', 'session_type_id', 'patient_id', 'notes', 'created_by',
                  'date_created ({0})'.format(date_format_str), 'modified_by',
                  'date_last_modified ({0})'.format(date_format_str)]
    writer = csv.DictWriter(given_file, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()

    for session in session_list:
        session_type = session.counselling_session_type
        patient = session.patient
        writer.writerow({fieldnames[0]:session.id, fieldnames[1]:session_type, fieldnames[2]:session_type.id,
                         fieldnames[3]:patient.identifier, fieldnames[4]:session.notes, fieldnames[5]:session.created_by,
                         fieldnames[6]:session.date_created.strftime(date_format),
                         fieldnames[7]:session.last_modified_by,
                         fieldnames[8]:session.date_last_modified.strftime(date_format)})