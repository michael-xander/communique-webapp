from .models import CounsellingSession
from communique.forms import PatientFieldForm


class CounsellingSessionForm(PatientFieldForm):
    """
    A form to create a counselling session
    """
    class Meta:
        model = CounsellingSession
        fields = ['counselling_session_type', 'patient', 'notes']