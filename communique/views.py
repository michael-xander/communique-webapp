from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse

from .forms import DurationForm


class CommuniqueTemplateView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    """
    A view to display a template.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    def test_func(self):
        """
        Checks whether the user is marked active.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class CommuniqueCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    A view that handles creation of a model.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    def test_func(self):
        """
        Checks whether the user is marked active.
        :return: True if user is active, false otherwise
        """
        return self.request.user.is_active

    def form_valid(self, form):
        # update the creator and modified fields of the models created
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user

        return super(CommuniqueCreateView, self).form_valid(form)


class CommuniqueFormView(LoginRequiredMixin, UserPassesTestMixin, FormView):
    """
    A view that displays a form.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    def test_func(self):
        """
        Checks whether the user is marked active.
        :return: True if user is active, false otherwise
        """
        return self.request.user.is_active


class CommuniqueExportFormView(CommuniqueFormView):
    """
    A view that displays a form to pick a duration during which certain models were created so that they can be exported
    """
    form_class = DurationForm

    def form_valid(self, form):
        # get the start and end date on valid form submission
        self.start_date = form.cleaned_data['start_date']
        self.end_date = form.cleaned_data['end_date']
        return super(CommuniqueExportFormView, self).form_valid(form)

    def get_success_view_name(self):
        # return the name of the view to which to redirect to on successful validation
        return None

    def get_success_url(self):
        # on successful validation of form, redirect to the expected export list
        start_date = self.start_date
        end_date = self.end_date

        start_year = '{:04d}'.format(start_date.year)
        end_year = '{:04d}'.format(end_date.year)

        start_month = '{:02d}'.format(start_date.month)
        end_month = '{:02d}'.format(end_date.month)

        start_day = '{:02d}'.format(start_date.day)
        end_day = '{:02d}'.format(end_date.day)
        return reverse(self.get_success_view_name(), kwargs={'start_year': start_year, 'start_month': start_month,
                                                                   'start_day': start_day, 'end_year': end_year,
                                                                   'end_month': end_month, 'end_day': end_day})


class CommuniqueDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    A view that handles displaying details of a model.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    def test_func(self):
        """
        Checks whether the user is marked active.
        :return: True if user is active, false otherwise
        """
        return self.request.user.is_active


class CommuniqueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view that handles updating a model.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    def test_func(self):
        """
        Checks whether the user is marked active.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active

    def form_valid(self, form):
        # update the last modified field of the model
        form.instance.last_modified_by = self.request.user

        return super(CommuniqueUpdateView, self).form_valid(form)


class CommuniqueListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    A view that lists available models.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    def test_func(self):
        """
        Checks whether the user is marked active.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active


class CommuniqueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    A view that handles deletion of a model.

    This view is only available to users that are logged in and are marked as active in the system.
    """
    def test_func(self):
        """
        Checks whether the user is marked active.
        :return: True if user is active, false otherwise.
        """
        return self.request.user.is_active