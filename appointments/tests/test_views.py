from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

import datetime

from communique.utils import ViewsTestCase
from appointments.models import Appointment


class AppointmentCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to create an appointment.
    """
    view_name = 'appointments_appointment_create'
    view_template_name = 'appointments/appointment_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class AppointmentListViewTestCase(ViewsTestCase):
    """
    Test cases for the view to list appointments.
    """
    view_name = 'appointments_appointment_list'
    view_template_name = 'appointments/appointment_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class ExistingAppointmentViewTestCase(ViewsTestCase):
    """
    Test cases for a view that requires an existing appointment for testing.
    """
    def setUp(self):
        """
        Add an appointment to the test database.
        """
        super(ExistingAppointmentViewTestCase, self).setUp()

        owner = User.objects.create_user('appointment_user', 'appointmentuser@gmail.com', 'p@55words')
        appointment_date = datetime.date.today()
        start_time = datetime.time(1)
        end_time = datetime.time(2)

        Appointment.objects.create(title='a dummy appointment', owner=owner, appointment_date=appointment_date,
                                   start_time=start_time, end_time=end_time)


class AppointmentDetailViewTestCase(ExistingAppointmentViewTestCase):
    """
    Test cases for the view that displays an appointment's information.
    """
    view_template_name = 'appointments/appointment_view.html'

    def test_active_user_access(self):
        appointment = Appointment.objects.get(id=1)
        self.only_active_user_access_test(appointment.get_absolute_url(), self.view_template_name)


class AppointmentUpdateViewTestCase(ExistingAppointmentViewTestCase):
    """
    Test cases for the view that handles updating an appointment.
    """
    view_template_name = 'appointments/appointment_update_form.html'

    def test_active_user_access(self):
        appointment = Appointment.objects.get(id=1)
        self.only_active_user_access_test(appointment.get_update_url(), self.view_template_name)


class AppointmentDeleteViewTestCase(ExistingAppointmentViewTestCase):
    """
    Test cases for the view that handles appointment deletion.
    """
    view_template_name = 'appointments/appointment_confirm_delete.html'

    def test_active_user_access(self):
        appointment = Appointment.objects.get(id=1)
        self.only_active_user_access_test(appointment.get_delete_url(), self.view_template_name)


