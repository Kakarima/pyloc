from django.shortcuts import render
from .models import Category, Agency


def home(request):
    agencies = Agency.objects.all
    context = {'agency_list': agencies}
    return render(request, 'rental/pyloc.html', context)


def tourism_categories(request):
    categories = Category.objects.all()
    context = {'category_list': categories}
    return render(request, 'rental/tourisme.html', context)


def tourism_category(request, id):
    category = Category.objects.get(id=id)
    return render(request, 'rental/tourism_category.html', {'category': category})


def utilitaires_categories(request):
    return render(request, 'rental/utilitaires.html')


def services_categories(request):
    return render(request, 'rental/services.html')


def agences_categories(request):
    return render(request, 'rental/agences.html')


def entreprise_categories(request):
    return render(request, 'rental/entreprise.html')


def todo_categories(request):
    return render(request, 'rental/todo.html')
