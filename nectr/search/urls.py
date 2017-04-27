from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.search,
        name='search_base'
    ),
    url(
        regex='^the_hive$',
        view=TemplateView.as_view(template_name='look_nectr.html')
    )
]
