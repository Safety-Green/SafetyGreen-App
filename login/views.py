from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
    return HttpResponse("informe seu cpf e sua senha para acessar sua dashbo")

def entrar(request):
    if  request.method == "GET":
        return render(request,'HTML/entrar.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        if user:
            login(request, user)
            return HttpResponse('autenticado')
        else:
            return HttpResponse('nome ou senha inavlidos')

def cadastrar(request):
    if request.method == "GET":    
        return render(request,'HTML/cadastrar.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()
        if user: 
            return HttpResponse("ja existe um usuario com esse nome")
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HttpResponse('usuario cadastrado com sucesso: ')
    
def dashboard(request):
    if request.user.is_authenticated:
        return HttpResponse('sua dashboard')
    return HttpResponse('erro 401, vc precisa estar logado')
