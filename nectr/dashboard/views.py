from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = "dashboard/base_dashboard.html"


class DashboardEditProfile(TemplateView):
    template_name = "dashboard/edit_profile.html"


class DashboardEditCourses(TemplateView):
    template_name = "dashboard/edit_courses.html"

    def post(self, request):
        return render(request, 'dashboard/edit_courses.html')


class DashboardEditSkills(TemplateView):
    template_name = "dashboard/edit_skills.html"
