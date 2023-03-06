from django.http import HttpResponse
from django.shortcuts import render


def op(request):
    #return render(request, "index.html")
    return HttpResponse("HOMEPAGE")


