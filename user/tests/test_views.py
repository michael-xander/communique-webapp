"""
Contains test cases for the views of the user app.
"""
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


from user.models import CommuniqueUser, Profile

class UserViewsTestCase(TestCase):
    def setUp(self):
        """
        Creates a super user and a regular user to be used throughout testing.
        """
        User.objects.create_user('regular_user', 'regularuser@gmail.com',
            'p@55words')
        User.objects.create_superuser('super_user', 'superuser@gmail.com',
            'p@55words')

    def template_test(self, view_url, template_name):
        """
        Tests that the right template is used to the view.
        """
        self.client.login(username='super_user', password='p@55words')
        response = self.client.get(view_url)
        self.assertTemplateUsed(response, template_name)

    def context_object_test(self, view_url, context_object_name):
        """
        Tests that the context object with the provided name is generated by the
        view.
        """
        self.client.login(username='super_user', password='p@55words')
        response = self.client.get(view_url)
        self.assertTrue(response.context[context_object_name])

"""
Test cases for the views handling the CommuniqueUser model.
"""
class CommuniqueUserViewsTestCase(UserViewsTestCase):
    def only_superuser_access_test(self, view_url, template_name):
        """
        Tests that only a superuser can access the view.

        If the user is not a superuser, he or she is redirected to the login
        page.
        """
        super_user = CommuniqueUser.objects.get(username='super_user')
        self.assertTrue(super_user.is_superuser)
        self.client.force_login(super_user)
        response = self.client.get(view_url, follow=True)
        self.assertTemplateUsed(response, template_name)
        self.client.logout()

        regular_user = CommuniqueUser.objects.get(username='regular_user')
        self.assertFalse(regular_user.is_superuser)
        self.client.force_login(regular_user)
        response = self.client.get(view_url, follow=True)
        self.assertTemplateUsed(response, 'user/login.html')

class CommuniqueUserAccessViewsTestCase(CommuniqueUserViewsTestCase):
    """
    Test cases for the login and logout views.
    """

    def test_login(self):
        """
        Test that login occurs on providing the right credentials.
        """
        self.assertFalse(self.client.login(username='dumb', password='secret'))
        self.assertTrue(self.client.login(username='super_user',
            password='p@55words'))

    def test_login_view_template(self):
        view_url = reverse('user_login')
        template_name = 'user/login.html'
        self.template_test(view_url, template_name)

    def test_logout_view_template(self):
        view_url = reverse('user_logout')
        template_name = 'user/logout.html'
        self.template_test(view_url, template_name)

class CommuniqueUserListViewTestCase(CommuniqueUserViewsTestCase):
    """
    Test cases for the user list view.
    """
    view_name = 'user_communique_user_list'
    view_template_name = 'user/communique_user_list.html'
    view_context_object_name = 'communique_user_list'
    view_url = reverse(view_name)

    def test_template(self):
        self.template_test(self.view_url, self.view_template_name)

    def test_only_superuser_access(self):
        self.only_superuser_access_test(self.view_url, self.view_template_name)

    def test_context_object(self):
        self.context_object_test(self.view_url, self.view_context_object_name)

class CommuniqueUserCreateViewTestCase(CommuniqueUserViewsTestCase):
    """
    Test cases for the view to create users.
    """
    view_name = 'user_communique_user_create'
    view_template_name = 'user/communique_user_form.html'
    view_url = reverse(view_name)

    def test_template(self):
        self.template_test(self.view_url, self.view_template_name)

    def test_only_superuser_access(self):
        self.only_superuser_access_test(self.view_url, self.view_template_name)

class CommuniqueUserDetailViewTestCase(CommuniqueUserViewsTestCase):
    """
    Test cases for the view to see user details.
    """
    view_name = 'user_communique_user_detail'
    view_template_name = 'user/communique_user_view.html'
    view_context_object_name = 'communique_user'
    view_url = reverse(view_name, kwargs={'pk':1})

    def test_template(self):
        self.template_test(self.view_url, self.view_template_name)

    def test_only_superuser_access(self):
        self.only_superuser_access_test(self.view_url, self.view_template_name)

    def test_context_object(self):
        self.context_object_test(self.view_url, self.view_context_object_name)

class CommuniqueUserUpdateViewTestCase(CommuniqueUserViewsTestCase):
    """
    Test cases for the view to update user active and superuser status.
    """
    view_name = 'user_communique_user_update'
    view_template_name = 'user/communique_user_update_form.html'
    view_context_object_name = 'communique_user'
    view_url = reverse(view_name, kwargs={'pk':1})

    def test_template(self):
        self.template_test(self.view_url, self.view_template_name)

    def test_context_object(self):
        self.context_object_test(self.view_url, self.view_context_object_name)

    def test_only_superuser_access(self):
        self.only_superuser_access_test(self.view_url, self.view_template_name)


"""
Test cases for the views handling the Profile model.
"""
class ProfileViewsTestCase(UserViewsTestCase):
    def only_current_user_access_test(self, view_url, template_name):
        """
        Tests whether the user requesting this Profile view owns the Profile.

        If the user doesn't own the profile, he/she is redirected to the login
        page.
        """
        # regular user is created first and therefore has id/pk=1
        regular_user = Profile.objects.get(username='regular_user')
        self.assertTrue(regular_user.pk == 1)
        self.client.force_login(regular_user)
        response = self.client.get(view_url, follow=True)
        self.assertTemplateUsed(response, template_name)
        self.client.logout()

        # super user is created second and therefore has id/pk=1
        super_user = Profile.objects.get(username='super_user')
        self.assertTrue(super_user.pk == 2)
        self.client.force_login(super_user)
        response = self.client.get(view_url, follow=True)
        self.assertTemplateUsed(response, 'user/login.html')


class ProfileDetailViewTestCase(ProfileViewsTestCase):
    """
    Test cases for the detail view for a Profile.
    """
    view_name = 'user_profile_detail'
    view_template_name = 'user/profile_view.html'
    view_context_object_name = 'user_profile'

    def test_only_current_user_access(self):
        view_url = reverse(self.view_name, kwargs={'pk':1})
        self.only_current_user_access_test(view_url, self.view_template_name)

    def test_template(self):
        # access is available through the super_user with pk=2
        view_url = reverse(self.view_name, kwargs={'pk':2})
        self.template_test(view_url, self.view_template_name)

    def test_context_object(self):
        # access is available through the super_user with pk=2
        view_url = reverse(self.view_name, kwargs={'pk':2})
        self.context_object_test(view_url, self.view_context_object_name)

class ProfileUpdateViewTestCase(ProfileViewsTestCase):
    """
    Test cases for the update view for a Profile.
    """
    view_name = 'user_profile_update'
    view_template_name = 'user/profile_update_form.html'
    view_context_object_name = 'user_profile'

    def test_only_current_user_access(self):
        view_url = reverse(self.view_name, kwargs={'pk':1})
        self.only_current_user_access_test(view_url, self.view_template_name)

    def test_template(self):
        # access is available through the super_user with pk=2
        view_url = reverse(self.view_name, kwargs={'pk':2})
        self.template_test(view_url, self.view_template_name)

    def test_context_object(self):
        # access is available through the super_user with pk=2
        view_url = reverse(self.view_name, kwargs={'pk':2})
        self.context_object_test(view_url, self.view_context_object_name)
