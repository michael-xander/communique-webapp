from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, View):
    """CBV that displays the entire dashboard"""
    template_name = "dashboard/dashboard_view.html"

    def get(self, request):
        return render(request, self.template_name)
