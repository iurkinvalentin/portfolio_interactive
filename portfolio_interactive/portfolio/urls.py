from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, WebhookAPIView

# Создаем роутер
router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')

# Подключаем маршруты
urlpatterns = [
    path('/portfolio/', include(router.urls)),
    path('portfolio/webhook/', WebhookAPIView.as_view(), name='webhook'),
]
