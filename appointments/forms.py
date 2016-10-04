from django import forms

import datetime

from .models import Appointment
from communique.forms import PatientFieldForm


class AppointmentForm(PatientFieldForm):
    """
    A form used to create and update an appointment
    """

    class Meta:
        model = Appointment
        fields = ['title', 'owner', 'patient', 'appointment_date', 'start_time', 'end_time', 'notes']

    def clean(self):
        # check that the start_time is less than the end_time
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')

        if start_time and end_time:
            if start_time >= end_time:
                raise forms.ValidationError('The start time cannot be greater than or equal to the end time',
                                            code='invalid')

        return super(AppointmentForm, self).clean()

    def clean_appointment_date(self):
        # check that the provided appointment date is not in the past
        appointment_date = self.cleaned_data.get('appointment_date')

        if appointment_date:
            current_date = datetime.date.today()
            if appointment_date < current_date:
                raise forms.ValidationError('The appointment date cannot be set in the past', code='invalid')

        return appointment_date
