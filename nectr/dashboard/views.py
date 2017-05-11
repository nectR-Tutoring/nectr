from django.conf.urls import url
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView

from nectr.courses.models import Courses
from nectr.dashboard.forms import CoursesForm
from nectr.skills.models import Skills
from nectr.users.models import User


class DashboardView(TemplateView):
    template_name = "dashboard/base_dashboard.html"


class DashboardEditProfile(TemplateView):
    template_name = "dashboard/edit_profile.html"

    def post(self, request):
        post = request.POST
        User.objects.filter(username__exact=request.user.username).update(
            first_name=post.get('first_name'),
            last_name=post.get('last_name'),
            bio=post.get('edit_bio'),
            street_address_1=post.get('street_address'),
            city=post.get('city'),
            country=post.get('country_text'),
            zip_code=post.get('zipcode_text')
        )
        return HttpResponseRedirect(reverse('dashboard:edit_profile'))


class DashboardEditCourses(TemplateView):
    model = User
    template_name = "dashboard/edit_courses.html"

    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard/edit_courses.html', {'courses': request.user.courses})

    def post(self, request):
        if request.POST.get('delete'):
            course_id = request.POST.get('delete')
            course = Courses.objects.get(id=course_id)
            user = User.objects.get(username__exact=request.user.username)
            user.courses.remove(course)
        if request.POST.get('create'):
            if request.POST.get('course'):
                course = request.POST.get('course')
                request.user.courses.create(course_name=course, subject=request.POST.get('subject'))

        return HttpResponseRedirect(reverse('dashboard:edit_courses'))


class DashboardEditSkills(TemplateView):
    model = User
    template_name = "dashboard/edit_skills.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'skills': request.user.skills})

    def post(self, request):
        if request.POST.get('delete'):
            skill_id = request.POST.get('delete')
            skill = Skills.objects.get(id=skill_id)
            user = User.objects.get(username__exact=request.user.username)
            user.courses.remove(skill)
        if request.POST.get('create'):
            if request.POST.get('skills'):
                skill = request.POST.get('skills')
                request.user.skills.create(skill=skill)

        return HttpResponseRedirect(reverse('dashboard:edit_skills'))
