from .models import MedicalReport
from communique.forms import PatientFieldForm


class MedicalReportForm(PatientFieldForm):
    """
    A view to create a medical report
    """
    class Meta:
        model = MedicalReport
        fields = ['title', 'report_type', 'patient', 'notes']