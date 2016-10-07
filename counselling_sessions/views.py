from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

import csv

from .models import CounsellingSession, CounsellingSessionType
from communique.views import (CommuniqueDeleteView, CommuniqueListView, CommuniqueDetailView, CommuniqueUpdateView,
                              CommuniqueCreateView, CommuniqueExportFormView, CommuniqueExportListView)
from .forms import CounsellingSessionForm


class CounsellingSessionTypeListView(CommuniqueListView):
    """
    A view that retrieves all the available session types.
    """
    model = CounsellingSessionType
    template_name = 'counselling_sessions/counselling_session_type_list.html'
    context_object_name = 'counselling_session_type_list'


class CounsellingSessionTypeCreateView(CommuniqueCreateView):
    """
    A view that handles creation of a session type.
    """
    model = CounsellingSessionType
    template_name = 'counselling_sessions/counselling_session_type_form.html'
    fields = ['name', 'description']


class CounsellingSessionTypeDetailView(CommuniqueDetailView):
    """
    A view that handles displaying details of a session type.
    """
    model = CounsellingSessionType
    template_name = 'counselling_sessions/counselling_session_type_view.html'
    context_object_name = 'counselling_session_type'


class CounsellingSessionTypeUpdateView(CommuniqueUpdateView):
    """
    A view that handles updating of a session type.
    """
    model = CounsellingSessionType
    fields = ['name', 'description']
    template_name = 'counselling_sessions/counselling_session_type_update_form.html'
    context_object_name = 'counselling_session_type'


class CounsellingSessionTypeDeleteView(CommuniqueDeleteView):
    """
    A view that handles the deletion of a session type.
    """
    model = CounsellingSessionType
    success_url = reverse_lazy('counselling_sessions_type_list')
    context_object_name = 'counselling_session_type'
    template_name = 'counselling_sessions/counselling_session_type_confirm_delete.html'


class CounsellingSessionListView(CommuniqueListView):
    """
    A view that retrieves all available sessions.
    """
    model = CounsellingSession
    template_name = 'counselling_sessions/counselling_session_list.html'
    context_object_name = 'counselling_session_list'


class CounsellingSessionCreateView(CommuniqueCreateView):
    """
    A view that handles creation of a session.
    """
    model = CounsellingSession
    template_name = 'counselling_sessions/counselling_session_form.html'
    form_class = CounsellingSessionForm


class CounsellingSessionDetailView(CommuniqueDetailView):
    """
    A view that handles displaying details of a session.
    """
    model = CounsellingSession
    template_name = 'counselling_sessions/counselling_session_view.html'
    context_object_name = 'counselling_session'


class CounsellingSessionUpdateView(CommuniqueUpdateView):
    """
    A view that handles updating a session.
    """
    model = CounsellingSession
    fields = ['notes']
    template_name = 'counselling_sessions/counselling_session_update_form.html'
    context_object_name = 'counselling_session'


class CounsellingSessionDeleteView(CommuniqueDeleteView):
    """
    A view that handles the deletion of a session.
    """
    model = CounsellingSession
    success_url = reverse_lazy('counselling_sessions_session_list')
    context_object_name = 'counselling_session'
    template_name = 'counselling_sessions/counselling_session_confirm_delete.html'


class CounsellingSessionExportFormView(CommuniqueExportFormView):
    """
    A view that handles the form for picking the creation dates for counselling sessions to be exported
    """
    template_name = 'counselling_sessions/counselling_session_export_list.html'

    def get_success_view_name(self):
        # return the name of the view to which to redirect to on successful validation
        return 'counselling_sessions_export_list'


class CounsellingSessionExportListView(CommuniqueExportListView):
    """
    A view that lists counselling sessions to be exported depending on the provided start and end dates
    """
    model = CounsellingSession
    template_name = 'counselling_sessions/counselling_session_export_list.html'
    context_object_name = 'counselling_session_export_list'

    def get_queryset(self):
        # get all the counselling sessions within the provided date range
        start_date = self.get_export_start_date()
        end_date = self.get_export_end_date()
        counselling_sessions = CounsellingSession.objects.filter(date_created__range=[start_date, end_date])
        return counselling_sessions

    def csv_export_response(self, context):
        # generate an HTTP response with the csv file for download
        start_date = self.get_export_start_date()
        end_date = self.get_export_end_date()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="sessions_{0}_{1}.csv"'.format(
            start_date.strftime('%d-%m-%Y'), end_date.strftime('%d-%m-%Y'))

        fieldnames = ['session_type','patient_id', 'patient_last_name', 'patient_other_names', 'added_by',
                      'date_added (dd-mm-yyyy)', 'notes']
        writer = csv.DictWriter(response, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for counselling_session in context[self.context_object_name]:
            session_type = counselling_session.counselling_session_type
            patient = counselling_session.patient
            writer.writerow({'session_type':session_type.__str__(), 'patient_id':patient.identifier,
                                 'patient_last_name':patient.last_name, 'patient_other_names':patient.other_names,
                                 'added_by':counselling_session.created_by.get_full_name(),
                                 'date_added (dd-mm-yyyy)':counselling_session.date_created.strftime('%d-%m-%Y'),
                                 'notes':counselling_session.notes})
        return response


