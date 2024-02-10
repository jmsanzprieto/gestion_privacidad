from django.contrib import admin
from .models import Mensajes

class MensajesAdmin(admin.ModelAdmin):
    # Define los campos que deseas mostrar en la lista de objetos
    list_display = ('content', 'created_at')

# Registra el modelo Mensajes con su administrador personalizado
admin.site.register(Mensajes, MensajesAdmin)
