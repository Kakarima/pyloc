from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Category, Agency
from rental.forms import UserRegistrationForm, UserEditForm, CustomerEditForm

def home(request):
    agencies = Agency.objects.all
    context = {'agency_list': agencies}
    return render(request, 'rental/pyloc.html', context)

def tourism_categories(request):
    categories = Category.objects.all()
    context = {'category_list': categories}
    return render(request, 'rental/tourisme.html', context)

def tourism_category(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        raise Http404
    return render(request, 'rental/tourism_category.html', {'category': category})

def services_categories(request):
    return render(request, 'rental/services.html')

def agences(request):
    toutesLesAgences = Agency.objects.all()
    return render(request, 'rental/agences.html', {'agences': toutesLesAgences})

def agence(request, id_agency):
    try:
        category = Category.objects.get(id=id_agency)
    except Category.DoesNotExist:
        raise Http404
    return render(request, 'rental/agence.html', {'agence': lAgence})

def entreprise_categories(request):
    return render(request, 'rental/entreprise.html')

def contact_categories(request):
    return render(request, 'rental/contact.html')

def conseils(request):
    return render(request, 'rental/conseils.html')

def conditions(request) :
    return render(request, 'rental/conditions.html')

def confidentialite(request) :
    return render(request, 'rental/confidentialite.html')

def partenaires(request) :
    return render(request, 'rental/partenaires.html')

def register(request):
    next_page = request.GET.get('next', '')
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        customer_form = CustomerEditForm(request.POST, files=request.FILES)
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()
            return render(request, 'registration/registration_done.html',
                          {'new_user': user, 'next': next_page})
        else:
            messages.error(request, "Error")
            return render(request, 'registration/registration.html',
                          {'user_form': user_form, 'customer_form': customer_form , 'next': next_page})
    else:
        user_form = UserRegistrationForm()
        customer_form = CustomerEditForm()
        return render(request, 'registration/registration.html',
                      {'user_form': user_form, 'customer_form': customer_form, 'next': next_page})


@login_required
def edit_customer(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        customer_form = CustomerEditForm(request.POST, instance=request.user.customer, files=request.FILES)
        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()
            customer_form.save()
            next_page = request.GET.get('next')
            return redirect(next_page)
    else:
        user_form = UserEditForm(instance=request.user)
        customer_form = CustomerEditForm(instance=request.user.customer)
        next_page = request.GET.get('next')
        return render(request, 'rental/edit_customer.html',
                      {'user_form': user_form, 'customer_form': customer_form, 'next': next_page})