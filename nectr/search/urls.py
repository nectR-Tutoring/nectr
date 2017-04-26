from django.conf.urls import url

from nectr.search import views

urlpatterns = [
    url(
        #TODO:
        regex=r'^tutors/$',
        view=views.tutor_search_result_list,
        name='list'
    ),
]
