from django.shortcuts import render

# Create your views here.

def gestion(request):
    return render(request, 'gestion/gestion.html')

def vehicules(request):
    return render(request, 'gestion/vehicules.html')

def disponibilites(request):
    return render(request, 'gestion/disponibilites.html')

def reservation(request):
    return render(request, 'gestion/reservation.html')