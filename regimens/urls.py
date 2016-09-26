from django.conf.urls import url

from .views import (DrugCreateView, DrugDetailView, DrugListView, DrugUpdateView, DrugDeleteView, RegimenCreateView,
                    RegimenDetailView, RegimenListView, RegimenDeleteView, RegimenUpdateView)


urlpatterns = [
    url(r'^$', RegimenListView.as_view(), name='regimens_regimen_list'),
    url(r'^create/$', RegimenCreateView.as_view(), name='regimens_regimen_create'),
    url(r'^(?P<pk>[0-9]+)/$', RegimenDetailView.as_view(), name='regimens_regimen_detail'),
    url(r'(?P<pk>[0-9]+)/update/$', RegimenUpdateView.as_view(), name='regimens_regimen_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', RegimenDeleteView.as_view(), name='regimens_regimen_delete'),
    url(r'^drugs/$', DrugListView.as_view(), name='regimens_drug_list'),
    url(r'^drugs/create/$', DrugCreateView.as_view(), name='regimens_drug_create'),
    url(r'^drugs/(?P<pk>[0-9]+)/$', DrugDetailView.as_view(), name='regimens_drug_detail'),
    url(r'^drugs/(?P<pk>[0-9]+)/update/$', DrugUpdateView.as_view(), name='regimens_drug_update'),
    url(r'^drugs/(?P<pk>[0-9]+)/delete/$', DrugDeleteView.as_view(), name='regimens_drug_delete'),
]