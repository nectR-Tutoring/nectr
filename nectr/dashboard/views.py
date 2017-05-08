from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = "dashboard/base_dashboard.html"


class DashboardEditProfile(TemplateView):
    template_name = "dashboard/edit_profile.html"


