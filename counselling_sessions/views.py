from django.core.urlresolvers import reverse_lazy, reverse

import datetime

from .models import CounsellingSession, CounsellingSessionType
from communique.views import (CommuniqueDeleteView, CommuniqueListView, CommuniqueDetailView, CommuniqueUpdateView,
                              CommuniqueCreateView, CommuniqueFormView)
from .forms import CounsellingSessionForm, DurationForm


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


class CounsellingSessionExportFormView(CommuniqueFormView):
    """
    A view that handles the form for picking the creation dates for counselling sessions to be exported
    """
    form_class = DurationForm
    template_name = 'counselling_sessions/counselling_session_export_list.html'

    def form_valid(self, form):
        # get the start and end date on valid form submission
        self.start_date = form.cleaned_data['start_date']
        self.end_date = form.cleaned_data['end_date']
        return super(CounsellingSessionExportFormView, self).form_valid(form)

    def get_success_url(self):
        # on successful validation of the form, redirect to the export list view with the provided start and end date

        start_date = self.start_date
        end_date = self.end_date

        start_year = '{:04d}'.format(start_date.year)
        end_year = '{:04d}'.format(end_date.year)

        start_month = '{:02d}'.format(start_date.month)
        end_month = '{:02d}'.format(end_date.month)

        start_day = '{:02d}'.format(start_date.day)
        end_day = '{:02d}'.format(end_date.day)
        return reverse('counselling_sessions_export_list', kwargs={'start_year':start_year, 'start_month':start_month,
                                                                   'start_day':start_day, 'end_year':end_year,
                                                                   'end_month':end_month, 'end_day':end_day})


class CounsellingSessionExportListView(CommuniqueListView):
    """
    A view that lists counselling sessions to be exported depending on the provided start and end dates
    """
    model = CounsellingSession
    template_name = 'counselling_sessions/counselling_session_export_list.html'
    context_object_name = 'counselling_session_export_list'

    def get_queryset(self):
        # get all the counselling sessions within the provided date range
        start_date = datetime.date(year=int(self.kwargs['start_year']), month=int(self.kwargs['start_month']),
                                   day=int(self.kwargs['start_day']))
        end_date = datetime.date(year=int(self.kwargs['end_year']), month=int(self.kwargs['end_month']),
                                 day=int(self.kwargs['end_day']))
        counselling_sessions = CounsellingSession.objects.filter(date_created__range=[start_date, end_date])
        return counselling_sessions

    def get_context_data(self, **kwargs):
        # add the duration form to the context
        context = super(CounsellingSessionExportListView, self).get_context_data(**kwargs)

        start_date = datetime.date(year=int(self.kwargs['start_year']), month=int(self.kwargs['start_month']),
                                   day=int(self.kwargs['start_day']))
        end_date = datetime.date(year=int(self.kwargs['end_year']), month=int(self.kwargs['end_month']),
                                 day=int(self.kwargs['end_day']))
        data = {'start_date':start_date, 'end_date':end_date}

        context['form'] = DurationForm(data)
        return context

