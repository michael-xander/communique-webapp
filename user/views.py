from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from notifications.models import Notification

from communique.views import (CommuniqueListView, CommuniqueDetailView, CommuniqueUpdateView, CommuniqueCreateView,
                              CommuniqueTemplateView, CommuniqueDeleteView, CommuniqueFormView)
from .forms import CommuniqueUserCreationForm, CommuniqueUserUpdateForm, ProfileUpdateForm, NotificationRegistrationForm
from .models import CommuniqueUser, Profile, NotificationRegistration
from occasions.models import Event


class CommuniqueUserListView(CommuniqueListView):
    """
    A view to list all users of the system.
    """
    model = CommuniqueUser
    template_name = 'user/communique_user_list.html'
    context_object_name = 'communique_user_list'

    def test_func(self):
        """
        Returns whether the user making the request is a superuser and is active.
        """
        current_user = self.request.user
        return current_user.is_superuser and current_user.is_active


class CommuniqueUserCreateView(CommuniqueCreateView):
    """
    A view to create a Communique user.
    """
    form_class = CommuniqueUserCreationForm
    model = CommuniqueUser
    template_name = 'user/communique_user_form.html'

    def test_func(self):
        """
        Returns whether the user making the request is an active superuser.
        """
        current_user = self.request.user
        return current_user.is_superuser and current_user.is_active


class CommuniqueUserDetailView(CommuniqueDetailView):
    """
    A view to display information of a user.
    """
    model = CommuniqueUser
    template_name = 'user/communique_user_view.html'
    context_object_name = 'communique_user'

    def test_func(self):
        """
        Returns whether the user making the request is an active superuser.
        """
        current_user = self.request.user
        return current_user.is_active and current_user.is_superuser


class CommuniqueUserUpdateView(CommuniqueUpdateView):
    """
    A view to update the information for a user.
    """
    form_class = CommuniqueUserUpdateForm
    model = CommuniqueUser
    template_name = 'user/communique_user_update_form.html'
    context_object_name = 'communique_user'

    def test_func(self):
        """
        Returns whether the user making the request is a superuser.
        """
        return self.request.user.is_superuser


class ProfileDetailView(CommuniqueDetailView):
    """
    A view to display the details of a user.
    """
    model = Profile
    template_name = 'user/profile_view.html'
    context_object_name = 'user_profile'

    def test_func(self):
        """
        Returns whether the user is making request to view his/her profile and is an active user.
        """
        return (str(self.request.user.pk) == str(self.kwargs['pk'])) and self.request.user.is_active


class ProfileUpdateView(CommuniqueUpdateView):
    """
    A view to update a user's profile.
    """
    form_class = ProfileUpdateForm
    model = Profile
    template_name = 'user/profile_update_form.html'
    context_object_name = 'user_profile'

    def test_func(self):
        """
        Returns whether the user making requests to his/her own profiles and is an active user.
        """
        return (str(self.request.user.pk) == str(self.kwargs['pk'])) and self.request.user.is_active


class ProfileNotificationListView(CommuniqueListView):
    """
    A view that lists a user's notifications
    """
    model = Notification
    template_name = 'user/profile_notification_list.html'
    context_object_name = 'notification_list'

    def get_queryset(self):
        # get all the unread notifications of the user making the request
        user = User.objects.get(pk=int(self.request.user.pk))
        user.notifications.mark_all_as_read()
        notification_list = user.notifications.all()

        paginator = Paginator(notification_list, 50) # show 100 notifications per page
        page = self.request.GET.get('page')

        try:
            notifications = paginator.page(page)
        except PageNotAnInteger:
            # if page is not an integer, deliver first page
            notifications = paginator.page(1)
        except EmptyPage:
            # if page is out of range (e.g 9999), deliver last page of results
            notifications = paginator.page(paginator.num_pages)

        # mark the notifications on this page as read
        for notification in notifications:
            notification.mark_as_read()

        return notifications


class CalendarView(CommuniqueTemplateView):
    """
    A view that displays a user's calendar.
    """
    template_name = 'user/profile_calendar_view.html'

    def get_context_data(self, **kwargs):
        # add the events and the appointments of the user
        context = super(CalendarView, self).get_context_data(**kwargs)
        context['event_list'] = Event.objects.all()
        user = User.objects.get(pk=int(self.request.user.pk))
        context['appointment_list'] = user.owned_appointments.all()
        return context


class NotificationRegistrationCreateView(CommuniqueFormView):
    """
    A view to register a user for certain notifications
    """
    form_class = NotificationRegistrationForm
    template_name = 'user/notification_registration_form.html'

    def get_success_url(self):
        # return to the profile view
        return reverse('user_profile_detail', kwargs={'pk':self.request.user.pk})

    def form_valid(self, form):
        # create the notification registration if the user doesn't already have a registration for the chosen service
        print(form.cleaned_data['service'])
        return super(NotificationRegistrationCreateView, self).form_valid(form)


class NotificationRegistrationDeleteView(CommuniqueDeleteView):
    """
    A view to delete a notification registration for a user
    """
    model = NotificationRegistration
    context_object_name = 'notification_registration'
    template_name = 'user/notification_registration_confirm_delete.html'

    def get_success_url(self):
        # return to the profile view
        return reverse('user_profile_detail', kwargs={'pk':self.request.user.pk})

    def test_func(self):
        # check that the user is active
        return self.request.user.is_active
