from django.core.urlresolvers import reverse_lazy

from communique.views import (CommuniqueDeleteView, CommuniqueListView, CommuniqueDetailView, CommuniqueUpdateView,
                              CommuniqueCreateView)
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
