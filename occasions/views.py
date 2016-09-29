from django.core.urlresolvers import reverse_lazy

from .models import Event
from communique.views import (CommuniqueDeleteView, CommuniqueListView, CommuniqueDetailView, CommuniqueUpdateView,
                              CommuniqueCreateView)
from .forms import EventForm


class EventCreateView(CommuniqueCreateView):
    """
    A view that handles creation of an event.
    """
    model = Event
    form_class = EventForm
    template_name = 'occasions/event_form.html'


class EventDetailView(CommuniqueDetailView):
    """
    A view that handles displaying event details.
    """
    model = Event
    template_name = 'occasions/event_view.html'
    context_object_name = 'event'


class EventUpdateView(CommuniqueUpdateView):
    """
    A view that handles updating an event.
    """
    model = Event
    form_class = EventForm
    template_name = 'occasions/event_update_form.html'
    context_object_name = 'event'


class EventListView(CommuniqueListView):
    """
    A view that lists available events.
    """
    model = Event
    template_name = 'occasions/event_list.html'
    context_object_name = 'event_list'


class EventDeleteView(CommuniqueDeleteView):
    """
    A view that handles event deletion.
    """
    model = Event
    success_url = reverse_lazy('occasions_event_list')
    context_object_name = 'event'
    template_name = 'occasions/event_confirm_delete.html'

