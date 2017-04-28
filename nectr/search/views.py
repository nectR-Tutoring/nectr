from django.shortcuts import render, get_list_or_404

from nectr.tutor.models import Tutor


def search(request):
    tutors = Tutor.objects.all()
    return render(request, 'search/base_search.html', {'tutors': tutors})
