from django.db.models.signals import post_save
from django.dispatch import receiver

from communique.utils.utils_signals import generate_notifications
from user.models import NotificationRegistration
from .models import Patient, Enrollment, Outcome
from .models import Admission
from .models import AdverseEvent
from .models import Appointment
from .models import CounsellingSession
from .models import MedicalReport
from .models import Event
from .models import Regimen


@receiver(post_save, sender=Patient)
def post_patient_save_callback(sender, **kwargs):
    """
    Creates notifications for all users registered for patient notifications on the creation and updating of a patient
    """
    generate_notifications(NotificationRegistration.PATIENTS, kwargs)


@receiver(post_save, sender=Enrollment)
def post_enrollment_save_callback(sender, **kwargs):
    """
    Creates notifications for all users registered for enrollment notifications on creation/modification of enrollments
    """
    generate_notifications(NotificationRegistration.ENROLLMENTS, kwargs)


@receiver(post_save, sender=Outcome)
def post_patient_outcome_save_callback(sender, **kwargs):
    """
    Creates notifications for all users registered for patient outcome notifications on creation/modification of a
    patient outcome
    """
    generate_notifications(NotificationRegistration.PATIENT_OUTCOMES, kwargs)
    
    
@receiver(post_save, sender=Admission)
def post_admission_save_callback(sender, **kwargs):
    """
    Creates a notification informing all users about creation or editing of admission
    """
    generate_notifications(NotificationRegistration.ADMISSIONS, kwargs)
    
    
@receiver(post_save, sender=AdverseEvent)
def post_adverse_event_save_callback(sender, **kwargs):
    """
    Creates notifications informing all registered users that an adverse event has been created/updated
    """
    generate_notifications(NotificationRegistration.ADVERSE_EVENTS, kwargs)
    
    
@receiver(post_save, sender=Appointment)
def post_appointment_save_callback(sender, **kwargs):
    """
    Creates a notification informing all users about the appointment
    """
    generate_notifications(NotificationRegistration.APPOINTMENTS, kwargs)
    
    
@receiver(post_save, sender=CounsellingSession)
def post_counselling_session_save_callback(sender, **kwargs):
    """
    Creates notifications informing all users registered for the notifications that a counselling session been
    added/edited
    """
    generate_notifications(NotificationRegistration.COUNSELLING_SESSIONS, kwargs)
    
    
@receiver(post_save, sender=MedicalReport)
def post_medical_report_save_callback(sender, **kwargs):
    """
    Creates notifications for all users registered for notifications when medical reports are added/updated
    """
    generate_notifications(NotificationRegistration.MEDICAL_REPORTS, kwargs)
    
    
@receiver(post_save, sender=Event)
def post_event_save_callback(sender, **kwargs):
    """
    Creates a notification informing all users about creation or editing of an event
    """
    generate_notifications(NotificationRegistration.EVENTS, kwargs)
    
    
@receiver(post_save, sender=Regimen)
def post_regimen_save_callback(sender, **kwargs):
    """
    Creates notifications for all users registered for regimen notifications on addition/modification of a regimen
    """
    generate_notifications(NotificationRegistration.REGIMENS, kwargs)

