from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse

# Create your models here.
class Service(models.Model):
    """
    A class representing a support service by MSF.
    A support service has both a name and description and is provided to
    patients.
    """
    name = models.CharField(verbose_name="Name", unique=True,
                            max_length=100)
    description = models.TextField(verbose_name="Description")
    # slug used to create unique url for service
    slug = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('support_services_service_detail', kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('support_services_service_update', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('support_services_service_delete', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        # make sure that the name is saved in lower case
        self.name = self.name.lower()
        self.slug = slugify(self.name, allow_unicode=True)
        super(Service, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']
