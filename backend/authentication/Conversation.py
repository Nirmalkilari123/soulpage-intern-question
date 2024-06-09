from django.db import models

class Conversation(models.Model):
    title = models.CharField(max_length=255)
    participants = models.ManyToManyField(User)
    # Add the new field
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
