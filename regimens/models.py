from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Drug(models.Model):
    """
    A class representing a drug that is added to a patient's regimen.
    """
    name = models.CharField(verbose_name='Drug name', unique=True, max_length=100,
                            help_text='The unique name of the drug')
    description = models.TextField(verbose_name='Description', help_text='Information about the drug')

    date_created = models.DateField(auto_now_add=True, help_text='The date the drug was added to the system')
    date_last_modified = models.DateField(auto_now=True, help_text='The most recent date any of the information of this'
                                                                   ' drug was last modified')

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_drugs',
                                  related_query_name='created_drug', help_text='The user that added this drug to the '
                                                                               'system')
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='modified_drugs', related_query_name='modified_drug',
                                         help_text='The user that made the most recent modification to any of the fields'
                                                   ' of this drug')

    def save(self, *args, **kwargs):
        # store the name of the drug in lower case
        self.name = self.name.lower()
        super(Drug, self).save(*args, **kwargs)

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('regimens_drug_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('regimens_drug_update', kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('regimens_drug_delete', kwargs={'pk':self.pk})