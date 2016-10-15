from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class CommuniqueUser(User):
    """
    A proxy model for the default User model, adding extra methods.
    """
    class Meta:
        proxy = True

    def get_absolute_url(self):
        return reverse('user_communique_user_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('user_communique_user_update', kwargs={'pk':self.pk})


class Profile(User):
    """
    A proxy model for the default User model, masquerading as a Profile.
    """
    class Meta:
        proxy = True

    def get_absolute_url(self):
        return reverse('user_profile_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('user_profile_update', kwargs={'pk':self.pk})
