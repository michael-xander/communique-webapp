from django.test import TestCase
from django.core.urlresolvers import reverse

import datetime

from patients.models import Patient
from adverse.models import EmergencyContact, AdverseEventType, AdverseEvent


class EmergencyContactTestCase(TestCase):
    """
    Test cases for the emergency contact model
    """
    def setUp(self):
        EmergencyContact.objects.create(name='jon Snow', email='jon_snow@gmail.com')

    def test_str(self):
        """
        A test case for the __str__ method of the model
        """
        emergency_contact = EmergencyContact.objects.get(id=1)
        self.assertEqual(emergency_contact.__str__(), 'Jon Snow')


class AdverseEventTypeTestCase(TestCase):
    """
    Test cases for the adverse event type model
    """
    def setUp(self):
        AdverseEventType.objects.create(name='Sample type', description='Sample description')

    def test_str(self):
        """
        A test case for the __str__ method of the model
        """
        adverse_event_type = AdverseEventType.objects.get(id=1)
        self.assertEqual(adverse_event_type.__str__(), 'Sample Type')


class AdverseEventTestCase(TestCase):
    """
    Test cases for the adverse event model
    """
    def setUp(self):
        patient = Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE)
        adverse_event_type = AdverseEventType.objects.create(name='Sample Type', description='Sample description')
        AdverseEvent.objects.create(patient=patient, adverse_event_type=adverse_event_type,
                                    event_date=datetime.date.today())

    def test_str(self):
        """
        A test case for the __str__ method of the model
        """
        adverse_event = AdverseEvent.objects.get(id=1)
        self.assertEqual(adverse_event.__str__(),
                         "Sample Type adverse event for Jon Snow on {0}".format(adverse_event.event_date))

