import csv


def write_appointments_to_csv(given_file, appointment_list, date_format, date_format_str):
    """
    A function that writes a list of appointments to a given file
    :param given_file: The file to which the appointments will be written
    :param appointment_list: The list of appointments to write to file
    :param date_format: The format in which dates should be written to file
    :param date_format_str: The string representation of the date format e.g dd-mm-yyyy
    """

    fieldnames = ['id', 'patient_id', 'title', 'notes', 'owner', 'appointment_date ({0})'.format(date_format_str),
                  'start_time', 'end_time', 'created_by', 'date_created ({0})'.format(date_format_str), 'modified_by',
                  'date_last_modified_by ({0})'.format(date_format_str)]
    writer = csv.DictWriter(given_file, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()

    for appointment in appointment_list:
        patient = appointment.patient
        owner = appointment.owner

        # only export appointments that have been assigned to a patient
        if patient:
            writer.writerow({fieldnames[0]:appointment.id, fieldnames[1]:patient.identifier,
                             fieldnames[2]:appointment.title, fieldnames[3]:appointment.notes, fieldnames[4]:owner,
                             fieldnames[5]:appointment.appointment_date.strftime(date_format),
                             fieldnames[6]:appointment.start_time, fieldnames[7]:appointment.end_time,
                             fieldnames[8]:appointment.created_by,
                             fieldnames[9]:appointment.date_created.strftime(date_format),
                             fieldnames[10]:appointment.last_modified_by,
                             fieldnames[11]:appointment.date_last_modified.strftime(date_format)})
