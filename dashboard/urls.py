from django.conf.urls import url, include
from .views import DashboardView
from support_services import urls as support_services_urls
urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='dashboard_home'),
    url(r'^services/', include(support_services_urls)),
]
