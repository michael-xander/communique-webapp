from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView


from .views import (CommuniqueUserListView, CommuniqueUserCreateView, CommuniqueUserDetailView, CommuniqueUserUpdateView,
                    ProfileDetailView, ProfileUpdateView, CalendarView, ProfileNotificationListView)

urlpatterns = [
    # urls for logging in and out
    url(r'^$', RedirectView.as_view(pattern_name='dashboard_home', permanent=False)),
    url(r'^login/$', auth_views.login, {'template_name':'user/login.html'}, name='user_login'),
    url(r'^logout/$', auth_views.logout, {'template_name':'user/logout.html', 'next_page':'/user/login/'},
        name='user_logout'),
    # urls for resetting a user's password
    url(r'^password-reset/$', auth_views.password_reset, {'template_name':'user/password_reset_form.html',
                                                          'email_template_name':'user/password_reset_email.html',
                                                          'post_reset_redirect':'/user/password-reset/done/'},
        name='password_reset'),
    url(r'^password-reset/done/$', auth_views.password_reset_done, {'template_name':'user/password_reset_done.html'},
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, {'template_name':'user/password_reset_confirm.html',
                                            'post_reset_redirect':'/user/reset/done/'}, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, {'template_name':'user/password_reset_complete.html'},
        name='password_reset_complete'),
    # urls to CRUD Communique users
    url(r'^communique-users/$', CommuniqueUserListView.as_view(), name='user_communique_user_list'),
    url(r'^communique-users/create/$', CommuniqueUserCreateView.as_view(), name='user_communique_user_create'),
    url(r'^communique-users/(?P<pk>[0-9]+)/$', CommuniqueUserDetailView.as_view(), name='user_communique_user_detail'),
    url(r'^communique-users/(?P<pk>[0-9]+)/update/$', CommuniqueUserUpdateView.as_view(),
        name='user_communique_user_update'),
    # urls to view and update user profile
    url(r'^profile/(?P<pk>[0-9]+)/$', ProfileDetailView.as_view(), name='user_profile_detail'),
    url(r'^profile/(?P<pk>[0-9]+)/update/$', ProfileUpdateView.as_view(), name='user_profile_update'),
    url(r'^profile/password-change/$', auth_views.password_change, {'template_name':'user/password_change_form.html',
                                                                    'post_change_redirect':'/user/profile/password-change-done/'},
        name='password_change'),
    url(r'^profile/password-change-done/$', auth_views.password_change_done,
        {'template_name':'user/password_change_done.html'}, name='password_change_done'),
    # urls to handle a profile's calendar
    url(r'^profile/calendar/$', CalendarView.as_view(), name='user_profile_calendar_view'),
    # urls for a profile's notifications
    url(r'^profile/notifications/$', ProfileNotificationListView.as_view(), name='user_profile_notification_list'),
]
