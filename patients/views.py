from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse

import csv

from communique.views import (CommuniqueDeleteView, CommuniqueListView, CommuniqueDetailView, CommuniqueUpdateView,
                              CommuniqueCreateView, CommuniqueFormView, CommuniqueExportFormView,
                              CommuniqueExportListView)
from .models import Patient, Enrollment, Outcome, OutcomeType
from counselling_sessions.models import CounsellingSession
from appointments.models import Appointment
from medical.models import MedicalReport
from .forms import PatientAppointmentForm, PatientUploadFileForm, PatientRegimenForm, EnrollmentForm, OutcomeForm
from admissions.models import Admission
from admissions.forms import AdmissionUpdateForm
from regimens.models import Regimen
from adverse.models import AdverseEvent
from patients.utils.utils_views import import_patients_from_file


class PatientListView(CommuniqueListView):
    """
    A view to list all patients that currently exist in the system and are not archived.
    """
    model = Patient
    template_name = 'patients/patient_list.html'
    context_object_name = 'patient_list'

    def get_queryset(self):
        # get all the patients that are not archived
        patients = Patient.objects.filter(archived=False)
        return patients


class PatientArchiveListView(CommuniqueListView):
    """
    A view to list all patients that have been archived
    """
    model = Patient
    template_name = 'patients/patient_archived_list.html'
    context_object_name = 'patient_archived_list'

    def get_queryset(self):
        # get all the patients that are archived
        patients = Patient.objects.filter(archived=True)
        return patients


class PatientCreateView(CommuniqueCreateView):
    """
    A view to handle creation of patients.
    """
    model = Patient
    fields = ['last_name', 'other_names', 'identifier', 'reference_health_centre', 'birth_date', 'sex', 'location',
              'treatment_start_date', 'interim_outcome', 'contact_number', 'second_contact_number',
              'third_contact_number']
    template_name = 'patients/patient_form.html'


class PatientDetailView(CommuniqueDetailView):
    """
    A view to display the details of a patient.
    """
    model = Patient
    template_name = 'patients/patient_view.html'
    context_object_name = 'patient'


class PatientUpdateView(CommuniqueUpdateView):
    """
    A view to handle updating patient information.
    """
    model = Patient
    fields = ['last_name', 'other_names', 'identifier', 'birth_date', 'sex', 'treatment_start_date', 'interim_outcome']
    template_name = 'patients/patient_update_form.html'
    context_object_name = 'patient'


class PatientContactUpdateView(CommuniqueUpdateView):
    """
    A view to handle updating a patient's contact details
    """
    model = Patient
    fields = ['location', 'reference_health_centre', 'contact_number', 'second_contact_number', 'third_contact_number']
    template_name = 'patients/patient_contact_update_form.html'
    context_object_name = 'patient'


class PatientArchiveView(CommuniqueUpdateView):
    """
    A view to handle archiving a patient
    """
    model = Patient
    fields = []
    template_name = 'patients/patient_confirm_archive.html'
    context_object_name = 'patient'

    def form_valid(self, form):
        # make the patient's archived attribute true
        form.instance.archived = True

        return super(PatientArchiveView, self).form_valid(form)


class PatientUnarchiveView(CommuniqueUpdateView):
    """
    A view to handle unarchiving a patient
    """
    model = Patient
    fields = []
    template_name = 'patients/patient_confirm_unarchive.html'
    context_object_name = 'patient'

    def form_valid(self, form):
        # make the patient's archived attribute false
        form.instance.archived = False

        return super(PatientUnarchiveView, self).form_valid(form)


class PatientDeleteView(CommuniqueDeleteView):
    """
    A view to handle the deletion of a patient.
    """
    model = Patient
    success_url = reverse_lazy('patients_patient_list')
    context_object_name = 'patient'
    template_name = 'patients/patient_confirm_delete.html'


class PatientImportView(SuccessMessageMixin, CommuniqueFormView):
    """
    A view to handle the importation of patients through an uploaded file.
    """
    template_name = 'patients/patient_import_form.html'
    form_class = PatientUploadFileForm
    success_url = reverse_lazy('patients_patient_list')
    success_message = 'The patients have successfully been added to the system.'

    def form_valid(self, form):
        # import the patients in the uploaded file
        uploaded_file = self.get_form_kwargs().get('files')['uploaded_file']
        import_patients_from_file(uploaded_file, self.request.user)
        return super(PatientImportView, self).form_valid(form)


class OutcomeTypeListView(CommuniqueListView):
    """
    A view to list all outcome types
    """
    model = OutcomeType
    template_name = 'patients/outcome_type_list.html'
    context_object_name = 'outcome_type_list'


class OutcomeTypeCreateView(CommuniqueCreateView):
    """
    A view to create an outcome type
    """
    model = OutcomeType
    template_name = 'patients/outcome_type_form.html'
    fields = ['name', 'description']


