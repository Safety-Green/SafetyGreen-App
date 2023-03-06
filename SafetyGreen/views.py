from django.http import HttpResponse
from django.shortcuts import render


def opp(request):
    return render(request, "index.html")
    #return HttpResponse("HOMEPAGE")


