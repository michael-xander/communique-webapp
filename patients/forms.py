from django import forms

import csv, copy
from io import StringIO

from appointments.models import Appointment
from appointments.forms import AppointmentForm

from regimens.models import Regimen
from regimens.forms import RegimenForm

from patients.models import Patient
from patients.utils.utils_forms import (ORDERED_UPLOAD_COLUMNS, PATIENT_ID_UPLOAD_COLUMN, OTHER_NAMES_UPLOAD_COLUMN,
                                        LAST_NAME_UPLOAD_COLUMN, SEX_UPLOAD_COLUMN)


class PatientAppointmentForm(AppointmentForm):
    """
    A form used to create an appointment for a patient.
    """
    class Meta(AppointmentForm.Meta):
        model = Appointment
        fields = ['title', 'owner', 'appointment_date', 'start_time', 'end_time', 'notes']


class PatientRegimenForm(RegimenForm):
    """
    A form used to create a regimen for a patient
    """
    class Meta(RegimenForm.Meta):
        model = Regimen
        fields = ['date_started', 'date_ended', 'drugs', 'notes']


class PatientUploadFileForm(forms.Form):
    """
    A form that handles uploading a csv file of patient information
    """
    uploaded_file = forms.FileField(label='Patient data file')

    def clean(self):
        # validate the required fields are available in the provided file
        uploaded_file = self.cleaned_data.get('uploaded_file')

        if uploaded_file:
            temp_file = copy.deepcopy(uploaded_file)
            csvf = StringIO(temp_file.read().decode())
            reader = csv.reader(csvf, delimiter=';')
            row_count = 0
            # iterate through the rows making sure that the required fields are available and the columns in the
            # expected order
            for row in reader:
                # the first row that contains the column names
                if row_count == 0:
                    if len(row) != len(ORDERED_UPLOAD_COLUMNS):
                        raise forms.ValidationError('The right number of columns has not been provided', code='invalid')
                    # check that the columns are in their expected orders
                    for i in list(range(len(ORDERED_UPLOAD_COLUMNS))):
                        if row[i] != ORDERED_UPLOAD_COLUMNS[i]:
                            raise forms.ValidationError('The csv columns are in the wrong order.', code='invalid')
                else:
                    if len(row) != len(ORDERED_UPLOAD_COLUMNS):
                        raise forms.ValidationError("Row {0} does not have the expected number of columns".format(row_count+1)
                                              , code='invalid')
                    # check that the required fields (patient_id, last_name, names) are filled
                    if not row[ORDERED_UPLOAD_COLUMNS.index(PATIENT_ID_UPLOAD_COLUMN)].strip() \
                            or not row[ORDERED_UPLOAD_COLUMNS.index(OTHER_NAMES_UPLOAD_COLUMN)].strip() \
                            or not row[ORDERED_UPLOAD_COLUMNS.index(LAST_NAME_UPLOAD_COLUMN)].strip() \
                            or not row[ORDERED_UPLOAD_COLUMNS.index(SEX_UPLOAD_COLUMN)]:
                        raise forms.ValidationError("Row {0} lacks one or more of the required fields".format(row_count+1)
                                                    , code='invalid')
                    # check that there isn't an existing patient with the provided patient_id
                    patient = Patient.objects.filter(
                        identifier=row[ORDERED_UPLOAD_COLUMNS.index(PATIENT_ID_UPLOAD_COLUMN)]).first()
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