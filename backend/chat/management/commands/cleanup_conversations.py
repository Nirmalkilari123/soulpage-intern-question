from django.core.management.base import BaseCommand
from datetime import timedelta
from django.utils import timezone
from myapp.models import Conversation

class Command(BaseCommand):
    help = 'Cleanup old conversations'

    def handle(self, *args, **kwargs):
        cutoff_date = timezone.now() - timedelta(days=30)
        old_conversations = Conversation.objects.filter(created_at__lt=cutoff_date)
        old_conversations.delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted old conversations'))
