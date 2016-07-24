from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', ServiceListView.as_view(), name='support_services_service_list'),
    url(r'^create/$', ServiceCreateView.as_view(),
        name='support_services_service_create'),
    url(r'^(?P<slug>[-\w]+)/$', ServiceDetailView.as_view(),
        name='support_services_service_detail'),
    url(r'^(?P<slug>[-\w]+)/update/$', ServiceUpdateView.as_view(),
        name='support_services_service_update'),
    url(r'^(?P<slug>[-\w]+)/delete/$', ServiceDeleteView.as_view(),
        name='support_services_service_delete'),
]
