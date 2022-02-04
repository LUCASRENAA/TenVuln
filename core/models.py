from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Senhas(models.Model):
    nome = models.CharField(max_length=50)
    senhas = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Chat(models.Model):
    titulo = models.CharField(max_length=50)

    de = models.ForeignKey(User, models.CASCADE, related_name='de')
    mensagem = models.CharField(max_length=50)
    para = models.ForeignKey(User, models.CASCADE, related_name='para')
