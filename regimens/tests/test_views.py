from django.core.urlresolvers import reverse

from communique.utils import ViewsTestCase

from regimens.models import Drug


class DrugCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to create a drug.
    """
    view_name = 'regimens_drug_create'
    view_template_name = 'regimens/drug_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class DrugListViewTestCase(ViewsTestCase):
    """
    Test cases for the view to list drugs
    """
    view_name = 'regimens_drug_list'
    view_template_name = 'regimens/drug_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)
        

class ExistingDrugViewsTestCase(ViewsTestCase):
    """
    Test cases for views that require an existing drug
    """
    def setUp(self):
        super(ExistingDrugViewsTestCase, self).setUp()
        Drug.objects.create(name='Sample Drug', description='Sample description')


class DrugDetailViewTestCase(ExistingDrugViewsTestCase):
    """
    Test cases for view to show the details of a drug
    """
    view_template_name = 'regimens/drug_view.html'

    def test_active_user_access(self):
        drug = Drug.objects.get(id=1)
        self.only_active_user_access_test(drug.get_absolute_url(), self.view_template_name)
