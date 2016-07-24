from django.forms import ModelForm
from .models import Service

class ServiceForm(ModelForm):
    """
    A ModelForm for the Service class.
    """
    class Meta:
        model = Service
        fields = ('name', 'description')
