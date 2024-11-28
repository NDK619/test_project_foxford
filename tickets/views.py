from rest_framework import viewsets
from .models import Ticket, Message
from .serializers import TicketSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [AllowAny]  # Для тестирования можно использовать AllowAny


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [AllowAny]  # Для тестирования можно использовать AllowAny IsAuthenticated
