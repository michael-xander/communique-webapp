from django.test import TestCase
from django.contrib.auth.models import User

from appointments.forms import AppointmentForm

from patients.models import Patient

import datetime


class AppointmentFormTestCase(TestCase):
    """
    Test cases for the appointment form.
    """

    def setUp(self):
        User.objects.create_superuser('jon_snow', 'jonsnow@gmail.com', 'p@55words')
        Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE)

    def test_time_validation(self):
        """
        Tests that the clean method invalidates submissions where start time is greater or equal to end time.
        """

        appointment_date = datetime.date.today()
        start_time = datetime.time(1)
        end_time = datetime.time(start_time.hour + 1)
        title = 'A dummy title'

        form = AppointmentForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

        # data when start time < endtime
        data = {'title':title, 'appointment_date':appointment_date, 'start_time':start_time, 'patient':1,
                'owner':1, 'end_time':end_time}
        self.assertTrue(data['start_time'] < data['end_time'])

        form = AppointmentForm(data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

        # reverse the start time and end time
        data['start_time'] = end_time
        data['end_time'] = start_time

        self.assertTrue(data['start_time'] > data['end_time'])

        form = AppointmentForm(data)
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())

    def test_date_validation(self):
        """
        Tests that the provided appointment date is not set in the past.
        """

        appointment_date = datetime.date.today()
        start_time = datetime.time(1)
        end_time = datetime.time(start_time.hour + 1)
        title = 'A dummy title'

        form = AppointmentForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

        data = {'title':title, 'appointment_date':appointment_date, 'start_time':start_time, 'patient':1, 'owner':1,
                'end_time':end_time}

        current_date  = datetime.date.today()

        self.assertFalse(data['appointment_date'] < current_date)

        form = AppointmentForm(data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

        one_day = datetime.timedelta(days=1)

        tomorrow = current_date + one_day

        data['appointment_date'] = tomorrow

        self.assertFalse(data['appointment_date'] < current_date)
        form = AppointmentForm(data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

        yesterday = current_date - one_day

        data['appointment_date'] = yesterday

        self.assertTrue(data['appointment_date'] < current_date)
        form = AppointmentForm(data)
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())



