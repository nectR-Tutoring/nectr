from django.views.generic import TemplateView

from nectr.chat.models import Conversation


class ChatView(TemplateView):
    template_name = 'chat/base_chat.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ChatView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['user_dict'] = Conversation.objects.get_unread_dict(self.request.user)
        return context
