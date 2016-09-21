from rest_framework import serializers

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
        fields = ('id', 'last_name', 'other_names',  'sex', 'birth_date', 'identifier', 'location',
                  'contact_number', 'reference_health_centre', 'interim_outcome', 'treatment_start_date',
                  'created_by', 'last_modified_by', 'date_created', 'date_last_modified', 'enrolled_programs')
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