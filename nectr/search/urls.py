from django.conf.urls import url

from nectr.search import views

urlpatterns = [
    url(
        regex=r'^tutors/$',
        view=views.TutorsSearchResultList.as_view(),
        name='list'
    ),
]
