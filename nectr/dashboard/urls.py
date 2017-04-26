from django.conf.urls import url

from nectr.dashboard.views import DashboardView

urlpatterns = [
    url(
        regex=r'^dashboard$',
        view=DashboardView.as_view(),
        name='dashboard_view'
    ),
]
