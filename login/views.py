from django.http import HttpResponse


def index(request):
    return HttpResponse("informe seu cpf e sua senha para acessar sua dashboard")
