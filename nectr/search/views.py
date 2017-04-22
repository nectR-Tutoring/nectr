from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def search_page():
    pass


def search(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['Computer Science'])
