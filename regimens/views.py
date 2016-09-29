from django.core.urlresolvers import reverse_lazy

from .models import Drug, Regimen
from .forms import RegimenForm, RegimenUpdateForm
from communique.views import (CommuniqueCreateView, CommuniqueDetailView, CommuniqueListView, CommuniqueUpdateView,
                              CommuniqueDeleteView)


class DrugListView(CommuniqueListView):
    """
    A view to list all the drugs in the system
    """
    model = Drug
    template_name = 'regimens/drug_list.html'
    context_object_name = 'drug_list'


class DrugCreateView(CommuniqueCreateView):
    """
    A view to handle the form for creation of a drug
    """
    model = Drug
    fields = ['name', 'description']
    template_name = 'regimens/drug_form.html'


class DrugDetailView(CommuniqueDetailView):
    """
    A view to display to details of a drug
    """
    model = Drug
    template_name = 'regimens/drug_view.html'
    context_object_name = 'drug'


class DrugUpdateView(CommuniqueUpdateView):
    """
    A view to handle the update form for a drug.
    """
    model = Drug
    fields = ['name', 'description']
    template_name = 'regimens/drug_update_form.html'
    context_object_name = 'drug'


class DrugDeleteView(CommuniqueDeleteView):
    """
    A view to handle the deletion of a drug
    """
    model = Drug
    success_url = reverse_lazy('regimens_drug_list')
    context_object_name = 'drug'
    template_name = 'regimens/drug_confirm_delete.html'


class RegimenCreateView(CommuniqueCreateView):
    """
    A view to handle the form for creation of a regimen
    """
    model = Regimen
    form_class = RegimenForm
    template_name = 'regimens/regimen_form.html'


class RegimenDetailView(CommuniqueDetailView):
    """
    A view to display the details of a regimen
    """
    model = Regimen
    template_name = 'regimens/regimen_view.html'
    context_object_name = 'regimen'


class RegimenListView(CommuniqueListView):
    """
    A view to list all the regimens in the system
    """
    model = Regimen
    template_name = 'regimens/regimen_list.html'
    context_object_name = 'regimen_list'


class RegimenDeleteView(CommuniqueDeleteView):
    """
    A view to handle the deletion of a regimen
    """
    model = Regimen
    success_url = reverse_lazy('regimens_regimen_list')
    context_object_name = 'regimen'
    template_name = 'regimens/regimen_confirm_delete.html'


class RegimenUpdateView(CommuniqueUpdateView):
    """
    A view to handle updating a regimen
    """
    model = Regimen
    form_class = RegimenUpdateForm
    template_name = 'regimens/regimen_update_form.html'
    context_object_name = 'regimen'
