from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from core.models import Evento


def eventos(request, titulo_evento):
    obj_evento = Evento.objects.get(titulo = titulo_evento)
    return HttpResponse('Nome do Evento: {}<br>Local: {}'.format(obj_evento.titulo,obj_evento.local))

def lista_evento_id(request, id):
    evento = Evento.objects.get(id=id)
    dados = {'evento': evento}
    return render(request,'agenda.html', dados)

def lista_todos_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request,'agenda.html', dados)

def lista_eventos_usuario(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos':evento}
    return render(request,'agenda.html', dados)
