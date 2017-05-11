from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from nectr.courses.models import Courses
from nectr.users.models import User


class DashboardView(TemplateView):
    template_name = "dashboard/base_dashboard.html"


class DashboardEditProfile(TemplateView):
    template_name = "dashboard/edit_profile.html"


class DashboardEditCourses(TemplateView):
    template_name = "dashboard/edit_courses.html"

    def post(self, request):
        user = User.objects.get(username=request.user.username)
        user.courses.subject = request.POST.get('subject')
        user.courses.course_name = request.POST.get('course')
        return render(request, 'dashboard/edit_courses.html', {'courses' : user.courses})


class DashboardEditSkills(TemplateView):
    template_name = "dashboard/edit_skills.html"
