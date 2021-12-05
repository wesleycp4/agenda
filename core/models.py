from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, timedelta


class Evento(models.Model):
    titulo = models.CharField(verbose_name='Título do Evento', max_length=100)
    descricao = models.TextField(verbose_name='Descrição do Evento', blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(verbose_name='Data de Criação do Evento', auto_now=True)
    local = models.CharField(verbose_name='Local do Evento', max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        test = self.data_evento.strftime('Dia: %d/%m/%Y às %H:%M Horas')
        return test

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False
