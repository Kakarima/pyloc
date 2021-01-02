from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.core.exceptions import PermissionDenied

app_name = 'rental'


def permission_denied_view():
    raise PermissionDenied


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
    path('403/', permission_denied_view, name='forbidden'),
]

# Here’s what LoginView does:
# If called via GET, it displays a login form that POSTs to the same URL. More on this in a bit.
# If called via POST with user submitted credentials, it tries to log the user in.
# If login is successful, the view redirects to the URL specified in next.
# If next isn’t provided, it redirects to settings.LOGIN_REDIRECT_URL
# (which defaults to /accounts/profile/). If login isn’t successful, it redisplays the login form.
