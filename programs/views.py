from django.core.urlresolvers import reverse_lazy

from .models import Program
from communique.views import (CommuniqueDeleteView, CommuniqueListView, CommuniqueDetailView, CommuniqueUpdateView,
                              CommuniqueCreateView)


class ProgramListView(CommuniqueListView):
    """
    A view to list all programs of the system.
    """
    model = Program
    template_name = "programs/program_list.html"
    context_object_name = 'program_list'


class ProgramCreateView(CommuniqueCreateView):
    """
    A view to handle creation of a Program by displaying the form and handling the post request.
    """
    model = Program
    fields = ['name', 'description']
    template_name = 'programs/program_form.html'


class ProgramDetailView(CommuniqueDetailView):
    """
    A view to display the details of a Program.
    """
    model = Program
    template_name = 'programs/program_view.html'
    context_object_name = 'program'


class ProgramUpdateView(CommuniqueUpdateView):
    """
    A view to update the details of a Program.
    """
    model = Program
    fields = ['name', 'description']
    template_name = 'programs/program_update_form.html'
    context_object_name = 'program'


class ProgramDeleteView(CommuniqueDeleteView):
    """
    A view to handle deletion of a program.
    """
    model = Program
    success_url = reverse_lazy('programs_program_list')
    context_object_name = 'program'
    template_name = 'programs/program_confirm_delete.html'
