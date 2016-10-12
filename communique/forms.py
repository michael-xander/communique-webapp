from django import forms

from patients.models import Patient


class PatientFieldForm(forms.ModelForm):
    """
    A model form that filters the patient field, if available, to utilise only patients that are not archived
    """
    def __init__(self, *args, **kwargs):
        super(PatientFieldForm, self).__init__(*args, **kwargs)
        # check for the patient field
        if 'patient' in self.fields:
            self.fields['patient'].queryset = Patient.objects.filter(archived=False)


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
