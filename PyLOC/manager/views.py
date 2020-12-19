from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from rental.models import Vehicle, Agency
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def vehicules(request):
    return render(request, 'manager/vehicules.html')

class LoginManager(LoginView):
    template_name = 'manager/login.html'

    def get_success_url(self):
        return reverse('manager:gestion')

def role_check(user):
    return user.groups.filter(name='managers').exists()

@login_required(login_url='manager:login')
@user_passes_test(role_check, login_url='manager:forbidden')

def gestion(request):
    return render(request,'manager/gestion.html', {})

@login_required(login_url='manager:login')
def vehicules(request):
    toutesLesVehicules = Vehicle.objects.all()
    toutesLesAgences = Agency.objects.all()
    return render(request,'manager/vehicules.html', {'vehicules': toutesLesVehicules, 'agences': toutesLesAgences})

@login_required(login_url='manager:login')
def compte(request):
    return render(request,'manager/compte.html', {})

@login_required()
def logged_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('manager:login'))


def disponibilites(request):
    return render(request, 'gestion/disponibilites.html')

def reservation(request):
    return render(request, 'gestion/reservation.html')