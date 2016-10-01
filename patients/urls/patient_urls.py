from django.conf.urls import url

from patients.views import (PatientListView, PatientCreateView, PatientDetailView, PatientUpdateView, PatientDeleteView,
                            PatientEnrollmentCreateView, PatientSessionCreateView, PatientAppointmentCreateView,
                            PatientMedicalReportCreateView, PatientAdmissionCreateView, PatientImportView,
                            PatientRegimenCreateView, PatientAdverseEventCreateView, PatientContactUpdateView,
                            PatientArchiveView, PatientUnarchiveView)

urlpatterns = [
    url(r'^$', PatientListView.as_view(), name='patients_patient_list'),
    url(r'^create/$', PatientCreateView.as_view(), name='patients_patient_create'),
    url(r'^import/$', PatientImportView.as_view(), name='patients_patient_import'),
    url(r'^(?P<pk>[0-9]+)/$', PatientDetailView.as_view(), name='patients_patient_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', PatientUpdateView.as_view(), name='patients_patient_update'),
    url(r'^(?P<pk>[0-9]+)/update-contacts/$', PatientContactUpdateView.as_view(),
        name='patients_patient_contact_update'),
    url(r'^(?P<pk>[0-9]+)/archive/$', PatientArchiveView.as_view(), name='patients_patient_archive'),
    url(r'^(?P<pk>[0-9]+)/unarchive/$', PatientUnarchiveView.as_view(), name='patients_patient_unarchive'),
    url(r'^(?P<pk>[0-9]+)/delete/$', PatientDeleteView.as_view(), name='patients_patient_delete'),
    url(r'^(?P<patient_pk>[0-9]+)/enroll/$', PatientEnrollmentCreateView.as_view(),
        name='patients_patient_enroll_create'),
    url(r'^(?P<patient_pk>[0-9]+)/add-session/$', PatientSessionCreateView.as_view(),
        name='patients_patient_session_create'),
    url(r'^(?P<patient_pk>[0-9]+)/add-appointment/$', PatientAppointmentCreateView.as_view(),
        name='patients_patient_appointment_create'),
    url(r'^(?P<patient_pk>[0-9]+)/add-medical-report/$', PatientMedicalReportCreateView.as_view(),
        name='patients_patient_medical_report_create'),
    url(r'^(?P<patient_pk>[0-9]+)/add-admission/$', PatientAdmissionCreateView.as_view(),
        name='patients_patient_admission_create'),
    url(r'^(?P<patient_pk>[0-9]+)/add-regimen/$', PatientRegimenCreateView.as_view(),
        name='patients_patient_regimen_create'),
    url(r'^(?P<patient_pk>[0-9]+)/report-adverse-event/$', PatientAdverseEventCreateView.as_view(),
        name='patients_patient_adverse_event_create'),
]