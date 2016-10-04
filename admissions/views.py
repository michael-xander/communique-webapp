from django.core.urlresolvers import reverse_lazy

from communique.views import (CommuniqueCreateView, CommuniqueDetailView, CommuniqueDeleteView, CommuniqueListView,
                              CommuniqueUpdateView)
from .models import Admission
from .forms import AdmissionUpdateForm, AdmissionCreateForm


class AdmissionCreateView(CommuniqueCreateView):
    """
    A view that handles creation of an admission.
    """
    model = Admission
    form_class = AdmissionCreateForm
    template_name = 'admissions/admission_form.html'


class AdmissionDetailView(CommuniqueDetailView):
    """
    A view that handles displaying details of an admission.
    """
    model = Admission
    template_name = 'admissions/admission_view.html'
    context_object_name = 'admission'


class AdmissionUpdateView(CommuniqueUpdateView):
    """
    A view that handles updating of an admission.
    """
    model = Admission
    form_class = AdmissionUpdateForm
    template_name = 'admissions/admission_update_form.html'
    context_object_name = 'admission'


class AdmissionListView(CommuniqueListView):
    """
    A view that lists the existing admissions.
    """
    model = Admission
    template_name = 'admissions/admission_list.html'
    context_object_name = 'admission_list'


class AdmissionDeleteView(CommuniqueDeleteView):
    """
    A view that handles deletion of an admission.
    """
    model = Admission
    success_url = reverse_lazy('admissions_admission_list')
    context_object_name = 'admission'
    template_name = 'admissions/admission_confirm_delete.html'
