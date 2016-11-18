from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

import datetime

from .models import CounsellingSession, CounsellingSessionType
from communique.views import (CommuniqueDeleteView, CommuniqueListView, CommuniqueDetailView, CommuniqueUpdateView,
                              CommuniqueCreateView, CommuniqueExportFormView, CommuniqueExportListView,
                              CommuniqueListAndExportView, DATE_FORMAT_STR, DATE_FORMAT, CommuniqueDetailAndExportView)
from .forms import CounsellingSessionForm
from .utils.utils_views import write_sessions_to_csv


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
    success_message = 'The counselling session type was successfully added'
    template_name = 'counselling_sessions/counselling_session_type_form.html'
    fields = ['name', 'description']


class CounsellingSessionTypeDetailView(CommuniqueDetailAndExportView):
    """
    A view that handles displaying details of a session type.
    """
    model = CounsellingSessionType
    template_name = 'counselling_sessions/counselling_session_type_view.html'
    context_object_name = 'counselling_session_type'

    def csv_export_response(self, context):
        # generate csv for exportation
        today = datetime.date.today()
        session_type = context[self.context_object_name]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="{0}_counselling_sessions_{1}.csv"'.format(
            session_type, today.strftime(DATE_FORMAT))
        write_sessions_to_csv(response, session_type.counselling_sessions.all(), DATE_FORMAT, DATE_FORMAT_STR)
        return response


class CounsellingSessionTypeUpdateView(CommuniqueUpdateView):
    """
    A view that handles updating of a session type.
    """
    model = CounsellingSessionType
    success_message = 'The details of the counselling session type were successfully updated'
    fields = ['name', 'description']
    template_name = 'counselling_sessions/counselling_session_type_update_form.html'
    context_object_name = 'counselling_session_type'


class CounsellingSessionTypeDeleteView(CommuniqueDeleteView):
    """
    A view that handles the deletion of a session type.
    """
    model = CounsellingSessionType
    success_message = 'The counselling session type was successfully deleted'
    success_url = reverse_lazy('counselling_sessions_type_list')
    context_object_name = 'counselling_session_type'
    template_name = 'counselling_sessions/counselling_session_type_confirm_delete.html'


class CounsellingSessionListView(CommuniqueListAndExportView):
    """
    A view that retrieves all available sessions.
    """
    model = CounsellingSession
    template_name = 'counselling_sessions/counselling_session_list.html'
    context_object_name = 'counselling_session_list'

    def csv_export_response(self, context):
        # generate csv for download
        today = datetime.date.today()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="all_counselling_sessions_{0}.csv"'.format(
            today.strftime(DATE_FORMAT))
        write_sessions_to_csv(response, context[self.context_object_name], DATE_FORMAT, DATE_FORMAT_STR)
        return response


class CounsellingSessionCreateView(CommuniqueCreateView):
    """
    A view that handles creation of a session.
    """
    model = CounsellingSession
    success_message = 'The counselling session was successfully added'
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
    success_message = 'The details of the counselling session were successfully updated'
    fields = ['notes']
    template_name = 'counselling_sessions/counselling_session_update_form.html'
    context_object_name = 'counselling_session'


class CounsellingSessionDeleteView(CommuniqueDeleteView):
    """
    A view that handles the deletion of a session.
    """
    model = CounsellingSession
    success_message = 'The counselling session was successfully deleted'
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
        counselling_sessions = CounsellingSession.objects.filter(date_last_modified__range=[start_date, end_date])
        return counselling_sessions

    def csv_export_response(self, context):
        # generate an HTTP response with the csv file for download
        start_date = self.get_export_start_date()
        end_date = self.get_export_end_date()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="sessions_{0}_to_{1}.csv"'.format(
            start_date.strftime(DATE_FORMAT), end_date.strftime(DATE_FORMAT))
        write_sessions_to_csv(response, context[self.context_object_name], DATE_FORMAT, DATE_FORMAT_STR)

        return response


