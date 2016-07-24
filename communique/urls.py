from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from dashboard import urls as dashboard_urls

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='login', permanent=False)),
    url(r'^login/$', auth_views.login, {'template_name':'login.html'},
        name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name':'logout.html'},
        name='logout'),
    url(r'^dashboard/', include(dashboard_urls)),
]
