from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
from core.models import Evento


def login_user(request):
    return render(request, 'login.html')


def submit_login_user(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('pw')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido! ")
    return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def lista_eventos_usuario(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)


@login_required(login_url='/login/')
def add_evento(request):
    return render(request, 'evento.html')


@login_required(login_url='/login/')
def submit_add_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        desc = request.POST.get('descricao')
        data_evento = request.POST.get('data_evento')
        local = request.POST.get('local')
        usuario = request.user
        Evento.objects.create(titulo=titulo,
                              descricao=desc,
                              data_evento=data_evento,
                              local=local,
                              usuario=usuario)
    return redirect('/')


# Eventos desabilitados
# @login_required(login_url='/login/')
# def eventos(request, titulo_evento):
#    obj_evento = Evento.objects.get(titulo=titulo_evento)
#    return HttpResponse('Nome do Evento: {}<br>Local: {}'.format(obj_evento.titulo, obj_evento.local))


# @login_required(login_url='/login/')
# def lista_evento_id(request, id):
#    evento = Evento.objects.get(id=id)
#    dados = {'evento': evento}
#    return render(request, 'agenda.html', dados)


# @login_required(login_url='/login/')
# def lista_todos_eventos(request):
#    evento = Evento.objects.all()
#    dados = {'eventos': evento}
#    return render(request, 'agenda.html', dados)
