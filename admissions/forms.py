from django import forms

from .models import Admission
from communique.forms import PatientFieldForm


class AdmissionCreateForm(PatientFieldForm):
    """
    A form used to create an admission for a patient.
    """
    class Meta:
        model = Admission
        fields = ['patient', 'health_centre', 'admission_date', 'discharge_date', 'notes']

    def clean(self):
        # check that the admission date is not greater than the discharge date
        admission_date = self.cleaned_data.get('admission_date')
        discharge_date = self.cleaned_data.get('discharge_date')

        if admission_date and discharge_date:
            if admission_date > discharge_date:
                raise forms.ValidationError('The admission date cannot occur after the discharge date', code='invalid')

        return super(AdmissionCreateForm, self).clean()


class AdmissionUpdateForm(AdmissionCreateForm):
    """
    A form used to update the information of an admission
    """
    class Meta(AdmissionCreateForm.Meta):
        model = Admission
        fields = ['health_centre', 'admission_date', 'discharge_date', 'notes']