from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

import datetime

from .models import EmergencyContact, AdverseEvent, AdverseEventType
from communique.views import (CommuniqueCreateView, CommuniqueDetailView, CommuniqueListView, CommuniqueUpdateView,
                              CommuniqueDeleteView, CommuniqueExportFormView, CommuniqueExportListView,
                              DATE_FORMAT_STR, DATE_FORMAT, CommuniqueListAndExportView)
from .forms import AdverseEventForm
from .utils.utils_views import write_adverse_events_to_csv


class EmergencyContactListView(CommuniqueListView):
    """
    A view to list all the emergency contacts in the system
    """
    model = EmergencyContact
    template_name = 'adverse/emergency_contact_list.html'
    context_object_name = 'emergency_contact_list'


class EmergencyContactCreateView(CommuniqueCreateView):
    """
    A view to handle the form for creation of an emergency contact
    """
    model = EmergencyContact
    fields = ['name', 'email']
    template_name = 'adverse/emergency_contact_form.html'


class EmergencyContactDetailView(CommuniqueDetailView):
    """
    A view to display details of an emergency contact
    """
    model = EmergencyContact
    template_name = 'adverse/emergency_contact_view.html'
    context_object_name = 'emergency_contact'


class EmergencyContactUpdateView(CommuniqueUpdateView):
    """
    A view to handle the update form for a drug
    """
    model = EmergencyContact
    fields = ['name', 'email']
    template_name = 'adverse/emergency_contact_update_form.html'
    context_object_name = 'emergency_contact'


class EmergencyContactDeleteView(CommuniqueDeleteView):
    """
    A view to handle the deletion of an emergency contact
    """
    model = EmergencyContact
    success_url = reverse_lazy('adverse_emergency_contact_list')
    context_object_name = 'emergency_contact'
    template_name = 'adverse/emergency_contact_confirm_delete.html'


class AdverseEventTypeListView(CommuniqueListView):
    """
    A view to list all the adverse event types
    """
    model = AdverseEventType
    template_name = 'adverse/adverse_event_type_list.html'
    context_object_name = 'adverse_event_type_list'


class AdverseEventTypeCreateView(CommuniqueCreateView):
    """
    A view to handle the form for creation of an adverse event type
    """
    model = AdverseEventType
    fields = ['name', 'description', 'emergency_contacts']
    template_name = 'adverse/adverse_event_type_form.html'


class AdverseEventTypeDetailView(CommuniqueDetailView):
    """
    A view to display the details of an adverse event type
    """
    model = AdverseEventType
    template_name = 'adverse/adverse_event_type_view.html'
    context_object_name = 'adverse_event_type'


class AdverseEventTypeUpdateView(CommuniqueUpdateView):
    """
    A view to handle the update form of an adverse event type
    """
    model = AdverseEventType
    fields = ['name', 'description', 'emergency_contacts']
    template_name = 'adverse/adverse_event_type_update_form.html'
    context_object_name = 'adverse_event_type'


class AdverseEventTypeDeleteView(CommuniqueDeleteView):
    """
    A view to handle deletion of an adverse event type
    """
    model = AdverseEventType
    success_url = reverse_lazy('adverse_event_type_list')
    context_object_name = 'adverse_event_type'
    template_name = 'adverse/adverse_event_type_confirm_delete.html'


class AdverseEventListView(CommuniqueListAndExportView):
    """
    A view to list all the adverse events
    """
    model = AdverseEvent
    template_name = 'adverse/adverse_event_list.html'
    context_object_name = 'adverse_event_list'

    def csv_export_response(self, context):
        # generate a csv file for download
        today = datetime.date.today()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="all_adverse_events_{0}.csv"'.format(
            today.strftime(DATE_FORMAT))

        write_adverse_events_to_csv(response, context[self.context_object_name], DATE_FORMAT, DATE_FORMAT_STR)

        return response


class AdverseEventCreateView(CommuniqueCreateView):
    """
    A view to handle the form for creation of an adverse event
    """
    model = AdverseEvent
    form_class = AdverseEventForm
    template_name = 'adverse/adverse_event_form.html'


class AdverseEventDetailView(CommuniqueDetailView):
    """
    A view to display the details of an adverse event
    """
    model = AdverseEvent
    template_name = 'adverse/adverse_event_view.html'
    context_object_name = 'adverse_event'


class AdverseEventUpdateView(CommuniqueUpdateView):
    """
    A view to handle the update form of an adverse event
    """
    model = AdverseEvent
    fields = ['event_date', 'notes']
    template_name = 'adverse/adverse_event_update_form.html'
    context_object_name = 'adverse_event'


class AdverseEventDeleteView(CommuniqueDeleteView):
    """
    A view to handle deletion of an adverse event type
    """
    model = AdverseEvent
    success_url = reverse_lazy('adverse_event_list')
    context_object_name = 'adverse_event'
    template_name = 'adverse/adverse_event_confirm_delete.html'


class AdverseEventExportFormView(CommuniqueExportFormView):
    """
    A view that handles the form for picking the creation dates for adverse events to be exported
    """
    template_name = 'adverse/adverse_event_export_list.html'

    def get_success_view_name(self):
        # return the name of the view to redirect to on successful validation
        return 'adverse_event_export_list'


class AdverseEventExportListView(CommuniqueExportListView):
    """
    A view that lists adverse events to be exported
    """
    model = AdverseEvent
    template_name = 'adverse/adverse_event_export_list.html'
    context_object_name = 'adverse_event_export_list'

    def get_queryset(self):
        # get all the adverse events created during the provided range
        start_date = self.get_export_start_date()
        end_date = self.get_export_end_date()
        adverse_events = AdverseEvent.objects.filter(date_last_modified__range=[start_date, end_date])
        return adverse_events

    def csv_export_response(self, context):
        # generate an HTTP response with the csv file for download
        start_date = self.get_export_start_date()
        end_date = self.get_export_end_date()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="adverse_events_{0}_to_{1}.csv"'.format(
            start_date.strftime(DATE_FORMAT), end_date.strftime(DATE_FORMAT))

        write_adverse_events_to_csv(response, context[self.context_object_name], DATE_FORMAT, DATE_FORMAT_STR)
        return response