from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from rental.models import Vehicle, Agency, Category
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from manager.forms import VehicleForm

# Gestion des véhicules #

def vehicules(request):
    vehicules = Vehicle.objects.all()
    return render(request, 'manager/vehicules.html', {'vehicules': vehicules})

def suppression_vehicule(request, id_vehicule):
    edit_vehicule = Vehicle.objects.get(id=id_vehicule)
    edit_vehicule.delete()
    return redirect('/manager/vehicules/liste')

def ajout_vehicule(request):
    next_page = request.GET.get('next', '')
    if request.method == 'POST':
        vehicule_form = VehicleForm(request.POST, files=request.FILES)
        if vehicule_form.is_valid():
            vehicule = vehicule_form.save(commit=False)
            agence = Agency.objects.get(id=request.POST.get('agencies'))
            cat = Category.objects.get(id=request.POST.get('categories'))
            vehicule.agence = agence
            vehicule.category = cat
            vehicule.save()
            return redirect('/manager/vehicules/liste')
    else:
        vehicle_form = VehicleForm()
        return render(request, 'manager/ajout_vehicule.html',
                      {'vehicle_form': vehicle_form})

# Gestion du login manager #

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
@user_passes_test(role_check, login_url='manager:forbidden')
def vehicules(request):
    toutesLesVehicules = Vehicle.objects.all()
    toutesLesAgences = Agency.objects.all()
    return render(request,'manager/vehicules.html', {'vehicules': toutesLesVehicules, 'agences': toutesLesAgences})

@login_required(login_url='manager:login')
@user_passes_test(role_check, login_url='manager:forbidden')
def compte(request):
    return render(request,'manager/compte.html', {})

@login_required()
def logged_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('manager:login'))

