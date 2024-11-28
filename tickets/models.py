from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    ]

    id = models.BigAutoField(primary_key=True)  # Автоинкрементируемый ID
    title = models.CharField(max_length=255)  # Название тикета
    description = models.TextField()  # Описание тикета
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')  # Статус тикета
    operator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tickets')  # Оператор тикета (необязательное поле)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания тикета
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего обновления тикета

    def __str__(self):
        return self.title


class Message(models.Model):
    id = models.BigAutoField(primary_key=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='messages')  # Связь с тикетом
    sender = models.CharField(max_length=100)  # Отправитель сообщения
    text = models.TextField()  # Текст сообщения
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания сообщения

    def __str__(self):
        return f"Message from {self.sender} in ticket {self.ticket.title}"