class OutcomeTypeUpdateView(CommuniqueUpdateView):
    """
    A view to update an outcome type
    """
    model = OutcomeType
    template_name = 'patients/outcome_type_update_form.html'
    fields = ['name', 'description']
    context_object_name = 'outcome_type'


class OutcomeTypeDetailView(CommuniqueDetailView):
    """
    A view to display details of an outcome type
    """
    model = OutcomeType
    template_name = 'patients/outcome_type_view.html'
    context_object_name = 'outcome_type'


class OutcomeTypeDeleteView(CommuniqueDeleteView):
    """
    A view to delete an outcome type
    """
    model = OutcomeType
    success_url = reverse_lazy('patient_outcome_type_list')
    context_object_name = 'outcome_type'
    template_name = 'patients/outcome_type_confirm_delete.html'


class OutcomeListView(CommuniqueListView):
    """
    A view to list the outcomes of patients
    """
    model = Outcome
    template_name = 'patients/outcome_list.html'
    context_object_name = 'outcome_list'


class OutcomeCreateView(CommuniqueCreateView):
    """
    A view to create a patient outcome
    """
    model = Outcome
    form_class = OutcomeForm
    template_name = 'patients/outcome_form.html'


class OutcomeExportFormView(CommuniqueExportFormView):
    """
    A view that handles the form for picking the creation dates for patient outcomes to be exported
    """
    template_name = 'patients/outcome_export_list.html'

    def get_success_view_name(self):
        return 'patients_outcome_export_list'


