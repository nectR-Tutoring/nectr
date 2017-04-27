from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from nectr.tutor.models import Tutor


class TutorDetailView(DetailView):
    model = Tutor


class TutorListView(ListView):
    model = Tutor


class TutorCreate(CreateView):
    model = Tutor


class TutorUpdate(UpdateView):
    model = Tutor


class TutorDelete(DeleteView):
    model = Tutor
