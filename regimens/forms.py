from django import forms

from .models import Regimen
from communique.forms import PatientFieldForm


class RegimenForm(PatientFieldForm):
    """
    A form used to create a Regimen
    """
    class Meta:
        model = Regimen
        fields = ['patient', 'date_started', 'date_ended', 'drugs', 'notes']

    def clean(self):
        # check that the start date is not greater than the end date
        date_started = self.cleaned_data.get('date_started')
        date_ended = self.cleaned_data.get('date_ended')

        if date_started and date_ended:
            if date_started > date_ended:
                raise forms.ValidationError('The regimen start date cannot occur after the end date', code='invalid')

        return super(RegimenForm, self).clean()


class RegimenUpdateForm(RegimenForm):
    """
    A form used to update the information of a regimen.
    """
    class Meta(RegimenForm.Meta):
        model = Regimen
        fields = ['date_started', 'date_ended', 'notes']