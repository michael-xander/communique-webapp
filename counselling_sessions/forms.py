from django import forms
from .models import CounsellingSession
from communique.forms import PatientFieldForm


class DurationForm(forms.Form):
    """
    A form used to pick a start date and end date
    """
    start_date = forms.DateField(label='Start date')
    end_date = forms.DateField(label='End date')

    def clean(self):
        # check that the start date is not greater than the end date
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')

        if start_date and end_date:
            if start_date > end_date:
                raise forms.ValidationError('The start date cannot be greater than the end date', code='invalid')

        return super(DurationForm, self).clean()


class CounsellingSessionForm(PatientFieldForm):
    """
    A form to create a counselling session
    """
    class Meta:
        model = CounsellingSession
        fields = ['counselling_session_type', 'patient', 'notes']