from django.conf.urls import url

from nectr.tutor import views

urlpatterns = [
    #Search Tutor by name
    # url(
    #     regex=r'^(?P<username>[\w.@+-]+)/$',
    #     view=views.TutorDetailView.as_view(),
    #     name='tutor_detail'
    # ),
    url(
        regex=r'^list/$',
        view=views.TutorListView.as_view(),
        name='tutor_lists'
    ),

]
