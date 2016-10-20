from django.test import TestCase
from django.core.urlresolvers import reverse

from programs.models import Program


class ProgramTestCase(TestCase):
    """
    Test cases for the Program model.
    """
    def setUp(self):
        self.program = Program.objects.create(name='Sample Program', description='sample description')

    def test_program_str(self):
        """
        A test case for the __str__ method of Program model.
        """
        self.assertEqual(self.program.__str__(), self.program.name)

    def test_get_absolute_url(self):
        """
        A test case for the get_absolute_url method of the Program model.
        """
        self.assertEqual(self.program.get_absolute_url(), reverse('programs_program_detail',
                                                                  kwargs={'pk':self.program.pk}))

    def test_get_update_url(self):
        """
        A test case for the get_update_url method of the Program model.
        """
        self.assertEqual(self.program.get_update_url(), reverse('programs_program_update',
                                                                kwargs={'pk':self.program.pk}))

    def test_get_delete_url(self):
        """
        A test case for the get_delete_url method of the Program model.
        """
        self.assertEqual(self.program.get_delete_url(), reverse('programs_program_delete',
                                                                kwargs={'pk':self.program.pk}))
