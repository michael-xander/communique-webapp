from django.core.urlresolvers import reverse

import datetime

from communique.utils import ViewsTestCase

from regimens.models import Drug, Regimen
from patients.models import Patient


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


class DrugUpdateViewTestCase(ExistingDrugViewsTestCase):
    """
    Test cases for view to update the details of a drug
    """
    view_template_name = 'regimens/drug_update_form.html'

    def test_active_user_access(self):
        drug = Drug.objects.get(id=1)
        self.only_active_user_access_test(drug.get_update_url(), self.view_template_name)


class DrugDeleteViewTestCase(ExistingDrugViewsTestCase):
    """
    Test cases for view to delete the details of a drug
    """
    view_template_name = 'regimens/drug_confirm_delete.html'

    def test_active_user_access(self):
        drug = Drug.objects.get(id=1)
        self.only_active_user_access_test(drug.get_delete_url(), self.view_template_name)


class RegimenListViewTestCase(ViewsTestCase):
    """
    Test cases for view to list regimens
    """
    view_name = 'regimens_regimen_list'
    view_template_name = 'regimens/regimen_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class RegimenCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to create a regimen
    """
    view_name = 'regimens_regimen_create'
    view_template_name = 'regimens/regimen_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class ExistingRegimenViewsTestCase(ViewsTestCase):
    """
    Test cases for views that require an existing regimen
    """
    def setUp(self):
        super(ExistingRegimenViewsTestCase, self).setUp()
        patient = Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE)
        Regimen.objects.create(patient=patient, notes='Sample notes', date_started=datetime.date.today())


class RegimenDetailViewTestCase(ExistingRegimenViewsTestCase):
    """
    Test cases for view to show the details of a regimen
    """
    view_template_name = 'regimens/regimen_view.html'

    def test_active_user_access(self):
        regimen = Regimen.objects.get(id=1)
        self.only_active_user_access_test(regimen.get_absolute_url(), self.view_template_name)


class RegimenDeleteViewTestCase(ExistingRegimenViewsTestCase):
    """
    Test cases for view to handle deletion of a regimen
    """
    view_template_name = 'regimens/regimen_confirm_delete.html'

    def test_active_user_access(self):
        regimen = Regimen.objects.get(id=1)
        self.only_active_user_access_test(regimen.get_delete_url(), self.view_template_name)