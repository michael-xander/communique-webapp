from django.conf.urls import url

from patients.views import (PatientListView, PatientCreateView, PatientDetailView, PatientUpdateView, PatientDeleteView,
                            PatientEnrollmentCreateView, PatientSessionCreateView, PatientAppointmentCreateView,
                            PatientMedicalReportCreateView, PatientAdmissionCreateView, PatientImportView,
                            PatientRegimenCreateView)

urlpatterns = [
    url(r'^$', PatientListView.as_view(), name='patients_patient_list'),
    url(r'^create/$', PatientCreateView.as_view(), name='patients_patient_create'),
    url(r'^import/$', PatientImportView.as_view(), name='patients_patient_import'),
    url(r'^(?P<pk>[0-9]+)/$', PatientDetailView.as_view(), name='patients_patient_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', PatientUpdateView.as_view(), name='patients_patient_update'),
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
]