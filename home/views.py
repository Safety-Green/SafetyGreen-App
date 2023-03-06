from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
    return HttpResponse("informe seu cpf e sua senha para acessar sua dashboard")


