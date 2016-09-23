from django.conf.urls import url

from .views import (DrugCreateView, DrugDetailView, DrugListView)


urlpatterns = [
    url(r'^drugs/$', DrugListView.as_view(), name='regimens_drug_list'),
    url(r'^drugs/create/$', DrugCreateView.as_view(), name='regimens_drug_create'),
    url(r'^drugs/(?P<pk>[0-9]+)/$', DrugDetailView.as_view(), name='regimens_drug_detail'),
]