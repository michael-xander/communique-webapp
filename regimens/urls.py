from django.conf.urls import url

from .views import (DrugCreateView, DrugDetailView, DrugListView, DrugUpdateView, DrugDeleteView, RegimenCreateView,
                    RegimenDetailView, RegimenListView, RegimenDeleteView, RegimenUpdateView, RegimenExportFormView,
                    RegimenExportListView)


urlpatterns = [
    url(r'^$', RegimenListView.as_view(), name='regimens_regimen_list'),
    url(r'^create/$', RegimenCreateView.as_view(), name='regimens_regimen_create'),
    url(r'^export/$', RegimenExportFormView.as_view(), name='regimens_regimen_export_form'),
    url(r'^export/(?P<start_year>[0-9]{4})-(?P<start_month>[0-9]{2})-(?P<start_day>[0-9]{2})/(?P<end_year>[0-9]{4})-(?P<end_month>[0-9]{2})-(?P<end_day>[0-9]{2})/$',
        RegimenExportListView.as_view(), name='regimens_regimen_export_list'),
    url(r'^(?P<pk>[0-9]+)/$', RegimenDetailView.as_view(), name='regimens_regimen_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', RegimenUpdateView.as_view(), name='regimens_regimen_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', RegimenDeleteView.as_view(), name='regimens_regimen_delete'),
    url(r'^drugs/$', DrugListView.as_view(), name='regimens_drug_list'),
    url(r'^drugs/create/$', DrugCreateView.as_view(), name='regimens_drug_create'),
    url(r'^drugs/(?P<pk>[0-9]+)/$', DrugDetailView.as_view(), name='regimens_drug_detail'),
    url(r'^drugs/(?P<pk>[0-9]+)/update/$', DrugUpdateView.as_view(), name='regimens_drug_update'),
    url(r'^drugs/(?P<pk>[0-9]+)/delete/$', DrugDeleteView.as_view(), name='regimens_drug_delete'),
]