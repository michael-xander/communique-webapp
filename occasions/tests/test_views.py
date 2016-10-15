from django.core.urlresolvers import reverse

import datetime

from communique.utils.utils_tests import ViewsTestCase
from occasions.models import Event


class EventCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to create an event.
    """
    view_name = 'occasions_event_create'
    view_template_name = 'occasions/event_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class EventListViewTestCase(ViewsTestCase):
    """
    Test cases for the view to list events.
    """
    view_name = 'occasions_event_list'
    view_template_name = 'occasions/event_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class ExistingEventViewTestCase(ViewsTestCase):
    """
    Test cases for a view that requires an existing event for testing
    """
    def setUp(self):
        """
        Add an event to the test database.
        """
        super(ExistingEventViewTestCase, self).setUp()

        event_date = datetime.date.today()
        start_time = datetime.time(1)
        end_time = datetime.time(2)

        Event.objects.create(name='a dummy name', event_date=event_date, start_time=start_time, end_time=end_time)


class EventDetailViewTestCase(ExistingEventViewTestCase):
    """
    Test cases for the view that displays an event's information.
    """
    view_template_name = 'occasions/event_view.html'

    def test_active_user_access(self):
        event = Event.objects.get(id=1)
        self.only_active_user_access_test(event.get_absolute_url(), self.view_template_name)


class EventUpdateViewTestCase(ExistingEventViewTestCase):
    """
    Test cases for the view that handles updating an event
    """
    view_template_name = 'occasions/event_update_form.html'

    def test_active_user_access(self):
        event = Event.objects.get(id=1)
        self.only_active_user_access_test(event.get_update_url(), self.view_template_name)


class EventDeleteViewTestCase(ExistingEventViewTestCase):
    """
    Test cases for the view that handles event deletion.
    """
    view_template_name = 'occasions/event_confirm_delete.html'

    def test_active_super_user_access(self):
        event = Event.objects.get(id=1)
        self.only_active_super_user_access_test(event.get_delete_url(), self.view_template_name)