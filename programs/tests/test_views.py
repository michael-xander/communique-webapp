"""
This file contains test cases for views of the programs app.
"""
from django.core.urlresolvers import reverse

from communique.utils import ViewsTestCase

from programs.models import Program


class ProgramListViewTestCase(ViewsTestCase):
    """
    Test cases for the view that lists programs.
    """
    view_name = 'programs_program_list'
    view_template_name = 'programs/program_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class ProgramCreateViewTestCase(ViewsTestCase):
    """
    Test cases for view to create a program.
    """
    view_name = 'programs_program_create'
    view_template_name = 'programs/program_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class ExistingProgramViewsTestCase(ViewsTestCase):
    """
    Test cases for views that require an existing program
    """
    def setUp(self):
        super(ExistingProgramViewsTestCase, self).setUp()
        Program.objects.create(name='Sample Program', description='Sample Description')


class ProgramDetailViewTestCase(ExistingProgramViewsTestCase):
    """
    Test cases for view to show the details of a program.
    """
    view_template_name = 'programs/program_view.html'

    def test_active_user_access(self):
        program = Program.objects.get(id=1)
        self.only_active_user_access_test(program.get_absolute_url(), self.view_template_name)


class ProgramUpdateViewTestCase(ExistingProgramViewsTestCase):
    """
    Test cases for view to update the details of a program.
    """
    view_template_name = 'programs/program_update_form.html'

    def test_active_user_access(self):
        program = Program.objects.get(id=1)
        self.only_active_user_access_test(program.get_update_url(), self.view_template_name)


class ProgramDeleteViewTestCase(ExistingProgramViewsTestCase):
    """
    Test cases for view to delete a program.
    """
    view_template_name = 'programs/program_confirm_delete.html'

    def test_active_user_access(self):
        program = Program.objects.get(id=1)
        self.only_active_user_access_test(program.get_delete_url(), self.view_template_name)

