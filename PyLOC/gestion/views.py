from django.shortcuts import render

# Create your views here.

def gestion(request):
    return render(request, 'gestion/gestion.html')

def vehicules_categories(request):
    return render(request, 'gestion/vehicules.html')

def disponibilites_categories(request):
    return render(request, 'gestion/disponibilites.html')

def reservation_categories(request):
    return render(request, 'gestion/reservation.html')