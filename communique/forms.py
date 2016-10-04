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