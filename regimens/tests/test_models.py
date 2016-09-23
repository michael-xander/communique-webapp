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

    def test_get_absolute_url(self):
        """
        A method that tests the get_absolute_url method of a model
        """
        drug = Drug.objects.get(id=1)
        self.assertEqual(drug.get_absolute_url(), reverse('regimens_drug_detail', kwargs={'pk':drug.pk}))