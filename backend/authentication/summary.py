from django.contrib import admin
from .models import Conversation

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'participants_display')

    def participants_display(self, obj):
        return ", ".join([p.username for p in obj.participants.all()])
    participants_display.short_description = 'Participants'
