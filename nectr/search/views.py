from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from nectr.tutor.models import Tutor

#TODO::
def tutor_search_result_list(request):
    if request.method == 'GET':
        tutors = Tutor.objects.all()
        return render(request, 'search/tutor/tutor_search_result_list.html', {'tutors': tutors})
    return request


