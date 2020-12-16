from django.contrib.auth import views as auth_views
from django.core.exceptions import PermissionDenied
from django.urls import path

from . import views

app_name= 'gestion'

urlpatterns = [
        path('', views.gestion, name = 'gestion'),
        path('vehicules/', views.vehicules, name = 'vehicules'),
        path('disponibilites/', views.disponibilites, name = 'disponibilites'),
        path('reservation/', views.reservation, name = 'reservation'),
]