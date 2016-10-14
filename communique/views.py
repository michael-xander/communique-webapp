from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse

import datetime

from .forms import DurationForm

# the date format to be used in
DATE_FORMAT = '%d-%m-%Y'
DATE_FORMAT_STR = 'dd-mm-yyyy'


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
        """
        A method to retrieve the name of the view to redirect to on successful valiation of the form
        :return: The name of the view
        """
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

        # redirect to the view with the overridden name method
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


class CommuniqueListAndExportView(CommuniqueListView):
    """
    A view that lists instances of a model and exports them to csv file when provided an export get parameter
    """

    def csv_export_response(self, context):
        """
        A method that returns the HTTP response to download a csv file with the items in the export list
        :param context: The context data for the view
        :return: The HTTP response
        """
        return None

    def render_to_response(self, context, **response_kwargs):
        # if there is a get parameter named export with the value csv and there are objects in the list then respond
        # with a csv file of the data
        if ('csv' in self.request.GET.get('export', '')) and context[self.context_object_name]:
            return self.csv_export_response(context)
        else:
            return super(CommuniqueListAndExportView, self).render_to_response(context, **response_kwargs)


class CommuniqueDetailAndExportView(CommuniqueDetailView):
    """
    A view that displays the details of a model and exports specified information to a csv file when provided an export
    get parameter.
    """

    def csv_export_response(self, context):
        """
        A method that returns the HTTP response to download a csv file
        :param context: The context data for the view
        :return: The HTTP response
        """
        return None

    def render_to_response(self, context, **response_kwargs):
        # if there is a get parameter named export with the value csv, then call for the csv export response
        if 'csv' in self.request.GET.get('export', ''):
            return self.csv_export_response(context)
        else:
            return super(CommuniqueDetailAndExportView, self).render_to_response(context, **response_kwargs)


class CommuniqueExportListView(CommuniqueListAndExportView):
    """
    A view that provides a list of the items that are to be exported
    """

    def get_export_start_date(self):
        """
        A method that returns the start date from which models created can be filtered
        :return: The start date
        """
        start_date = datetime.date(year=int(self.kwargs['start_year']), month=int(self.kwargs['start_month']),
                                   day=int(self.kwargs['start_day']))
        return start_date

    def get_export_end_date(self):
        """
        A method that returns the end date from which models created can be filtered
        :return: The end date
        """
        end_date = datetime.date(year=int(self.kwargs['end_year']), month=int(self.kwargs['end_month']),
                                 day=int(self.kwargs['end_day']))
        return end_date

    def get_context_data(self, **kwargs):
        # add the duration from to the context
        context = super(CommuniqueExportListView, self).get_context_data(**kwargs)

        start_date = self.get_export_start_date()
        end_date = self.get_export_end_date()
        data = {'start_date':start_date, 'end_date':end_date}

        context['form'] = DurationForm(data)
        return context


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