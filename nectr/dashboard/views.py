from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from nectr.courses.models import Courses
from nectr.dashboard.forms import CoursesForm
from nectr.users.models import User


class DashboardView(TemplateView):
    template_name = "dashboard/base_dashboard.html"


class DashboardEditProfile(TemplateView):
    template_name = "dashboard/edit_profile.html"

    def post(self, request):
        post = request.POST
        request.user.first_name = post.get('first_name')
        request.user.last_name = post.get('last_name')
        request.user.bio = post.get('edit_bio')
        request.user.street_address_1 = post.get('street_address')
        request.user.city = post.get('city')
        request.user.country = post.get('country_text')
        request.user.zip_code = post.get('zipcode_text')
        return render(request, self.template_name)


class DashboardEditCourses(TemplateView):
    model = User
    template_name = "dashboard/edit_courses.html"

    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard/edit_courses.html', {'courses': request.user.courses})

    def post(self, request):
        if request.POST.get('course'):
            request.user.courses.create(course_name=request.POST.get('course'), subject=request.POST.get('subject'))

        return render(request, 'dashboard/edit_courses.html', {'courses': request.user.courses})


class DashboardEditSkills(TemplateView):
    model = User
    template_name = "dashboard/edit_skills.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'skills': request.user.skills})

    def post(self, request):
        if request.POST.get('skills'):
            request.user.skills.create(skill=request.POST.get('skills'))

        return render(request, self.template_name, {'courses': request.user.skills})
