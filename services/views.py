from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import PatientSerializer, PilotProgramSerializer
from .models import Patient, PilotProgram
from .forms import PilotProgramForm, PatientForm

"""
Views for the Web App
"""
class PilotProgramListView(LoginRequiredMixin, ListView):
    """
    A list view for the pilot program model.
    """
    model = PilotProgram
    template_name = 'services/pilot_program_list.html'
    context_object_name = 'pilot_program_list'

class PilotProgramDetailView(LoginRequiredMixin, DetailView):
    """
    A detail view for the Pilot Program model.
    """
    model = PilotProgram
    template_name = 'services/pilot_program_view.html'
    context_object_name = 'pilot_program'

class PilotProgramCreateView(LoginRequiredMixin, CreateView):
    """
    A create view for the pilot program model.
    """
    form_class = PilotProgramForm
    model = PilotProgram
    template_name = 'services/pilot_program_form.html'

class PilotProgramUpdateView(LoginRequiredMixin, UpdateView):
    """
    An update view for the pilot program model.
    """
    form_class = PilotProgramForm
    model = PilotProgram
    template_name = 'services/pilot_program_update_form.html'
    context_object_name = 'pilot_program'

class PilotProgramDeleteView(LoginRequiredMixin, DeleteView):
    """
    A delete view for the pilot progrom model.
    """
    model = PilotProgram
    template_name = 'services/pilot_program_confirm_delete.html'
    success_url = reverse_lazy('services_pilot_program_list')
    context_object_name = 'pilot_program'

class PatientListView(LoginRequiredMixin, ListView):
    """
    A list view for the patient model.
    """
    model = Patient
    template_name = 'services/patient_list.html'
    context_object_name = 'patient_list'

class PatientDetailView(LoginRequiredMixin, DetailView):
    """
    A detail view for the patient model.
    """
    model = Patient
    template_name = 'services/patient_view.html'
    context_object_name = 'patient'

class PatientCreateView(LoginRequiredMixin, CreateView):
    """
    A create view for the patient model.
    """
    form_class = PatientForm
    model = Patient
    template_name = 'services/patient_form.html'

class PatientUpdateView(LoginRequiredMixin, UpdateView):
    """
    An update view for the patient model.
    """
    form_class = PatientForm
    model = Patient
    template_name = 'services/patient_update_form.html'
    context_object_name = 'patient'

class PatientDeleteView(LoginRequiredMixin, DeleteView):
    """
    A delete view for the patient model.
    """
    model = Patient
    template_name = 'services/patient_confirm_delete.html'
    success_url = reverse_lazy('services_patient_list')
    context_object_name = 'patient'


"""
Views for the REST API
"""

class PatientViewSet(viewsets.ModelViewSet):
    """
    A view set that automatically provides `list`, `create`, `retrieve`, `update`
    and `destroy` actions for the Patient model via REST API.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = (permissions.IsAuthenticated,)

class PilotProgramViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A view set that automatically provides `list` and `detail` actions for the
    Pilot Program model via REST API.
    """
    queryset = PilotProgram.objects.all()
    serializer_class = PilotProgramSerializer
    permission_classes = (permissions.IsAuthenticated,)