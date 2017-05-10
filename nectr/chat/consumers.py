from channels.generic.websockets import JsonWebsocketConsumer
from django.db.models import Q, ObjectDoesNotExist

from nectr.chat.models import Conversation, Message
from nectr.users.models import User


class ChatServer(JsonWebsocketConsumer):
    http_user = True

    def connection_groups(self, **kwargs):
        """
        Called to return the list of groups to automatically add/remove
        this connection to/from.
        """
        return [str(self.message.user.id)]

    def connect(self, message, **kwargs):
        """
        Perform things on connection start
        """
        # Accept the connection; this is done by default if you don't override
        # the connect function.
        self.message.reply_channel.send({"accept": True})

    def receive(self, content, **kwargs):
        """
        Called when a message is received with either text or bytes
        filled out.
        """
        # TODO: Refactor this dispatch into something more elegant.
        if content['type'] == 'init':
            self.cmd_init(content['payload'])
        elif content['type'] == 'message':
            self.cmd_message(content['payload'])

    def cmd_init(self, payload):
        try:
            conversation = Conversation.objects.get(
                (Q(recipient_id=int(payload)) & Q(initiator_id=self.message.user.id)) |
                (Q(recipient_id=self.message.user.id) & Q(initiator_id=int(payload))))
        except ObjectDoesNotExist:
            recipient = User.objects.get(id=int(payload))
            conversation = Conversation.objects.create(initiator=self.message.user, recipient=recipient)

        self.message.channel_session['conversation_id'] = conversation.id
        self.message.channel_session['other_user_id'] = conversation.recipient.id if self.message.user == conversation.initiator else conversation.initiator.id

        query = Message.objects.filter(conversation=conversation)
        messages = []
        for message in query: # TODO: Refactor! Assigning user_id here is super dirty!
            messages.append({'user': message.author.username, 'user_id': self.message.channel_session['other_user_id'], 'text': message.text, 'time': message.created_at.isoformat()})
        self.send({'type': 'init', 'payload': messages})

    def cmd_message(self, payload):
        try:
            conversation = Conversation.objects.get(id=self.message.channel_session.get('conversation_id'))
        except ObjectDoesNotExist:
            return

        message = Message.objects.create(text=payload, author=self.message.user, conversation=conversation)
        response = {'type': 'message', 'payload': {'user': message.author.username, 'user_id': message.author.id, 'text': message.text, 'time': message.created_at.isoformat()}}
        self.group_send(str(self.message.channel_session['other_user_id']),
                        response)
        response['payload'].update({'user_id': self.message.channel_session['other_user_id']}) # TODO: Another dirty trick of mine.
        self.send(response)

    def disconnect(self, message, **kwargs):
        """
        Perform things on connection close
        """
        pass
