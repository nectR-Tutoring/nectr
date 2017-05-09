from django.shortcuts import render

from django.views.generic import TemplateView

from nectr.users.models import User


class ChatView(TemplateView):
    template_name = 'chat/base_chat.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ChatView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['user_list'] = User.objects.exclude(id=self.request.user.id)
        return context
