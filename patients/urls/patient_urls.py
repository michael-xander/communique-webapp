from django.conf.urls import url

from patients.views import (PatientListView, PatientCreateView, PatientDetailView, PatientUpdateView, PatientDeleteView,
                            PatientEnrollmentCreateView, PatientSessionCreateView, PatientAppointmentCreateView,
                            PatientMedicalReportCreateView, PatientAdmissionCreateView, PatientImportView,
                            PatientRegimenCreateView, PatientAdverseEventCreateView, PatientContactUpdateView,
                            PatientArchiveView, PatientUnarchiveView, PatientArchiveListView, PatientOutcomeCreateView,
                            OutcomeTypeListView, OutcomeTypeCreateView, OutcomeTypeUpdateView, OutcomeTypeDetailView,
                            OutcomeTypeDeleteView, OutcomeListView, OutcomeCreateView, OutcomeDetailView,
                            OutcomeUpdateView, OutcomeExportFormView, OutcomeExportListView, OutcomeDeleteView)

urlpatterns = [
    url(r'^$', PatientListView.as_view(), name='patients_patient_list'),
    url(r'^archive/$', PatientArchiveListView.as_view(), name='patients_patient_archived_list'),
    url(r'^create/$', PatientCreateView.as_view(), name='patients_patient_create'),
    url(r'^import/$', PatientImportView.as_view(), name='patients_patient_import'),
    url(r'^(?P<pk>[0-9]+)/$', PatientDetailView.as_view(), name='patients_patient_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', PatientUpdateView.as_view(), name='patients_patient_update'),
    url(r'^(?P<pk>[0-9]+)/update-contacts/$', PatientContactUpdateView.as_view(),
        name='patients_patient_contact_update'),
    url(r'^(?P<pk>[0-9]+)/archive/$', PatientArchiveView.as_view(), name='patients_patient_archive'),
    url(r'^(?P<pk>[0-9]+)/unarchive/$', PatientUnarchiveView.as_view(), name='patients_patient_unarchive'),
    url(r'^(?P<pk>[0-9]+)/delete/$', PatientDeleteView.as_view(), name='patients_patient_delete'),
    url(r'^outcome-types/$', OutcomeTypeListView.as_view(), name='patients_outcome_type_list'),
    url(r'^outcome-types/create/$', OutcomeTypeCreateView.as_view(), name='patients_outcome_type_create'),
    url(r'^outcome-types/(?P<pk>[0-9]+)/update/$', OutcomeTypeUpdateView.as_view(), name='patients_outcome_type_update'),
    url(r'^outcome-types/(?P<pk>[0-9]+)/$', OutcomeTypeDetailView.as_view(), name='patients_outcome_type_detail'),
    url(r'^outcome-types/(?P<pk>[0-9]+)/delete/$', OutcomeTypeDeleteView.as_view(), name='patients_outcome_type_delete'),
    url(r'^outcomes/$', OutcomeListView.as_view(), name='patients_outcome_list'),
    url(r'^outcomes/create/$', OutcomeCreateView.as_view(), name='patients_outcome_create'),
    url(r'^outcomes/export/$', OutcomeExportFormView.as_view(), name='patients_outcome_export_form'),
    url(r'^outcomes/export/(?P<start_year>[0-9]{4})-(?P<start_month>[0-9]{2})-(?P<start_day>[0-9]{2})/(?P<end_year>[0-9]{4})-(?P<end_month>[0-9]{2})-(?P<end_day>[0-9]{2})/$',
        OutcomeExportListView.as_view(), name='patients_outcome_export_list'),
    url(r'^outcomes/(?P<pk>[0-9]+)/$', OutcomeDetailView.as_view(), name='patients_outcome_detail'),
    url(r'^outcomes/(?P<pk>[0-9]+)/update/$', OutcomeUpdateView.as_view(), name='patients_outcome_update'),
    url(r'^outcomes/(?P<pk>[0-9]+)/delete/$', OutcomeDeleteView.as_view(), name='patients_outcome_delete'),
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
    url(r'^(?P<patient_pk>[0-9]+)/add-outcome/$', PatientOutcomeCreateView.as_view(),
        name='patients_patient_outcome_create')

]