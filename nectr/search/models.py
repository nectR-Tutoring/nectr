from django.db import models

# Create your models here.
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from nectr.tutor.models import Tutor


class Search(models.Model):
    search_text = models.TextField(default='No Search Given')


class SearchResultTutorListViewAll(ListView):
    model = Tutor

    def get_context_data(self, **kwargs):
        context = super(SearchResultTutorListViewAll, self).get_context_data(**kwargs)
        context['tutors'] = Tutor.objects.all()
        return context


class TutorList(ListView):
    template_name = 'search/tutor/tutor_search_result_list.html'

    def get_queryset(self):
        self.tutor = get_object_or_404(Tutor,name=self.args[0])
        return Tutor.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TutorList, self).get_context_data(**kwargs)
        context['tutor'] = self.tutor
        return context

    def get(self, request, *args, **kwargs):
        pass
