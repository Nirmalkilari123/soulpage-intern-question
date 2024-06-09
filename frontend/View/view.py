from rest_framework import serializers, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from .models import Conversation

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ['title', 'summary', 'participants']

class ConversationPagination(PageNumberPagination):
    page_size = 10

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    pagination_class = ConversationPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'summary']
