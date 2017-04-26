from django.shortcuts import render


# Create your views here.
from nectr.tutor.models import Tutor


def TutorsSearchResultList(request):
    if request.method == 'GET':
        Tutor.objects.get()
