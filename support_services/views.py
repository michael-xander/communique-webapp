from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import viewsets
from rest_framework import permissions

from .models import Service
from .forms import ServiceForm
from .serializers import ServiceSerializer

class ServiceListView(LoginRequiredMixin, ListView):
    """
    A list view for the support service model.
    """
    model = Service
    template_name = 'support_services/service_list.html'
    context_object_name = 'service_list'

class ServiceDetailView(LoginRequiredMixin, DetailView):
    """
    A detail view for the support service model.
    """
    model = Service
    template_name = 'support_services/service_view.html'
    context_object_name = 'service'

class ServiceCreateView(LoginRequiredMixin, CreateView):
    """
    A create view for the support service model.
    """
    form_class = ServiceForm
    model = Service
    template_name = 'support_services/service_form.html'

class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    """
    An UpdateView for the support service model. No shit.
    """
    form_class = ServiceForm
    model = Service
    template_name = 'support_services/service_update_form.html'
    context_object_name = 'service'

class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    """
    A delete view for the support service model.
    """
    model = Service
    template_name = 'support_services/service_confirm_delete.html'
    success_url = reverse_lazy('support_services_service_list')
    context_object_name = 'service'

"""
Views for the REST API
"""

class ServiceViewSet(viewsets.ModelViewSet):
    """
    This view set automatically provides 'list', 'create', 'retrieve', 'update'
    and 'destroy' actions for the Service model via REST API.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticated,)
