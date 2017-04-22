from django.http import HttpResponse
from django.shortcuts import render

from nectr.search.models import Search


def search_page(request):
    if request.method == 'POST':
        new_search_text = request.POST['search_text']
        Search.objects.create(search_text=new_search_text)
    else:
        new_search_text = ''

    return render(request, 'search.html', {
        'search_text': new_search_text,
    })
