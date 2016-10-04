from django.test import TestCase

from django.core.urlresolvers import reverse

from counselling_sessions.models import CounsellingSession, CounsellingSessionType
from patients.models import Patient


class CounsellingSessionTypeTestCase(TestCase):
    """
    Test cases for the CounsellingSessionType model.
    """

    def setUp(self):
        CounsellingSessionType.objects.create(name='dummy type')

    def test_counselling_session_type_str(self):
        """
        A test case for the __str__ method of the model.
        """
        session_type = CounsellingSessionType.objects.get(id=1)
        self.assertEqual(session_type.__str__(), 'Dummy Type')

    def test_get_absolute_url(self):
        """
        A test case for the get_absolute_url method for the model.
        """
        session_type = CounsellingSessionType.objects.get(id=1)
        self.assertEqual(session_type.get_absolute_url(), reverse('counselling_sessions_type_detail',
                                                                              kwargs={'pk':session_type.pk}))

    def test_get_update_url(self):
        """
        A test case for the get_update_url method for the model.
        """
        session_type = CounsellingSessionType.objects.get(id=1)
        self.assertEqual(session_type.get_update_url(), reverse('counselling_sessions_type_update',
                                                                            kwargs={'pk':session_type.pk}))

    def test_get_delete_url(self):
        """
        A test case for the get_delete_url method for the model.
        """
        session_type = CounsellingSessionType.objects.get(id=1)
        self.assertEqual(session_type.get_delete_url(), reverse('counselling_sessions_type_delete',
                                                                kwargs={'pk':session_type.pk}))


class CounsellingSessionTestCase(TestCase):
    """
    Test cases for the CounsellingSession model.
    """
    def setUp(self):
        session_type = CounsellingSessionType.objects.create(name='dummy type')
        patient = Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE, identifier='A001')
        CounsellingSession.objects.create(patient=patient, counselling_session_type=session_type)

    def test_counselling_session_str(self):
        """
        A test case for the __str__ method of the model.
        """
        counselling_session = CounsellingSession.objects.get(id=1)
        self.assertEqual(counselling_session.__str__(), 'A Dummy Type session for Jon Snow')

    def test_get_absolute_url(self):
        """
        A test case for the get_absolute_url method of the model.
        """
        counselling_session = CounsellingSession.objects.get(id=1)
        self.assertEqual(counselling_session.get_absolute_url(), reverse('counselling_sessions_session_detail',
                                                                         kwargs={'pk':counselling_session.pk}))

    def test_get_update_url(self):
        """
        A test case for the get_update_url method of the model.
        """
        counselling_session = CounsellingSession.objects.get(id=1)
        self.assertEqual(counselling_session.get_update_url(), reverse('counselling_sessions_session_update',
                                                                       kwargs={'pk':counselling_session.pk}))

    def test_get_delete_url(self):
        """
        A test case for the get_delete_url method of the model.
        """
        counselling_session = CounsellingSession.objects.get(id=1)
        self.assertEqual(counselling_session.get_delete_url(), reverse('counselling_sessions_session_delete',
                                                                       kwargs={'pk':counselling_session.pk}))