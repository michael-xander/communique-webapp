from django.core.urlresolvers import reverse

import datetime

from communique.utils import ViewsTestCase

from patients.models import Patient
from adverse.models import EmergencyContact, AdverseEvent, AdverseEventType


class EmergencyContactCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to create an emergency contact
    """
    view_name = 'adverse_emergency_contact_create'
    view_template_name = 'adverse/emergency_contact_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class EmergencyContactListViewTestCase(ViewsTestCase):
    """
    Test cases for the view to list emergency contacts
    """
    view_name = 'adverse_emergency_contact_list'
    view_template_name = 'adverse/emergency_contact_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class ExistingEmergencyContactViewsTestCase(ViewsTestCase):
    """
    Test cases for views that require an existing emergency contact
    """
    def setUp(self):
        super(ExistingEmergencyContactViewsTestCase, self).setUp()
        EmergencyContact.objects.create(name='Jon Snow', email='jon_snow@gmail.com')


class EmergencyContactDetailViewTestCase(ExistingEmergencyContactViewsTestCase):
    """
    Test cases for view to show the details of an emergency contact
    """
    view_template_name = 'adverse/emergency_contact_view.html'

    def test_active_user_access(self):
        emergency_contact = EmergencyContact.objects.get(id=1)
        self.only_active_user_access_test(emergency_contact.get_absolute_url(), self.view_template_name)


class EmergencyContactUpdateViewTestCase(ExistingEmergencyContactViewsTestCase):
    """
    Test cases for view that handles updating an emergency contact
    """
    view_template_name = 'adverse/emergency_contact_update_form.html'

    def test_active_user_access(self):
        emergency_contact = EmergencyContact.objects.get(id=1)
        self.only_active_user_access_test(emergency_contact.get_update_url(), self.view_template_name)


class EmergencyContactDeleteViewTestCase(ExistingEmergencyContactViewsTestCase):
    """
    Test cases for view that handles deletion of an emergency contact
    """
    view_template_name = 'adverse/emergency_contact_confirm_delete.html'

    def test_active_user_access(self):
        emergency_contact = EmergencyContact.objects.get(id=1)
        self.only_active_user_access_test(emergency_contact.get_delete_url(), self.view_template_name)


class AdverseEventTypeCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to create an adverse event type
    """
    view_name = 'adverse_event_type_create'
    view_template_name = 'adverse/adverse_event_type_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class AdverseEventTypeListViewTestCase(ViewsTestCase):
    """
    Test cases for the view that lists adverse event types
    """
    view_name = 'adverse_event_type_list'
    view_template_name = 'adverse/adverse_event_type_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class ExistingAdverseEventTypeViewsTestCase(ViewsTestCase):
    """
    Test cases for views that require an existing adverse event type
    """
    def setUp(self):
        super(ExistingAdverseEventTypeViewsTestCase, self).setUp()
        AdverseEventType.objects.create(name='Sample Type', description='Sample description')


class AdverseEventTypeDetailViewTestCase(ExistingAdverseEventTypeViewsTestCase):
    """
    Test cases for view to show details of an adverse event type
    """
    view_template_name = 'adverse/adverse_event_type_view.html'

    def test_active_user_access(self):
        adverse_event_type = AdverseEventType.objects.get(id=1)
        self.only_active_user_access_test(adverse_event_type.get_absolute_url(), self.view_template_name)


class AdverseEventTypeUpdateViewTestCase(ExistingAdverseEventTypeViewsTestCase):
    """
    Test cases for view to handle updating an adverse event type
    """
    view_template_name = 'adverse/adverse_event_type_update_form.html'

    def test_active_user_access(self):
        adverse_event_type = AdverseEventType.objects.get(id=1)
        self.only_active_user_access_test(adverse_event_type.get_update_url(), self.view_template_name)


class AdverseEventTypeDeleteViewTestCase(ExistingAdverseEventTypeViewsTestCase):
    """
    Test cases for view to handle deletion of an adverse event type
    """
    view_template_name = 'adverse/adverse_event_type_confirm_delete.html'

    def test_active_user_access(self):
        adverse_event_type = AdverseEventType.objects.get(id=1)
        self.only_active_user_access_test(adverse_event_type.get_delete_url(), self.view_template_name)


class AdverseEventCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to create an adverse event
    """
    view_name = 'adverse_event_create'
    view_template_name = 'adverse/adverse_event_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class AdverseEventListViewTestCase(ViewsTestCase):
    """
    Test cases for the view to list the adverse events
    """
    view_name = 'adverse_event_list'
    view_template_name = 'adverse/adverse_event_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class ExistingAdverseEventViewsTestCase(ViewsTestCase):
    """
    Test cases for views that require an existing adverse event
    """
    def setUp(self):
        super(ExistingAdverseEventViewsTestCase, self).setUp()
        patient = Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE)
        adverse_event_type = AdverseEventType.objects.create(name='Sample Type', description='Sample description')
        AdverseEvent.objects.create(patient=patient, adverse_event_type=adverse_event_type,
                                    event_date=datetime.date.today())


class AdverseEventDetailViewTestCase(ExistingAdverseEventViewsTestCase):
    """
    Test cases for view to show details of adverse event
    """
    view_template_name = 'adverse/adverse_event_view.html'

    def test_active_user_access(self):
        adverse_event = AdverseEvent.objects.get(id=1)
        self.only_active_user_access_test(adverse_event.get_absolute_url(), self.view_template_name)


class AdverseEventUpdateViewTestCase(ExistingAdverseEventViewsTestCase):
    """
    Test cases for view to handle updating an adverse event
    """
    view_template_name = 'adverse/adverse_event_update_form.html'

    def test_active_user_access(self):
        adverse_event = AdverseEvent.objects.get(id=1)
        self.only_active_user_access_test(adverse_event.get_update_url(), self.view_template_name)


class AdverseEventDeleteViewTestCase(ExistingAdverseEventViewsTestCase):
    """
    Test cases for view to handle deleting an adverse event
    """
    view_template_name = 'adverse/adverse_event_confirm_delete.html'

    def test_active_user_access(self):
        adverse_event = AdverseEvent.objects.get(id=1)
        self.only_active_user_access_test(adverse_event.get_delete_url(), self.view_template_name)