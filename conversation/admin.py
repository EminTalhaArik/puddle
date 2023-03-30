from django.contrib import admin


from .models import Conversation, ConversatioNmessage

admin.site.register(Conversation)
admin.site.register(ConversatioNmessage)