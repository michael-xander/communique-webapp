from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


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