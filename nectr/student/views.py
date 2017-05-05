from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse
from django.views.generic import TemplateView

from nectr.student.models import Student, StudentLikes
from nectr.tutor.models import Tutor


class StudentPublicProfile(TemplateView):
    model = Tutor
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'dashboard/student_public_profile.html'

    def profile_load(self, request):
        likes = StudentLikes.objects.all()
        return TemplateResponse(request, self.template_name, {'likes': likes})
