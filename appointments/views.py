from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

import csv

from communique.views import (CommuniqueDeleteView, CommuniqueListView, CommuniqueDetailView, CommuniqueUpdateView,
                              CommuniqueCreateView, CommuniqueExportFormView, CommuniqueExportListView)
from .models import Appointment
from .forms import AppointmentForm


class AppointmentCreateView(CommuniqueCreateView):
    """
    A view that handles creation of an appointment.
    """
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/appointment_form.html'

    def form_valid(self, form):
        # set the owner of the appointment as current user if not chosen in form
        if not form.instance.owner:
            form.instance.owner = self.request.user

        return super(AppointmentCreateView, self).form_valid(form)


class AppointmentDetailView(CommuniqueDetailView):
    """
    A view that handles displaying appointment details.
    """
    model = Appointment
    template_name = 'appointments/appointment_view.html'
    context_object_name = 'appointment'


class AppointmentUpdateView(CommuniqueUpdateView):
    """
    A view that handles updating an appointment.
    """
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/appointment_update_form.html'
    context_object_name = 'appointment'

    def form_valid(self, form):
        # set the owner as currently logged in user if none chosen in form
        if not form.instance.owner:
            form.instance.owner = self.request.owner

        return super(AppointmentUpdateView, self).form_valid(form)


class AppointmentListView(CommuniqueListView):
    """
    A view that lists available appointments.
    """
    model = Appointment
    template_name = 'appointments/appointment_list.html'
    context_object_name = 'appointment_list'


class AppointmentDeleteView(CommuniqueDeleteView):
    """
    A view that handles deletion of an appointment.
    """
    model = Appointment
    success_url = reverse_lazy('appointments_appointment_list')
    context_object_name = 'appointment'
    template_name = 'appointments/appointment_confirm_delete.html'


class AppointmentExportFormView(CommuniqueExportFormView):
    """
    A view that handles the form for picking the creation dates for appointments to be exported
    """
    template_name = 'appointments/appointment_export_list.html'

    def get_success_view_name(self):
        return 'appointments_appointment_export_list'


class AppointmentExportListView(CommuniqueExportListView):
    """
    A view that lists all the appointments that are to be exported depending on the selected start and end dates
    """
    model = Appointment
    template_name = 'appointments/appointment_export_list.html'
    context_object_name = 'appointment_export_list'

    def get_queryset(self):
        # get all the appointments within the provided date range
        start_date = self.get_export_start_date()
        end_date = self.get_export_end_date()
        appointments = Appointment.objects.filter(appointment_date__range=[start_date, end_date])
        return appointments

    def csv_export_response(self, context):
        # generate an HTTP response with the csv file for download
        start_date = self.get_export_start_date()
        end_date = self.get_export_end_date()
        date_format = '%d-%m-%Y'
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="appointments_{0}_to_{1}.csv"'.format(
            start_date.strftime(date_format), end_date.strftime(date_format)
        )
        fieldnames = ['id', 'title', 'patient_id', 'patient_last_name', 'patient_other_names', 'owner', 'added_by',
                      'appointment_date (dd-mm-yyyy)', 'start_time', 'end_time', 'notes','date_added (dd-mm-yyyy)']
        writer = csv.DictWriter(response, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for appointment in context[self.context_object_name]:
            # only export appointments that are assigned a patient and owner
            patient = appointment.patient
            owner = appointment.owner
            if patient and owner:
                writer.writerow({'id':appointment.id, 'title':appointment.__str__(), 'patient_id':patient.identifier,
                                 'patient_last_name':patient.last_name, 'patient_other_names':patient.other_names,
                                 'owner':owner.get_full_name(), 'added_by':appointment.created_by.get_full_name(),
                                 'appointment_date (dd-mm-yyyy)':appointment.appointment_date.strftime(date_format),
                                 'start_time':appointment.start_time, 'end_time':appointment.end_time,
                                 'notes':appointment.notes,
                                 'date_added (dd-mm-yyyy)':appointment.date_created.strftime(date_format)})
        return response
