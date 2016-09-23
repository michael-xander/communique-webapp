from django.test import TestCase
from django.core.urlresolvers import reverse

from regimens.models import Drug


class DrugTestCase(TestCase):
    """
    Test cases for the Drug model.
    """
    def setUp(self):
        Drug.objects.create(name='a Drug', description='A drug description')

    def test_str(self):
        """
        A test case for the __str__ method of the model
        """
        drug = Drug.objects.get(id=1)
        self.assertEqual(drug.__str__(), 'A Drug')