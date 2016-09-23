from django.core.urlresolvers import reverse_lazy

from .models import Drug
from communique.views import (CommuniqueCreateView)


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