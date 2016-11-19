from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

import datetime

from communique.views import (CommuniqueDeleteView, CommuniqueDetailView, CommuniqueUpdateView,
                              CommuniqueCreateView, CommuniqueExportFormView, CommuniqueExportListView,
                              CommuniqueListAndExportView, DATE_FORMAT_STR, DATE_FORMAT)
from .models import Appointment
from .forms import AppointmentForm
from .utils.utils_views import write_appointments_to_csv


class AppointmentCreateView(CommuniqueCreateView):
    """
    A view that handles creation of an appointment.
    """
    model = Appointment
    form_class = AppointmentForm
    success_message = 'The appointment was successfully added'
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
    success_message = 'The details of the appointment were successfully updated'
    form_class = AppointmentForm
    template_name = 'appointments/appointment_update_form.html'
    context_object_name = 'appointment'

    def form_valid(self, form):
        # set the owner as currently logged in user if none chosen in form
        if not form.instance.owner:
            form.instance.owner = self.request.owner

        return super(AppointmentUpdateView, self).form_valid(form)


class AppointmentListView(CommuniqueListAndExportView):
    """
    A view that lists available appointments.
    """
    model = Appointment
    template_name = 'appointments/appointment_list.html'
    context_object_name = 'appointment_list'

    def csv_export_response(self, context):
        # generate a csv for download
        today = datetime.date.today()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="all_appointments_{0}.csv"'.format(
            today.strftime(DATE_FORMAT))
        write_appointments_to_csv(response, context[self.context_object_name], DATE_FORMAT, DATE_FORMAT_STR)

        return response


class AppointmentDeleteView(CommuniqueDeleteView):
    """
    A view that handles deletion of an appointment.
    """
    model = Appointment
    success_message = 'The appointment was successfully deleted'
    success_url = reverse_lazy('appointments_appointment_list')
    context_object_name = 'appointment'
    template_name = 'appointments/appointment_confirm_delete.html'

    def test_func(self):
        # check that user is an active user
        return self.request.user.is_active


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
        appointments = Appointment.objects.filter(date_last_modified__range=[start_date, end_date])
        return appointments

    def csv_export_response(self, context):
        # generate an HTTP response with the csv file for download
        start_date = self.get_export_start_date()
        end_date = self.get_export_end_date()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="appointments_{0}_to_{1}.csv"'.format(
            start_date.strftime(DATE_FORMAT), end_date.strftime(DATE_FORMAT)
        )

        write_appointments_to_csv(response, context[self.context_object_name], DATE_FORMAT, DATE_FORMAT_STR)

        return response
