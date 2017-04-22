from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def search_page(request):
    return render(request, 'search.html')


def search(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['Computer Science'])
