from django.conf.urls import url

from .views import (AdmissionCreateView, AdmissionUpdateView, AdmissionDeleteView, AdmissionDetailView,
                    AdmissionListView, AdmissionExportFormView, AdmissionExportListView)

urlpatterns = [
    url(r'^$', AdmissionListView.as_view(), name='admissions_admission_list'),
    url(r'^create/$', AdmissionCreateView.as_view(), name='admissions_admission_create'),
    url(r'^(?P<pk>[0-9]+)/$', AdmissionDetailView.as_view(), name='admissions_admission_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', AdmissionUpdateView.as_view(), name='admissions_admission_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', AdmissionDeleteView.as_view(), name='admissions_admission_delete'),
    url(r'^export/$', AdmissionExportFormView.as_view(), name='admissions_admission_export_form'),
    url(r'^export/(?P<start_year>[0-9]{4})-(?P<start_month>[0-9]{2})-(?P<start_day>[0-9]{2})/(?P<end_year>[0-9]{4})-(?P<end_month>[0-9]{2})-(?P<end_day>[0-9]{2})/$',
        AdmissionExportListView.as_view(), name='admissions_admission_export_list'),
]