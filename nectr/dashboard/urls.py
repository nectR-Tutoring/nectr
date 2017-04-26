from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from nectr.dashboard.views import DashboardView

urlpatterns = [
    url(
        regex=r'^$',
        view=login_required(DashboardView.as_view()),
        name='dashboard_view'
    ),
]
