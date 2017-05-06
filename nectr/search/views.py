from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_list_or_404
from django.views import View

from nectr.tutor.models import Tutor


class Search(View):
    model = Tutor

    @staticmethod
    def get(request):
        search = request.GET.get('search_text', '')
        if search is not '':
            tutors = Tutor.objects.get(courses__course_name__contains=search)
            return render(request, 'search/search_with_results.html', {'tutors': tutors, 'search_text': search})
        else:
            tutors = Tutor.objects.all()
            return render(request, 'search/base_search.html', {'tutors': tutors})
