from django.urls import path
from .import views

urlpatterns = [
        path('', views.gestion, name = 'gestion'),
        path('vehicules/categories', views.vehicules_categories, name = 'vehicules_categories'),
        path('disponibilites/categories', views.disponibilites_categories, name = 'disponibilites_categories'),
        path('reservation/categories', views.reservation_categories, name = 'reservation_categories'),
]