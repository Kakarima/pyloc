from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'rental'

urlpatterns = [
    path('', views.home, name='home'),
    path('tourism/categories', views.tourism_categories, name='tourism_categories'),
    path('tourism/categories/<int:id_category>', views.tourism_category, name='tourism_category'),
    path('services/categories', views.services_categories, name='services_categories'),
    path('entreprise/categories', views.entreprise_categories, name='entreprise_categories'),
    path('registration/', views.register, name='registration'),
    path('login/', auth_views.LoginView.as_view(success_url='home'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': 'home'}, name='logout'),
    path('customer/edit', views.edit_customer, name='edit_customer'),
    path('contact/categories', views.contact_categories, name='contact_categories'),
    path('conseils/', views.conseils, name='conseils'),
    path('conditions/', views.conditions, name='conditions'),
    path('partenaires/', views.partenaires, name='partenaires'),
    path('agences/', views.agences, name='agences'),
    path('agences/agence/<int:id_agency>', views.agence, name='agence'),
    path('confidentialite/', views.confidentialite, name='confidentialite'),
    path('register/contract', views.register_contract, name='register_contract'),
]
