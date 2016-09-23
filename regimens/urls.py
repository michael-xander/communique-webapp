from django.conf.urls import url

from .views import (DrugCreateView)


urlpatterns = [
    url(r'^drugs/create/$', DrugCreateView.as_view(), name='regimens_drug_create'),
]