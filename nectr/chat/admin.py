from django.contrib import admin

from nectr.chat.models import Message, Conversation


@admin.register(Conversation, Message)
class ConversationAdmin(admin.ModelAdmin):
    pass
