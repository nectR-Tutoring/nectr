from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from nectr.tutor.models import Tutor


def get_tutor_profile_by_username(request, username):
    tutor = get_object_or_404(Tutor, user__username=username)
    courses = tutor.courses
    return render(request, template_name='tutors/tutor_detail.html', context={'tutor': tutor, 'courses': courses})


class TutorDetailView(DetailView):
    model = Tutor
    # These next two lines tell the view to index lookups by username
    # slug_field = 'user'
    slug_url_kwarg = 'username'

    def get_queryset(self):
        return Tutor.objects.filter(user__username=self.get_slug_field())


class TutorListView(ListView):
    model = Tutor
    template_name = 'search/tutor/tutor_search_result_list.html'
    paginate_by = 10
    context_object_name = 'tutors_list'

    def get_queryset(self):
        query = self.request.GET.get('search_text')
        return Tutor.objects.filter(courses=query)


class TutorCreate(CreateView):
    model = Tutor


class TutorUpdate(UpdateView):
    model = Tutor


class TutorDelete(DeleteView):
    model = Tutor


class TutorProfile(object):
    model = Tutor
