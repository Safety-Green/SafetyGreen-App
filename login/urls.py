
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entrar/', views.entrar, name='entrar'),
    path('cadastrar/',views.cadastrar,name='cadastrar'),
    path('dashboard/', views.dashboard, name='dashboard')
]