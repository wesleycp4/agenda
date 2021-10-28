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
            messages.error(request,"Usuário ou senha inválido! ")
    return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def eventos(request, titulo_evento):
    obj_evento = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse('Nome do Evento: {}<br>Local: {}'.format(obj_evento.titulo, obj_evento.local))


@login_required(login_url='/login/')
def lista_evento_id(request, id):
    evento = Evento.objects.get(id=id)
    dados = {'evento': evento}
    return render(request, 'agenda.html', dados)


@login_required(login_url='/login/')
def lista_todos_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)


@login_required(login_url='/login/')
def lista_eventos_usuario(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)


