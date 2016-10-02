from django.conf.urls import url

from .views import (EmergencyContactCreateView, EmergencyContactUpdateView, EmergencyContactDeleteView,
                    EmergencyContactDetailView, EmergencyContactListView, AdverseEventTypeUpdateView,
                    AdverseEventTypeCreateView, AdverseEventTypeDeleteView, AdverseEventTypeDetailView,
                    AdverseEventTypeListView, AdverseEventCreateView, AdverseEventDeleteView, AdverseEventDetailView,
                    AdverseEventListView, AdverseEventUpdateView)

urlpatterns = [
    url(r'^emergency-contacts/$', EmergencyContactListView.as_view(), name='adverse_emergency_contact_list'),
    url(r'^emergency-contacts/create/$', EmergencyContactCreateView.as_view(), name='adverse_emergency_contact_create'),
    url(r'^emergency-contacts/(?P<pk>[0-9]+)/$', EmergencyContactDetailView.as_view(),
        name='adverse_emergency_contact_detail'),
    url(r'^emergency-contacts/(?P<pk>[0-9]+)/update/$', EmergencyContactUpdateView.as_view(),
        name='adverse_emergency_contact_update'),
    url(r'^emergency-contacts/(?P<pk>[0-9]+)/delete/$', EmergencyContactDeleteView.as_view(),
        name='adverse_emergency_contact_delete'),
    url(r'^event-types/$', AdverseEventTypeListView.as_view(), name='adverse_event_type_list'),
    url(r'^event-types/create/$', AdverseEventTypeCreateView.as_view(), name='adverse_event_type_create'),
    url(r'^event-types/(?P<pk>[0-9]+)/$', AdverseEventTypeDetailView.as_view(), name='adverse_event_type_detail'),
    url(r'^event-types/(?P<pk>[0-9]+)/update/$', AdverseEventTypeUpdateView.as_view(), name='adverse_event_type_update'),
    url(r'^event-types/(?P<pk>[0-9]+)/delete/$', AdverseEventTypeDeleteView.as_view(), name='adverse_event_type_delete'),
    url(r'^events/$', AdverseEventListView.as_view(), name='adverse_event_list'),
    url(r'^events/create/$', AdverseEventCreateView.as_view(), name='adverse_event_create'),
    url(r'^events/(?P<pk>[0-9]+)/$', AdverseEventDetailView.as_view(), name='adverse_event_detail'),
    url(r'^events/(?P<pk>[0-9]+)/update/$', AdverseEventUpdateView.as_view(), name='adverse_event_update'),
    url(r'^events/(?P<pk>[0-9]+)/delete/$', AdverseEventDeleteView.as_view(), name='adverse_event_delete'),
]