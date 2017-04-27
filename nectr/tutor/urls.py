from django.conf.urls import url

from nectr.tutor import views

urlpatterns = [
    #Search Tutor by name
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.TutorDetailView.as_view(),
        name='detail'
    )
]
