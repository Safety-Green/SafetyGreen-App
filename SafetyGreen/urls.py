from django.contrib import admin
from django.urls import path, include

from SafetyGreen import views

urlpatterns = [
    path('', views.opp),
    path('admin/', admin.site.urls),
]
