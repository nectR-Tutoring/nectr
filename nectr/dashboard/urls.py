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
]
