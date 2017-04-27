from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from nectr.tutor.models import Tutor


class TutorDetailView(DetailView):
    model = Tutor


class TutorListView(ListView):
    model = Tutor
    template_name = 'search/tutor/tutor_search_result_list.html'
    paginate_by = 10
    context_object_name = 'tutors_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Tutor.objects.filter(courses=query)


class TutorCreate(CreateView):
    model = Tutor


class TutorUpdate(UpdateView):
    model = Tutor


class TutorDelete(DeleteView):
    model = Tutor
