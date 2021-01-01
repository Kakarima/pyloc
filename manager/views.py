from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from rental.models import Vehicle, Agency, Category
from django.http import HttpResponseRedirect
from django.urls import reverse
from manager.forms import VehicleForm
from django.contrib.auth.decorators import permission_required

# Gestion des véhicules #

# We retrieve all the vehicles from the table vehicle
# then we pass the list to the page vehicles.html


def vehicules(request):
    vehicules = Vehicle.objects.all()
    return render(request, 'manager/vehicules.html', {'vehicules': vehicules})


# we try to verify that the user is connected
# then we see if they have the permission to delete the vehicle
# after that we retrieve all the vehicles from the table vehicle
# we search from the table the vehicle that matches the id
# then we delete the vehicle
# finally we redirect the client to the front page of all the vehicle list
@login_required(login_url='manager:login')
@permission_required('rental.delete_vehicle', raise_exception=True)
def suppression_vehicule(request, id_vehicule):
    edit_vehicule = Vehicle.objects.get(id=id_vehicule)
    edit_vehicule.delete()
    return redirect('/manager/vehicules/liste')


# we try to verify that the user is connected
# then we see if they have the permission to add the vehicle
# it retrieves the data from the form (POST)
# we verify that the form is valid
# if it is then we create the vehicle object
@login_required(login_url='manager:login')
@permission_required('rental.add_vehicle', raise_exception=True)
def ajout_vehicule(request):
    if request.method == 'POST':
        vehicule_form = VehicleForm(request.POST, files=request.FILES)
        if vehicule_form.is_valid():
            vehicule = vehicule_form.save(commit=False)
            agence = Agency.objects.get(id=request.POST.get('agencies'))
            # we retrieve the selected agency from the table agency
            cat = Category.objects.get(id=request.POST.get('categories'))
            # we retrieve the selected category from the table category
            vehicule.agence = agence  # we put the agency that we retrieved to the vehicle
            vehicule.category = cat  # we do the same to category
            vehicule.save()  # we save the vehicle
            return redirect('/manager/vehicules/liste')  # we return the front page with the vehicle list
    else:
        vehicle_form = VehicleForm()  # if the method is not POST, so it is GET,
        # we create the form and we display so the user can enter the information
        return render(request, 'manager/ajout_vehicule.html',
                      {'vehicle_form': vehicle_form})  # we pass the form to ajout_vehicule.html and we display it

# Gestion du login manager #


class LoginManager(LoginView):
    template_name = 'manager/login.html'

    # if the login is success, it returns the page gestion.html
    def get_success_url(self):
        return reverse('manager:gestion')


# it checks if the user belongs to the group manager
def role_check(user):
    return user.groups.filter(name='managers').exists()

# it verifies if the manager is connected and if he is manager (if not it displays forbidden)
# if so, we display the page gestion.html


@login_required(login_url='manager:login')
@user_passes_test(role_check, login_url='manager:forbidden')
def gestion(request):
    return render(request, 'manager/gestion.html', {})


# it verifies if the manager is connected and if he is manager (if not it displays forbidden)
# then we retrieve all the vehicle and all the agencies
# we display all the vehicle and the agencies that we retrieved


@login_required(login_url='manager:login')
@user_passes_test(role_check, login_url='manager:forbidden')
def vehicules(request):
    touteslesvehicules = Vehicle.objects.all()
    touteslesagences = Agency.objects.all()
    return render(request, 'manager/vehicules.html', {'vehicules': touteslesvehicules, 'agences': touteslesagences})

# it verifies if the manager is connected and if he is manager (if not it displays forbidden)
# if so, we display the page compte.html


@login_required(login_url='manager:login')
@user_passes_test(role_check, login_url='manager:forbidden')
def compte(request):
    return render(request, 'manager/compte.html', {})


def logged_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('manager:login'))
