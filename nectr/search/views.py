from django.shortcuts import render, get_list_or_404

from nectr.tutor.models import Tutor


def search(request):
    tutors = get_list_or_404(Tutor)
    return render(request, 'search/tutor/tutor_search_result_list.html', tutors)
