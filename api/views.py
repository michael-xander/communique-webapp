
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions

from .serializers import *
from .permissions import IsActiveUser, IsSuperUser, IsProfileOrReadOnly

from admissions.models import Admission
from appointments.models import Appointment
from counselling_sessions.models import CounsellingSession
from programs.models import Program
from patients.models import Patient, Enrollment, Outcome, OutcomeType
from user.models import CommuniqueUser, Profile, NotificationRegistration
from notifications.models import Notification


class ProgramViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD Program models.
    """
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that has created the Program
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class PatientViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD Patient models.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that has created the Patient
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class EnrollmentViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD Enrollment models.
    """
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that is enrolling the patient
        serializer.save(enrolled_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class CommuniqueUserViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD CommuniqueUser models.

    Only superusers can access it.
    """
    queryset = CommuniqueUser.objects.all()
    serializer_class = CommuniqueUserSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser, IsSuperUser,)


class ProfileViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD Profile models.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser, IsProfileOrReadOnly,)


class ProfileLoginView(generics.RetrieveAPIView):
    """
    This endpoint retrieves a user's profile on successful login.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'username'
    lookup_url_kwarg = 'username'
    permission_classes = (permissions.IsAuthenticated,)


class CounsellingSessionViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD CounsellingSession models.
    """
    queryset = CounsellingSession.objects.all()
    serializer_class = CounsellingSessionSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that is enrolling the patient
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class CounsellingSessionTypeViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD CounsellingSessionType models.
    """
    queryset = CounsellingSessionType.objects.all()
    serializer_class = CounsellingSessionTypeSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that is enrolling the patient
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class AppointmentViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD Appointment models.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that is enrolling the patient
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class AdmissionsViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD Admissions models.
    """
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that is enrolling the patient
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class MedicalReportTypeViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD MedicalReportType models.
    """
    queryset = MedicalReportType.objects.all()
    serializer_class = MedicalReportTypeSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that is enrolling the patient
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class MedicalReportViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD MedicalReport models.
    """
    queryset = MedicalReport.objects.all()
    serializer_class = MedicalReportSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that is enrolling the patient
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class EventViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD Event models.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that is enrolling the patient
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class EmergencyContactViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD EmergencyContact models.
    """
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencyContactSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that is enrolling the patient
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class AdverseEventTypeViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD AdverseEventType models.
    """
    queryset = AdverseEventType.objects.all()
    serializer_class = AdverseEventTypeSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that is enrolling the patient
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class AdverseEventViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD AdverseEvent models.
    """
    queryset = AdverseEvent.objects.all()
    serializer_class = AdverseEventSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that is enrolling the patient
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class DrugViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD Drug models.
    """
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that is enrolling the patient
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class RegimenViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD Regimen models.
    """
    queryset = Regimen.objects.all()
    serializer_class = RegimenSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that is enrolling the patient
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class OutcomeViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD Outcome models.
    """
    queryset = Outcome.objects.all()
    serializer_class = OutcomeSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that is enrolling the patient
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)


class OutcomeTypeViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD Outcome models.
    """
    queryset = OutcomeType.objects.all()
    serializer_class = OutcomeTypeSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)

    def perform_create(self, serializer):
        # save the user that is enrolling the patient
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)

class NotificationViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD Notification models.
    """
    queryset = Notification.objects.unread()
    serializer_class = NotificationSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)
    

class NotificationRegistrationViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides calls to CRUD NotificationRegistration models.
    """
    queryset = NotificationRegistration.objects.all()
    serializer_class = NotificationRegistrationSerializer
    permission_classes = (permissions.IsAuthenticated, IsActiveUser,)
    
    def perform_create(self, serializer):
        # save the user that is enrolling the patient
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)

    def perform_update(self, serializer):
        # save the user that has made the modification
        serializer.save(last_modified_by=self.request.user)
    
