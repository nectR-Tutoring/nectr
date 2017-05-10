from django.db import models
from django.utils import timezone

from nectr.users.models import User


class Conversation(models.Model):
    initiator = models.ForeignKey(User, related_name='+')  # TODO: Refactor this into ManyToMany when chat groups will be implemented.
    recipient = models.ForeignKey(User, related_name='+')
    initiator_last_read_time = models.DateTimeField(default=timezone.now())
    recipient_last_read_time = models.DateTimeField(default=timezone.now())


class Message(models.Model):
    text = models.CharField(max_length=1024)
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    conversation = models.ForeignKey(Conversation)

    def __str__(self):
        return '{}: {}'.format(self.author, self.text)
