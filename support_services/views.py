from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Service

class ServiceListView(ListView):
    """
    A list view for the support service model.
    """
    model = Service
    template_name = 'support_services/service_list.html'
    context_object_name = 'service_list'

class ServiceDetailView(DetailView):
    """
    A detail view of the support service model.
    """
    model = Service
    template_name = 'support_services/service_view.html'
    context_object_name = 'service'
