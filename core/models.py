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


class Pontuacao(models.Model):

    usuario = models.ForeignKey(User, models.CASCADE, related_name='pontuacao')
    pontuacao = models.IntegerField()


class OWASP(models.Model):
    titulo = models.CharField(max_length=50)
    posicao = models.IntegerField()
    ano = models.IntegerField()
    def __str__(self):
            return self.titulo+ ": "+ str(self.ano)

class QuestaoResposta(models.Model):
    questao = models.CharField(max_length=50)
    resposta = models.CharField(max_length=50)
    owasp = models.ForeignKey(OWASP, models.CASCADE)

    def __str__(self):
            return self.questao


class QuestaoUsuario(models.Model):

    usuario = models.ForeignKey(User, models.CASCADE)
    questao = models.ForeignKey(QuestaoResposta, models.CASCADE)
    boleean = models.BooleanField()