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
        EmergencyContact.objects.create(name='Jon Snow', email='jon_snow@gmail.com')

    def test_str(self):
        """
        A test case for the __str__ method of the model
        """
        emergency_contact = EmergencyContact.objects.get(id=1)
        self.assertEqual(emergency_contact.__str__(), 'Jon Snow')

    def test_get_absolute_url(self):
        """
        A test case for the get_absolute_url method of the model
        """
        emergency_contact = EmergencyContact.objects.get(id=1)
        self.assertEqual(emergency_contact.get_absolute_url(), reverse('adverse_emergency_contact_detail',
                                                                       kwargs={'pk':emergency_contact.pk}))

    def test_get_update_url(self):
        """
        A test case for the get_update_url method of the model
        """
        emergency_contact = EmergencyContact.objects.get(id=1)
        self.assertEqual(emergency_contact.get_update_url(), reverse('adverse_emergency_contact_update',
                                                                       kwargs={'pk': emergency_contact.pk}))

    def test_get_delete_url(self):
        """
        A test case for the get_delete_url method of the model
        """
        emergency_contact = EmergencyContact.objects.get(id=1)
        self.assertEqual(emergency_contact.get_delete_url(), reverse('adverse_emergency_contact_delete',
                                                                       kwargs={'pk':emergency_contact.pk}))


class AdverseEventTypeTestCase(TestCase):
    """
    Test cases for the adverse event type model
    """
    def setUp(self):
        AdverseEventType.objects.create(name='Sample Type', description='Sample description')

    def test_str(self):
        """
        A test case for the __str__ method of the model
        """
        adverse_event_type = AdverseEventType.objects.get(id=1)
        self.assertEqual(adverse_event_type.__str__(), 'Sample Type')

    def test_get_absolute_url(self):
        """
        A test case for the get_absolute_url of the model
        """
        adverse_event_type = AdverseEventType.objects.get(id=1)
        self.assertEqual(adverse_event_type.get_absolute_url(), reverse('adverse_event_type_detail',
                                                                        kwargs={'pk':adverse_event_type.pk}))

    def test_get_update_url(self):
        """
        A test case for the get_update_url of the model
        """
        adverse_event_type = AdverseEventType.objects.get(id=1)
        self.assertEqual(adverse_event_type.get_update_url(), reverse('adverse_event_type_update',
                                                                        kwargs={'pk':adverse_event_type.pk}))

    def test_get_delete_url(self):
        """
        A test case for the get_delete_url of the model
        """
        adverse_event_type = AdverseEventType.objects.get(id=1)
        self.assertEqual(adverse_event_type.get_delete_url(), reverse('adverse_event_type_delete',
                                                                        kwargs={'pk':adverse_event_type.pk}))


class AdverseEventTestCase(TestCase):
    """
    Test cases for the adverse event model
    """
    def setUp(self):
        patient = Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE, identifier='A001')
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

    def test_get_absolute_url(self):
        """
        A test for the get_absolute_url method of the model
        """
        adverse_event = AdverseEvent.objects.get(id=1)
        self.assertEqual(adverse_event.get_absolute_url(), reverse('adverse_event_detail',
                                                                   kwargs={'pk':adverse_event.pk}))

    def test_get_update_url(self):
        """
        A test for the get_update_url method of the model
        """
        adverse_event = AdverseEvent.objects.get(id=1)
        self.assertEqual(adverse_event.get_update_url(), reverse('adverse_event_update',
                                                                   kwargs={'pk':adverse_event.pk}))

    def test_get_delete_url(self):
        """
        A test for the get_delete_url method of the model
        """
        adverse_event = AdverseEvent.objects.get(id=1)
        self.assertEqual(adverse_event.get_delete_url(), reverse('adverse_event_delete',
                                                                   kwargs={'pk':adverse_event.pk}))

