from rest_framework import viewsets
from .models import Mensajes
from .serializers import MensajesSerializer
from rest_framework.permissions import IsAuthenticated  # Importar el permiso de autenticación


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Mensajes.objects.all()
    serializer_class = MensajesSerializer
    permission_classes = [IsAuthenticated]  # Establecer el permiso de autenticación

