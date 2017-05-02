from django.conf.urls import url
from .views import StudentPublicProfile

urlpatterns = [
url(
        regex=r'^(?P<student_username>[\w.@+-]+)/$',
        view=StudentPublicProfile.profile_load(),
        name='student_public_profile'
    ),
]
