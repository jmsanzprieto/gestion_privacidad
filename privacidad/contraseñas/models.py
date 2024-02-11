from django.db import models
from django.contrib.auth.models import User

class Contraseñas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - {self.service}"
