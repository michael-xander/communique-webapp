from rest_framework import serializers

from admissions.models import Admission
from appointments.models import Appointment
from counselling_sessions.models import CounsellingSession, CounsellingSessionType
from medical.models import MedicalReportType, MedicalReport
from occasions.models import Event
from programs.models import Program
from patients.models import Patient, Enrollment
from user.models import CommuniqueUser, Profile


class ProgramSerializer(serializers.ModelSerializer):
    """
    A serializer for the Program model.
    """
    created_by = serializers.ReadOnlyField(source='created_by.username')
    last_modified_by = serializers.ReadOnlyField(source='last_modified_by.username')

    class Meta:
        model = Program
        fields = ('id', 'name', 'description', 'is_open', 'created_by', 'last_modified_by',
                  'date_created', 'date_last_modified')
        read_only_fields = ('date_created', 'date_last_modified',)


class PatientSerializer(serializers.ModelSerializer):
    """
    A serializer for the Patient model.
    """
    created_by = serializers.ReadOnlyField(source='created_by.username')
    last_modified_by = serializers.ReadOnlyField(source='last_modified_by.username')

    class Meta:
        model = Patient
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'birth_date', 'identifier', 'location',
                  'contact_number', 'reference_health_centre', 'enrolled_programs', 'created_by', 'last_modified_by',
                  'date_created', 'date_last_modified')
        read_only_fields = ('date_created', 'date_last_modified',)


class EnrollmentSerializer(serializers.ModelSerializer):
    """
    A serializer for the Enrollment model.
    """
    enrolled_by = serializers.ReadOnlyField(source='enrolled_by.username')

    class Meta:
        model = Enrollment
        fields = ('id', 'patient', 'program', 'comment', 'is_active', 'enrolled_by', 'date_enrolled')
        read_only_fields = ('date_enrolled',)


class CommuniqueUserSerializer(serializers.ModelSerializer):
    """
    A serializer for the CommuniqueUser model.
    """
    class Meta:
        model = CommuniqueUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'is_superuser',
                  'last_login', 'date_joined')
        read_only_fields = ('last_login', 'date_joined',)


class ProfileSerializer(serializers.ModelSerializer):
    """
    A serializer for the Profile model.
    """
    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name', 'email', 'last_login', 'date_joined', 'username', 'is_staff',
                  'is_active', 'is_superuser')
        read_only_fields = ('last_login', 'date_joined', 'username', 'is_staff', 'is_active', 'is_superuser',)


class CounsellingSessionSerializer(serializers.ModelSerializer):
    """
    A serializer for the CounsellingSession model.
    """
    class Meta:
        model = CounsellingSession
        fields = ('id', 'counselling_session_type', 'patient', 'notes', 'created_by', 'date_created',
                  'last_modified_by', 'date_last_modified')
        read_only_fields = ('date_created', 'date_last_modified')


class CounsellingSessionTypeSerializer(serializers.ModelSerializer):
    """
    A serializer for the CounsellingSessionType model.
    """
    class Meta:
        model = CounsellingSessionType
        fields = ('id', 'name', 'description', 'created_by', 'date_created',
                  'last_modified_by', 'date_last_modified')
        read_only_fields = ('date_created', 'date_last_modified')


class AppointmentSerializer(serializers.ModelSerializer):
    """
    A serializer for the Appointments model.
    """
    class Meta:
        model = Appointment
        fields = ('title', 'notes', 'patient', 'owner', 'appointment_date', 'start_time', 'end_time', 'created_by',
                  'last_modified_by', 'date_created', 'date_last_modified')
        read_only_fields = ('date_created', 'date_last_modified')


class AdmissionSerializer(serializers.ModelSerializer):
    """
    A serializer for the Admission model.
    """
    class Meta:
        model = Admission
        fields = ('patient', 'admission_date', 'discharge_date', 'health_centre', 'notes', 'created_by',
                  'last_modified_by', 'date_created', 'date_last_modified')
        read_only_fields = ('date_created', 'date_last_modified')


class MedicalReportTypeSerializer(serializers.ModelSerializer):
    """
    A serializer for the MedicalReportType model.
    """
    class Meta:
        model = MedicalReportType
        fields = ('name', 'description', 'created_by', 'last_modified_by', 'date_created', 'date_last_modified')
        read_only_fields = ('date_created', 'date_last_modified')


class MedicalReportSerializer(serializers.ModelSerializer):
    """"
    A serializer for the MedicalReport model.
    """
    class Meta:
        model = MedicalReport
        fields = ('title', 'report_type', 'patient', 'notes', 'date_created', 'date_last_modified', 'created_by',
                  'last_modified_by')
        read_only_fields = ('date_created', 'date_last_modified')


class EventSerializer(serializers.ModelSerializer):
    """"
    A serializer for the Event model.
    """
    class Meta:
        model = Event
        fields = ('name', 'description', 'event_date', 'start_time', 'end_time', 'created_by', 'last_modified_by',
                  'date_created', 'date_last_modified')
        ead_only_fields = ('date_created', 'date_last_modified')
