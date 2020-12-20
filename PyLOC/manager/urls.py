from django.contrib.auth import views as auth_views
from django.core.exceptions import PermissionDenied
from django.urls import path
from django.core.exceptions import PermissionDenied

from . import views

app_name = 'manager'

def permission_denied_view(request):
        raise PermissionDenied

urlpatterns = [
        path('', views.gestion, name = 'gestion'),
        path('compte', views.compte, name='manager_account'),
        path('login', views.LoginManager.as_view(), name='login'),
        path('logged_out', views.logged_out, name='logged_out'),
        path('vehicules/liste', views.vehicules, name='vehicules'),
        path('403', permission_denied_view, name='forbidden'),

        path('disponibilites', views.disponibilites, name = 'disponibilites'),
        path('reservation', views.reservation, name = 'reservation'),
]