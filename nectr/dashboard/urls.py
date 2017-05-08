from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from nectr.dashboard import views

urlpatterns = [
    url(
        regex=r'^$',
        view=login_required(views.DashboardView.as_view()),
        name='dashboard_view'
    ),
    url(
        regex=r'^edit_profile',
        view=login_required(views.DashboardEditProfile.as_view()),
        name='edit_profile'
    ),
    url(
        regex=r'^edit_courses',
        view=login_required(views.DashboardEditCourses.as_view()),
        name='edit_courses'
    ),
    url(
        regex=r'^edit_skills',
        view=login_required(views.DashboardEditSkills.as_view()),
        name='edit_skills'
    ),
]
