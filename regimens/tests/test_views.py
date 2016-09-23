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