class OutcomeExportListView(CommuniqueExportListView):
    """
    A view that lists the patient outcomes to be exported depending on the provided start and end dates
    """
    model = Outcome
    template_name = 'patients/outcome_export_list.html'
    context_object_name = 'outcome_export_list'

    def get_queryset(self):
        # get all the outcomes within the provided date range
        start_date = self.get_export_start_date()
        end_date = self.get_export_end_date()
        outcomes = Outcome.objects.filter(date_created__range=[start_date, end_date])
        return outcomes

    def csv_export_response(self, context):
        # generate an HTTP response with the csv file for download
        start_date = self.get_export_start_date()
        end_date = self.get_export_end_date()
        date_format = '%d-%m-%Y'
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="outcomes_{0}_to_{1}.csv"'.format(
            start_date.strftime(date_format), end_date.strftime(date_format)
        )

        fieldnames = ['id', 'patient_id', 'patient_last_name', 'patient_other_names', 'outcome_type',
                      'outcome_date (dd-mm-yyyy)', 'notes', 'date_added (dd-mm-yyyy)', 'added_by']
        writer = csv.DictWriter(response, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()

        for outcome in context[self.context_object_name]:
            patient = outcome.patient
            writer.writerow({'id':outcome.id, 'patient_id':patient.identifier, 'patient_last_name':patient.last_name,
                             'patient_other_names':patient.other_names, 'outcome_type':outcome.outcome_type.__str__(),
                             'outcome_date (dd-mm-yyyy)':outcome.outcome_date.strftime(date_format),
                             'notes':outcome.notes, 'date_added (dd-mm-yyyy)':outcome.date_created.strftime(date_format),
                             'added_by':outcome.created_by.get_full_name()})

        return response


class OutcomeUpdateView(CommuniqueUpdateView):
    """
    A view to update a patient outcome
    """
    model = Outcome
    fields = ['outcome_date', 'notes']
    context_object_name = 'outcome'
    template_name = 'patients/outcome_update_form.html'


class OutcomeDetailView(CommuniqueDetailView):
    """
    A view to view the details of an outcome
    """
    model = Outcome
    template_name = 'patients/outcome_view.html'
    context_object_name = 'outcome'


class EnrollmentListView(CommuniqueListView):
    """
    A view to list all the enrollments that currently exist in the system.
    """
    model = Enrollment
    template_name = 'patients/enrollment_list.html'
    context_object_name = 'enrollment_list'


class EnrollmentCreateView(CommuniqueCreateView):
    """
    A view to handle creation of an enrollment.
    """
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'patients/enrollment_form.html'


class EnrollmentDetailView(CommuniqueDetailView):
    """
    A view to display details of an enrollment.
    """
    model = Enrollment
    template_name = 'patients/enrollment_view.html'
    context_object_name = 'enrollment'


class EnrollmentUpdateView(CommuniqueUpdateView):
    """
    A view to handle updating an enrollment.
    """
    model = Enrollment
    fields = ['date_enrolled', 'comment']
    template_name = 'patients/enrollment_update_form.html'
    context_object_name = 'enrollment'


class EnrollmentExportFormView(CommuniqueExportFormView):
    """
    A view that displays the form to be pick the duration to be considered for selecting enrollments for exportation
    """
    template_name = 'patients/enrollment_export_list.html'

    def get_success_view_name(self):
        # return the name of the view to which to redirect to on successful validation
        return 'patients_enrollment_export_list'


class EnrollmentExportListView(CommuniqueExportListView):
    """
    A view that retrieves the list of enrollments to be exported
    """
    model = Enrollment
    template_name = 'patients/enrollment_export_list.html'
    context_object_name = 'enrollment_export_list'

    def get_queryset(self):
        # get all the enrollments within the provided date range
        start_date = self.get_export_start_date()
        end_date = self.get_export_end_date()
        enrollments = Enrollment.objects.filter(date_created__range=[start_date, end_date])
        return enrollments

    def csv_export_response(self, context):
        # generate an HTTP response with the csv file for download
        start_date = self.get_export_start_date()
        end_date = self.get_export_end_date()
        date_format = '%d-%m-%Y'
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="enrollments_{0}_to_{1}.csv"'.format(
            start_date.strftime(date_format), end_date.strftime(date_format))

        fieldnames = ['id', 'program', 'patient_id', 'patient_last_name', 'patient_other_names',
                      'date_enrolled (dd-mm-yyyy)', 'enrolled_by', 'date_added (dd-mm-yyyy)', 'comment']

        writer = csv.DictWriter(response, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()

        for enrollment in context[self.context_object_name]:
            program = enrollment.program
            patient = enrollment.patient
            writer.writerow({'id':enrollment.id,'program':program.__str__(), 'patient_id':patient.identifier,
                             'patient_last_name':patient.last_name, 'patient_other_names':patient.other_names,
                             'date_enrolled (dd-mm-yyyy)':enrollment.date_enrolled.strftime(date_format),
                             'enrolled_by':enrollment.created_by.get_full_name(),
                             'date_added (dd-mm-yyyy)':enrollment.date_created.strftime(date_format),
                             'comment':enrollment.comment})
        return response


class PatientModelCreateView(CommuniqueCreateView):
    """
    A view that handles the creation of another model from the Patients app.
    """
    def get_success_url(self):
        # on finalising the creation of the model, redirect to the patient details view
        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        return patient.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super(PatientModelCreateView, self).get_context_data(**kwargs)
        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        context['patient'] = patient
        return context

    def form_valid(self, form):
        # set the patient
        patient = Patient.objects.get(pk=int(self.kwargs['patient_pk']))
        form.instance.patient = patient

        return super(PatientModelCreateView, self).form_valid(form)


class PatientEnrollmentCreateView(PatientModelCreateView):
    """
    A view to create an enrollment for a defined patient.
    """
    model = Enrollment
    fields = ['program', 'date_enrolled','comment']
    template_name = 'patients/patient_enrollment_form.html'


class PatientSessionCreateView(PatientModelCreateView):
    """
    A view that handles creation of a session for a specific patient.
    """
    model = CounsellingSession
    fields = ['counselling_session_type', 'notes']
    template_name = 'patients/patient_session_form.html'


class PatientOutcomeCreateView(PatientModelCreateView):
    """
    A view that handles creation of an outcome for a patient
    """
    model = Outcome
    fields = ['outcome_type', 'outcome_date', 'notes']
    template_name = 'patients/patient_outcome_form.html'


class PatientMedicalReportCreateView(PatientModelCreateView):
    """
    A view that handles creation of a medical report for a specific patient.
    """
    model = MedicalReport
    fields = ['title', 'report_type', 'notes']
    template_name = 'patients/patient_medical_report_form.html'


class PatientAppointmentCreateView(PatientModelCreateView):
    """
    A view that handles creation of an appointment for a specific patient.
    """
    model = Appointment
    form_class = PatientAppointmentForm
    template_name = 'patients/patient_appointment_form.html'

    def form_valid(self, form):
        if not form.instance.owner:
            form.instance.owner = self.request.user

        return super(PatientAppointmentCreateView, self).form_valid(form)


class PatientAdmissionCreateView(PatientModelCreateView):
    """
    A view that handles admission for a specific patient.
    """
    model = Admission
    form_class = AdmissionUpdateForm
    template_name = 'patients/patient_admission_form.html'


class PatientRegimenCreateView(PatientModelCreateView):
    """
    A view that handles adding a regimen for a specific patient.
    """
    model = Regimen
    form_class = PatientRegimenForm
    template_name = 'patients/patient_regimen_form.html'


class PatientAdverseEventCreateView(PatientModelCreateView):
    """
    A view that handles adding an adverse event for a specific patient.
    """
    model = AdverseEvent
    fields = ['adverse_event_type', 'event_date', 'notes']
    template_name = 'patients/patient_adverse_event_form.html'

