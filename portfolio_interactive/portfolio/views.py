from rest_framework.response import Response
import requests
from rest_framework.views import APIView
from rest_framework import status, viewsets
from .models import Project
from django.conf import settings
from .serializers import ProjectSerializer, ContactFormSubmissionSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WebhookAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactFormSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Form submitted successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_to_telegram(message):
    """Функция отправки сообщения в Telegram"""
    bot_token = settings.TELEGRAM_BOT_TOKEN  # Добавьте в settings.py
    chat_id = settings.TELEGRAM_CHAT_ID      # Добавьте в settings.py
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка отправки в Telegram: {e}")