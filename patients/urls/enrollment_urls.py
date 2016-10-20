from django.conf.urls import url

from patients.views import (EnrollmentListView, EnrollmentCreateView, EnrollmentDetailView, EnrollmentUpdateView,
                            EnrollmentExportFormView, EnrollmentExportListView, EnrollmentDeleteView)

urlpatterns = [
    url(r'^$', EnrollmentListView.as_view(), name='patients_enrollment_list'),
    url(r'^create/$', EnrollmentCreateView.as_view(), name='patients_enrollment_create'),
    url(r'^(?P<pk>[0-9]+)/$', EnrollmentDetailView.as_view(), name='patients_enrollment_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', EnrollmentUpdateView.as_view(), name='patients_enrollment_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', EnrollmentDeleteView.as_view(), name='patients_enrollment_delete'),
    url(r'^export/$', EnrollmentExportFormView.as_view(), name='patients_enrollment_export_form'),
    url(r'^export/(?P<start_year>[0-9]{4})-(?P<start_month>[0-9]{2})-(?P<start_day>[0-9]{2})/(?P<end_year>[0-9]{4})-(?P<end_month>[0-9]{2})-(?P<end_day>[0-9]{2})/$',
        EnrollmentExportListView.as_view(), name='patients_enrollment_export_list'),
]