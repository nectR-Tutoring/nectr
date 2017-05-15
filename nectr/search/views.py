from django.shortcuts import render
from django.views import View

from nectr.tutor.models import Tutor
from nectr.users.models import User


class Search(View):
    model = Tutor

    @staticmethod
    def get(request):
        search = request.GET.get('search_text', '')
        if search is not '':
            users_courses = User.objects.filter(courses__course_name__contains=search)
            users_skills = User.objects.filter(skills__skill__contains=search)
            users_name = User.objects.filter(name__contains=search)
            from itertools import chain
            users = list(chain(users_courses, users_skills, users_name))
        else:
            users = User.objects.all()
        return render(request, 'search/base_search.html', {'tutors': users, 'search_text': search})
