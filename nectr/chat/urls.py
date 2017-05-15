from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from nectr.chat import views

urlpatterns = [
    url(
        regex=r'^$',
        view=login_required(views.ChatView.as_view()),
        name='chat_view'
    )
]
