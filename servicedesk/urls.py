from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# Генерация схемы для Swagger
# schema_view = get_schema_view(
#     openapi.Info(
#         title="ServiceDesk API",
#         default_version='v1',
#         description="API для управления заявками",
#         contact=openapi.Contact(email="contact@servicedesk.local"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     #permission_classes=(permissions.AllowAny,)  # Разрешаем доступ всем пользователям
# )

urlpatterns = [
    # Маршруты для админки и API
    path('admin/', admin.site.urls),
    path('api/', include('tickets.urls')),  # Ваши маршруты API

    # Схема API
    path('schema/', SpectacularAPIView.as_view(), name='schema'),  # Генерация схемы

    # Swagger UI
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Отображение Swagger UI
]

# Для обслуживания статики в режиме отладки
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)