from django.db import models
from django.utils import timezone

from nectr.users.models import User


class ConversationManager(models.Manager):
    def get_unread_dict(self, for_user):
        user_dict = {}
        not_user = User.objects.exclude(id=for_user.id)
        for user in not_user:
            conversation = Conversation.objects.filter(
                models.Q(recipient=for_user) & models.Q(initiator=user) |
                models.Q(initiator=for_user) & models.Q(recipient=user)).first()
            if not conversation:
                user_dict.update({user: 0})
                continue
            last_read_time = conversation.initiator_last_read_time if conversation.initiator == for_user else conversation.recipient_last_read_time
            unread_count = Message.objects.filter(
                models.Q(conversation=conversation) &
                models.Q(created_at__gt=last_read_time)).count()
            user_dict.update({user: unread_count})
        return user_dict


class Conversation(models.Model):
    objects = ConversationManager()

    initiator = models.ForeignKey(User, related_name='+')  # TODO: Refactor this into ManyToMany when chat groups will be implemented.
    recipient = models.ForeignKey(User, related_name='+')
    initiator_last_read_time = models.DateTimeField(default=timezone.now()) #TODO: This is adding extra migrations becuase the now is changing
    recipient_last_read_time = models.DateTimeField(default=timezone.now())


class Message(models.Model):
    text = models.CharField(max_length=1024)
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    conversation = models.ForeignKey(Conversation)

    def __str__(self):
        return '{}: {}'.format(self.author, self.text)
