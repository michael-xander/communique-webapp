from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django import forms
from django.forms import ModelForm

from .models import CommuniqueUser, Profile, NotificationRegistration


class CommuniqueUserCreationForm(UserCreationForm):
    """
    A form used to register a new Communiqué user.
    """
    class Meta (UserCreationForm.Meta):
        model = CommuniqueUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'is_superuser', 'email',)

    def clean_first_name(self):
        # check that a first name has been given to the user
        first_name = self.cleaned_data.get('first_name')

        if not first_name:
            raise forms.ValidationError('The user must have a first name', code='invalid')

        return first_name

    def clean_last_name(self):
        # check that a last name has been given to the user
        last_name = self.cleaned_data.get('last_name')

        if not last_name:
            raise forms.ValidationError('The user must have a last name', code='invalid')

        return last_name


class CommuniqueUserSetPasswordForm(SetPasswordForm):
    """
    A form used to update the password of a user without requesting for the current password
    """
    class Meta (SetPasswordForm.Meta):
        model = CommuniqueUser
        fields = SetPasswordForm.Meta.fields


class CommuniqueUserUpdateForm(ModelForm):
    """
    A form used to update a user's active and superuser status.
    """
    class Meta:
        model = CommuniqueUser
        fields = ['is_active', 'is_superuser']


class NotificationRegistrationForm(ModelForm):
    """
    A form used to create a notification registration
    """
    class Meta:
        model = NotificationRegistration
        fields = ['service']


class ProfileUpdateForm(ModelForm):
    """
    A form used to update a user profile's information
    """
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email']

    def clean_first_name(self):
        # check that the first name field is not empty
        first_name = self.cleaned_data.get('first_name')

        if not first_name:
            raise forms.ValidationError('A first name must be provided', code='invalid')

        return first_name

    def clean_last_name(self):
        # check that the last name field is not empty
        last_name = self.cleaned_data.get('last_name')

        if not last_name:
            raise forms.ValidationError('A last name must be provided', code='invalid')

        return last_name
