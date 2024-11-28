from rest_framework import serializers
from .models import Ticket, Message


class MessageSerializer(serializers.ModelSerializer):
    ticket = serializers.PrimaryKeyRelatedField(
        queryset=Message.objects.all())  # Убедитесь, что queryset настроен правильно

    class Meta:
        model = Message
        fields = ['ticket', 'sender', 'text', 'created_at']


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'status', 'operator', 'created_at', 'updated_at']
