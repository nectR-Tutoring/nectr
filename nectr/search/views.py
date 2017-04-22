from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def search_page(request):
    return render(request, 'search.html',
                  {'search_text': request.POST.get('search_text', '')})
