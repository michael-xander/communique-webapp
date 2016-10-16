from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from .views import *

# Create a router and register our viewSets with it.
router = DefaultRouter()
router.register(r'programs', ProgramViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'users', CommuniqueUserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'counselling', CounsellingSessionViewSet)
router.register(r'session', CounsellingSessionTypeViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'admissions', AdmissionsViewSet)
router.register(r'medicalReportType', MedicalReportTypeViewSet)
router.register(r'medicalReport', MedicalReportViewSet)
router.register(r'events', EventViewSet)
router.register(r'adverseEvents', AdverseEventViewSet)
router.register(r'adverseEventType', AdverseEventTypeViewSet)
router.register(r'contact', EmergencyContactViewSet)
router.register(r'drug', DrugViewSet)
router.register(r'regimen', RegimenViewSet)
router.register(r'outcomeType', OutcomeTypeViewSet)
router.register(r'outcome', OutcomeViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'devices', FCMDeviceAuthorizedViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/(?P<username>\w+)/$', ProfileLoginView.as_view(), name='api_login'),
]
