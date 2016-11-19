from django.core.urlresolvers import reverse_lazy

from .models import MedicalReport, MedicalReportType
from communique.views import (CommuniqueDeleteView, CommuniqueListView, CommuniqueDetailView, CommuniqueUpdateView,
                              CommuniqueCreateView)
from .forms import MedicalReportForm


class MedicalReportTypeListView(CommuniqueListView):
    """
    A view that retrieves all available medical report types.
    """
    model = MedicalReportType
    template_name = 'medical/medical_report_type_list.html'
    context_object_name = 'medical_report_type_list'


class MedicalReportTypeCreateView(CommuniqueCreateView):
    """
    A view that handles creation of a report type.
    """
    model = MedicalReportType
    success_message = 'The medical report type was successfully added'
    template_name = 'medical/medical_report_type_form.html'
    fields = ['name', 'description']


class MedicalReportTypeDetailView(CommuniqueDetailView):
    """
    A view that handles displaying details of a report type.
    """
    model = MedicalReportType
    template_name = 'medical/medical_report_type_view.html'
    context_object_name = 'medical_report_type'


class MedicalReportTypeUpdateView(CommuniqueUpdateView):
    """
    A view that handles updating the details of a report type.
    """
    model = MedicalReportType
    success_message = 'The details of the medical report type were successfully updated'
    fields = ['name', 'description']
    template_name = 'medical/medical_report_type_update_form.html'
    context_object_name = 'medical_report_type'


class MedicalReportTypeDeleteView(CommuniqueDeleteView):
    """
    This view handles the deletion of a report type.
    """
    model = MedicalReportType
    success_message = 'The medical report type was successfully deleted'
    success_url = reverse_lazy('medical_report_type_list')
    context_object_name = 'medical_report_type'
    template_name = 'medical/medical_report_type_confirm_delete.html'


class MedicalReportListView(CommuniqueListView):
    """
    A view that retrieves all available medical reports.
    """
    model = MedicalReport
    template_name = 'medical/medical_report_list.html'
    context_object_name = 'medical_report_list'


class MedicalReportCreateView(CommuniqueCreateView):
    """
    A view that handles the creation of a medical report.
    """
    model = MedicalReport
    success_message = 'The medical report was successfully added'
    template_name = 'medical/medical_report_form.html'
    form_class = MedicalReportForm


class MedicalReportDetailView(CommuniqueDetailView):
    """
    A view that handles displaying details of a medical report.
    """
    model = MedicalReport
    template_name = 'medical/medical_report_view.html'
    context_object_name = 'medical_report'


class MedicalReportUpdateView(CommuniqueUpdateView):
    """
    A view that handles updating a medical report.
    """
    model = MedicalReport
    success_message = 'The details of the medical report were successfully updated'
    template_name = 'medical/medical_report_update_form.html'
    fields = ['title', 'report_type', 'notes']
    context_object_name = 'medical_report'


class MedicalReportDeleteView(CommuniqueDeleteView):
    """
    A view that handles the deletion of a medical report.
    """
    model = MedicalReport
    success_message = 'The medical report was successfully deleted'
    success_url = reverse_lazy('medical_report_list')
    context_object_name = 'medical_report'
    template_name = 'medical/medical_report_confirm_delete.html'
