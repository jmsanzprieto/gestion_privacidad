from rest_framework import serializers
from .models import Mensajes

class MensajesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensajes
        fields = '__all__'
