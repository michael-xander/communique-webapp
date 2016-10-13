from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

import csv

from .models import EmergencyContact, AdverseEvent, AdverseEventType
from communique.views import (CommuniqueCreateView, CommuniqueDetailView, CommuniqueListView, CommuniqueUpdateView,
                              CommuniqueDeleteView, CommuniqueExportFormView, CommuniqueExportListView)
from .forms import AdverseEventForm


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


class AdverseEventListView(CommuniqueListView):
    """
    A view to list all the adverse events
    """
    model = AdverseEvent
    template_name = 'adverse/adverse_event_list.html'
    context_object_name = 'adverse_event_list'


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
        date_format = '%d-%m-%Y'
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="adverse_events_{0}_to_{1}.csv"'.format(
            start_date.strftime(date_format), end_date.strftime(date_format))

        fieldnames = ['event_type', 'patient_id', 'event_date (dd-mm-yyyy)', 'date_last_modified (dd-mm-yyyy)',
                      'modified_by', 'notes']
        writer = csv.DictWriter(response, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for adverse_event in context[self.context_object_name]:
            adverse_event_type = adverse_event.adverse_event_type
            patient = adverse_event.patient
            writer.writerow({'event_type':adverse_event_type.__str__(), 'patient_id':patient.identifier,
                             'event_date (dd-mm-yyyy)':adverse_event.event_date.strftime(date_format),
                             'date_last_modified (dd-mm-yyyy)':adverse_event.date_last_modified.strftime(date_format),
                             'modified_by':adverse_event.last_modified_by.get_full_name(), 'notes':adverse_event.notes})

        return response