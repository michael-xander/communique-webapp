from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

import datetime

from .models import Drug, Regimen
from .forms import RegimenForm, RegimenUpdateForm
from communique.views import (CommuniqueCreateView, CommuniqueDetailView, CommuniqueListView, CommuniqueUpdateView,
                              CommuniqueDeleteView, CommuniqueListAndExportView, CommuniqueDetailAndExportView,
                              DATE_FORMAT_STR, DATE_FORMAT)
from .utils.utils_views import write_regimens_to_csv


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


class DrugDetailView(CommuniqueDetailAndExportView):
    """
    A view to display to details of a drug
    """
    model = Drug
    template_name = 'regimens/drug_view.html'
    context_object_name = 'drug'

    def csv_export_response(self, context):
        # generate a csv fir exportation
        today = datetime.date.today()
        drug = context[self.context_object_name]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="{0}_regimens_{1}.csv"'.format(
            drug, today.strftime(DATE_FORMAT))
        write_regimens_to_csv(response, drug.regimens.all(), DATE_FORMAT, DATE_FORMAT_STR)
        return response


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


class RegimenListView(CommuniqueListAndExportView):
    """
    A view to list all the regimens in the system
    """
    model = Regimen
    template_name = 'regimens/regimen_list.html'
    context_object_name = 'regimen_list'

    def csv_export_response(self, context):
        # generate a csv for exportation
        today = datetime.date.today()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="all_regimens_{0}.csv"'.format(
            today.strftime(DATE_FORMAT))
        write_regimens_to_csv(response, context[self.context_object_name], DATE_FORMAT, DATE_FORMAT_STR)
        return response


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
