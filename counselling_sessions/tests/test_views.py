from django.core.urlresolvers import reverse

from communique.utils.utils_tests import ViewsTestCase

from counselling_sessions.models import CounsellingSessionType, CounsellingSession
from patients.models import Patient


class CounsellingSessionTypeListViewTestCase(ViewsTestCase):
    """
    Test cases for the view that lists counselling session types.
    """
    view_name = 'counselling_sessions_type_list'
    view_template_name = 'counselling_sessions/counselling_session_type_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class CounsellingSessionTypeCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to create a new session type.
    """
    view_name = 'counselling_sessions_type_create'
    view_template_name = 'counselling_sessions/counselling_session_type_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class ExistingCounsellingSessionTypeViewsTestCase(ViewsTestCase):
    """
    Test cases for a view that requires an existing Session Type
    """
    def setUp(self):
        super(ExistingCounsellingSessionTypeViewsTestCase, self).setUp()
        CounsellingSessionType.objects.create(name='Dummy Type')


class CounsellingSessionTypeDetailViewTestCase(ExistingCounsellingSessionTypeViewsTestCase):
    """
    Test cases for the view to display session type information.
    """
    view_template_name = 'counselling_sessions/counselling_session_type_view.html'

    def test_active_user_access(self):
        session_type = CounsellingSessionType.objects.get(id=1)
        self.only_active_user_access_test(session_type.get_absolute_url(), self.view_template_name)


class CounsellingSessionTypeUpdateViewTestCase(ExistingCounsellingSessionTypeViewsTestCase):
    """
    Test cases for the view to update a session type.
    """
    view_template_name = 'counselling_sessions/counselling_session_type_update_form.html'

    def test_active_user_access(self):
        session_type = CounsellingSessionType.objects.get(id=1)
        self.only_active_user_access_test(session_type.get_update_url(), self.view_template_name)


class CounsellingSessionTypeDeleteViewTestCase(ExistingCounsellingSessionTypeViewsTestCase):
    """
    Test cases for the view to delete a session type.
    """
    view_template_name = 'counselling_sessions/counselling_session_type_confirm_delete.html'

    def test_active_user_access(self):
        session_type = CounsellingSessionType.objects.get(id=1)
        self.only_active_user_access_test(session_type.get_delete_url(), self.view_template_name)


class CounsellingSessionListViewTestCase(ViewsTestCase):
    """
    Test cases for the view that lists counselling sessions.
    """
    view_name = 'counselling_sessions_session_list'
    view_template_name = 'counselling_sessions/counselling_session_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class CounsellingSessionCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to add a session.
    """
    view_name = 'counselling_sessions_session_create'
    view_template_name = 'counselling_sessions/counselling_session_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class CounsellingSessionExportFormViewTestCase(ViewsTestCase):
    """
    Test cases for the view that displays the export form
    """
    view_name = 'counselling_sessions_export_form'
    view_template_name = 'counselling_sessions/counselling_session_export_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class CounsellingSessionExportListViewTestCase(ViewsTestCase):
    view_name = 'counselling_sessions_export_list'
    view_template_name = 'counselling_sessions/counselling_session_export_list.html'
    view_url = reverse(view_name, kwargs={'start_year':'2000', 'start_month':'01', 'start_day':'01',
                                          'end_year':'2001', 'end_month':'01', 'end_day':'01'})

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class ExistingCounsellingSessionViewsTestCase(ViewsTestCase):
    """
    Test cases for views that require an existing counselling session
    """
    def setUp(self):
        super(ExistingCounsellingSessionViewsTestCase, self).setUp()
        session_type = CounsellingSessionType.objects.create(name='dummy type')
        patient = Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE, identifier='A001')
        CounsellingSession.objects.create(patient=patient, counselling_session_type=session_type)


class CounsellingSessionDetailViewTestCase(ExistingCounsellingSessionViewsTestCase):
    """
    Test cases for the view to display a session.
    """
    view_template_name = 'counselling_sessions/counselling_session_view.html'

    def test_active_user_access(self):
        counselling_session = CounsellingSession.objects.get(id=1)
        self.only_active_user_access_test(counselling_session.get_absolute_url(), self.view_template_name)


class CounsellingSessionUpdateViewTestCase(ExistingCounsellingSessionViewsTestCase):
    """
    Test cases for the view to update a session.
    """
    view_template_name = 'counselling_sessions/counselling_session_update_form.html'

    def test_active_user_access(self):
        counselling_session = CounsellingSession.objects.get(id=1)
        self.only_active_user_access_test(counselling_session.get_update_url(), self.view_template_name)


class CounsellingSessionDeleteViewTestCase(ExistingCounsellingSessionViewsTestCase):
    """
    Test cases for the view to delete a session.
    """
    view_template_name = 'counselling_sessions/counselling_session_confirm_delete.html'

    def test_active_user_access(self):
        counselling_session = CounsellingSession.objects.get(id=1)
        self.only_active_user_access_test(counselling_session.get_delete_url(), self.view_template_name)
