from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Регистрируем вьюсеты в роутере
router = DefaultRouter()
router.register(r'tickets', views.TicketViewSet)
router.register(r'messages', views.MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Включаем все маршруты, сгенерированные роутером
]
