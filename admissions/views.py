from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

import datetime

from communique.views import (CommuniqueCreateView, CommuniqueDetailView, CommuniqueDeleteView, CommuniqueListView,
                              CommuniqueUpdateView, CommuniqueExportFormView, CommuniqueExportListView,
                              DATE_FORMAT_STR, DATE_FORMAT, CommuniqueListAndExportView)
from .models import Admission
from .forms import AdmissionUpdateForm, AdmissionCreateForm
from .utils.utils_views import write_admissions_to_csv


class AdmissionCreateView(CommuniqueCreateView):
    """
    A view that handles creation of an admission.
    """
    model = Admission
    form_class = AdmissionCreateForm
    template_name = 'admissions/admission_form.html'


class AdmissionDetailView(CommuniqueDetailView):
    """
    A view that handles displaying details of an admission.
    """
    model = Admission
    template_name = 'admissions/admission_view.html'
    context_object_name = 'admission'


class AdmissionUpdateView(CommuniqueUpdateView):
    """
    A view that handles updating of an admission.
    """
    model = Admission
    form_class = AdmissionUpdateForm
    template_name = 'admissions/admission_update_form.html'
    context_object_name = 'admission'


class AdmissionListView(CommuniqueListAndExportView):
    """
    A view that lists the existing admissions.
    """
    model = Admission
    template_name = 'admissions/admission_list.html'
    context_object_name = 'admission_list'

    def csv_export_response(self, context):
        # generate a csv for exportation
        today = datetime.date.today()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="all_admissions_{0}.csv"'.format(
            today.strftime(DATE_FORMAT))
        write_admissions_to_csv(response, context[self.context_object_name], DATE_FORMAT, DATE_FORMAT_STR)

        return response


class AdmissionDeleteView(CommuniqueDeleteView):
    """
    A view that handles deletion of an admission.
    """
    model = Admission
    success_url = reverse_lazy('admissions_admission_list')
    context_object_name = 'admission'
    template_name = 'admissions/admission_confirm_delete.html'


class AdmissionExportFormView(CommuniqueExportFormView):
    """
    A view that handles the form for picking the creation/modified dates for admissions to be exported
    """
    template_name = 'admissions/admission_export_list.html'

    def get_success_view_name(self):
        return 'admissions_admission_export_list'


class AdmissionExportListView(CommuniqueExportListView):
    """
    A view that lists admissions to be exported depending on the provided start and end dates
    """
    model = Admission
    template_name = 'admissions/admission_export_list.html'
    context_object_name = 'admissions_export_list'

    def get_queryset(self):
        # get all the admissions within the provided date range
        start_date = self.get_export_start_date()
        end_date = self.get_export_end_date()
        admissions = Admission.objects.filter(date_last_modified__range=[start_date, end_date])
        return admissions

    def csv_export_response(self, context):
        # generate an HTTP response with the csv file for the download
        start_date = self.get_export_start_date()
        end_date = self.get_export_end_date()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="admissions_{0}_to_{1}.csv"'.format(
            start_date.strftime(DATE_FORMAT), end_date.strftime(DATE_FORMAT))
        write_admissions_to_csv(response, context[self.context_object_name], DATE_FORMAT, DATE_FORMAT_STR)

        return response
