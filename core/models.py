from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(verbose_name='Título do Evento',max_length=100)
    descricao = models.TextField(verbose_name='Descrição do Evento',blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(verbose_name='Data de Criação do Evento',auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo