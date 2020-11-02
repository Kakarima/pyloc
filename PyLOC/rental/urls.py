from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tourism/categories', views.tourism_categories, name='tourism_categories'),
    path('tourism/categories/<int:id>', views.tourism_category, name='tourism_category'),
    path('utilitaires/categories', views.utilitaires_categories, name='utilitaires_categories'),
    path('services/categories', views.services_categories, name='services_categories'),
    path('agences/categories', views.agences_categories, name='agences_categories'),
    path('entreprise/categories', views.entreprise_categories, name='entreprise_categories'),
    path('todo/categories', views.todo_categories, name='todo_categories'),

]
