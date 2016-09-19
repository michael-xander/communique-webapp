from django import forms

import csv
from io import StringIO

from appointments.models import Appointment
from appointments.forms import AppointmentForm

from patients.models import Patient


class PatientAppointmentForm(AppointmentForm):
    """
    A form used to create an appointment for a patient.
    """
    class Meta(AppointmentForm.Meta):
        model = Appointment
        fields = ['title', 'owner', 'appointment_date', 'start_time', 'end_time', 'notes']


class PatientUploadFileForm(forms.Form):
    """
    A form that handles uploading a csv file of patient information
    """
    uploaded_file = forms.FileField(label='Patient data file')

    def clean(self):
        # validate the required fields are available in the provided file
        uploaded_file = self.cleaned_data.get('uploaded_file')

        if uploaded_file:
            csvf = StringIO(uploaded_file.read().decode())
            reader = csv.reader(csvf, delimiter=';')
            row_count = 0
            # iterate through the rows making sure that the required fields are available and the columns in the
            # expected order
            for row in reader:
                # the first row that contains the column names
                if row_count == 0:
                    if len(row) != 8:
                        raise forms.ValidationError('The right number of columns has not been provided', code='invalid')
                    # check that the columns are in their expected orders i.e
                    # patient_id, last_name, names, health_centre, dob, address, treatment_start_date, interim_outcome
                    if (row[0] != 'patient_id' or row[1] != 'last_name' or row[2] != 'names' or row[3] != 'health_centre'
                        or row[4] != 'dob' or row[5] != 'address' or row[6] != 'treatment_start_date' or
                                row[7] != 'interim_outcome'):
                        raise forms.ValidationError('The csv columns are in the wrong order. The order should be: patient_id, '
                                              'last_name, names, health_centre, dob, address, treatment_start_date and '
                                              'interim_outcome')
                else:
                    if len(row) != 8:
                        raise forms.ValidationError("Row {0} does not have the expected number of columns".format(row_count+1)
                                              , code='invalid')
                    # check that the required fields (patient_id, last_name, names) are filled
                    if not row[0].strip() or not row[1].strip() or not row[2].strip():
                        raise forms.ValidationError("Row {0} lacks one or more of the required fields".format(row_count+1)
                                                    , code='invalid')
                    # check that there isn't an existing patient with the provided patient_id
                    patient = Patient.objects.filter(identifier=row[0]).first()
                    if patient:
                        raise forms.ValidationError("There is already a patient with the patient_id provide in row {0}".format(row_count+1),
                                                    code='invalid')
                row_count += 1
        return super(PatientUploadFileForm, self).clean()

    def clean_uploaded_file(self):
        # checks that the file is not beyond accepted size
        uploaded_file = self.cleaned_data.get('uploaded_file')

        if uploaded_file and uploaded_file.multiple_chunks():
            raise forms.ValidationError('The provided file is too big. It should have a maximum size of 2.5MB', code='invalid')

        return uploaded_file