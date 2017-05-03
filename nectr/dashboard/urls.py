from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from nectr.dashboard import views
from nectr.dashboard.views import DashboardView

urlpatterns = [
    url(
        regex=r'^$',
        view=login_required(DashboardView.as_view()),
        name='dashboard_view'
    ),
    url(
        regex=r'^student_dashboard',
        view=login_required(views.student_dashboard),
        name='student_dashboard'
    )
]
