from .models import AdverseEvent
from communique.forms import PatientFieldForm


class AdverseEventForm(PatientFieldForm):
    """
    A form to create an adverse event
    """
    class Meta:
        model = AdverseEvent
        fields = ['patient', 'adverse_event_type', 'event_date', 'notes']