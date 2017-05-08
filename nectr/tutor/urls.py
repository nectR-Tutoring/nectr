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
    url(
        regex=r'^update/profile$',
        view=views.TutorProfile
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.get_tutor_profile_by_username,
        name='detail'
    ),

]
