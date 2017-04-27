from django.conf.urls import url
from . import views
urlpatterns = [
    url (
        url(
            regex=r'^$',
            view=views.TutorListView.as_view(),
            name='search_default'
        ),
    )
]
