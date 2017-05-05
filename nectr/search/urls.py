from django.conf.urls import url
from django.views.generic import TemplateView

from nectr.search.views import Search
from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=Search.as_view(),
        name='search_base'
    ),
    url(
        regex='^the_hive$',
        view=TemplateView.as_view(template_name='look_nectr.html')
    )

]
