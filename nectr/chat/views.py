from django.views.generic import TemplateView
from django.db.models import Q

from nectr.users.models import User
from nectr.chat.models import Conversation, Message


class ChatView(TemplateView):
    template_name = 'chat/base_chat.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ChatView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        user_dict = {}
        not_user = User.objects.exclude(id=self.request.user.id)
        for user in not_user:
            conversation = Conversation.objects.filter(
                Q(recipient=self.request.user) & Q(initiator=user) |
                Q(initiator=self.request.user) & Q(recipient=user)).first()
            last_read_time = conversation.initiator_last_read_time if conversation.initiator == self.request.user else conversation.recipient_last_read_time
            unread_count = Message.objects.filter(Q(conversation=conversation) &
                                              Q(created_at__gt=last_read_time)).count()
            user_dict.update({user: unread_count})
        context['user_dict'] = user_dict
        return context
