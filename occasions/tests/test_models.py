from django.test import TestCase
from django.core.urlresolvers import reverse

import datetime

from occasions.models import Event


class EventTestCase(TestCase):
    """
    Test cases for the Event model.
    """
    def setUp(self):
        event_date = datetime.date.today()
        start_time = datetime.time(1)
        end_time = datetime.time(2)
        Event.objects.create(name='A dummy event', event_date=event_date, start_time=start_time, end_time=end_time)

    def test_str(self):
        """
        Tests the __str__ method of the model
        """
        event = Event.objects.get(id=1)
        self.assertEqual(event.__str__(), 'A dummy event')

    def test_get_absolute_url(self):
        """
        Tests the get_absolute_url method of the model
        """
        event = Event.objects.get(id=1)
        self.assertEqual(event.get_absolute_url(), reverse('occasions_event_detail', kwargs={'pk':event.pk}))

    def test_get_update_url(self):
        """
        Tests the get_update_url method of the model
        """
        event = Event.objects.get(id=1)
        self.assertEqual(event.get_update_url(), reverse('occasions_event_update', kwargs={'pk':event.pk}))

    def test_get_delete_url(self):
        """
        Test the get_delete_url method of the model
        """
        event = Event.objects.get(id=1)
        self.assertEqual(event.get_delete_url(), reverse('occasions_event_delete', kwargs={'pk':event.pk}))
