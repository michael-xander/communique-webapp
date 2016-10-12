from django.conf.urls import url

from .views import (AppointmentCreateView, AppointmentDetailView, AppointmentUpdateView, AppointmentListView,
                    AppointmentDeleteView, AppointmentExportFormView, AppointmentExportListView)

urlpatterns = [
    url(r'^$', AppointmentListView.as_view(), name='appointments_appointment_list'),
    url(r'^create/$', AppointmentCreateView.as_view(), name='appointments_appointment_create'),
    url(r'^(?P<pk>[0-9]+)/$', AppointmentDetailView.as_view(), name='appointments_appointment_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', AppointmentUpdateView.as_view(), name='appointments_appointment_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', AppointmentDeleteView.as_view(), name='appointments_appointment_delete'),
    url(r'^export/$', AppointmentExportFormView.as_view(), name='appointments_appointment_export_form'),
    url(r'^export/(?P<start_year>[0-9]{4})-(?P<start_month>[0-9]{2})-(?P<start_day>[0-9]{2})/(?P<end_year>[0-9]{4})-(?P<end_month>[0-9]{2})-(?P<end_day>[0-9]{2})/$',
        AppointmentExportListView.as_view(), name='appointments_appointment_export_list'),
]