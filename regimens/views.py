from django.core.urlresolvers import reverse_lazy

from .models import Drug
from communique.views import (CommuniqueCreateView, CommuniqueDetailView, CommuniqueListView, CommuniqueUpdateView)


class DrugListView(CommuniqueListView):
    """
    A view to list all the drugs in the system
    """
    model = Drug
    template_name = 'regimens/drug_list.html'
    context_object_name = 'drug_list'


class DrugCreateView(CommuniqueCreateView):
    """
    A view to handles the form for creation of a drug
    """
    model = Drug
    fields = ['name', 'description']
    template_name = 'regimens/drug_form.html'

    def form_valid(self, form):
        # fill in the creator fields for the drug model
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user

        return super(DrugCreateView, self).form_valid(form)


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

    def form_valid(self, form):
        # update the user to last modify the drug
        form.instance.last_modified_by = self.request.user

        return super(DrugUpdateView, self).form_valid(form)