from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import SearchVehicleDatesForm, SearchVehicleCategoriesForm, SearchVehicleCustomerForm, SearchVehicleAgencyForm, RentVehicleAgencyDatesForm
from .models import Category, Agency, Customer, Contract, Vehicle
from .forms import UserRegistrationForm, UserEditForm, CustomerEditForm
from django.db.models import Subquery

#def home(request):
    #agencies = Agency.objects.all
    #context = {'agency_list': agencies}
    #return render(request, 'rental/pyloc.html', context)

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
        lAgence = Agency.objects.get(id=id_agency)
    except Agency.DoesNotExist:
        raise Http404
    return render(request, 'rental/agence.html', {'agency': lAgence})

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


def home(request):
    """ User home page"""

    # formulaire découpé en 4 parties

    post = request.POST or None
    print(post)
    searchvehicledatesform = SearchVehicleDatesForm(post, prefix='search_dates')
    searchvehiclecategoriesform = SearchVehicleCategoriesForm(post, prefix='search_vehicle_category')
    searchvehicleagencyform = SearchVehicleAgencyForm(post, prefix='search_agency')
    searchvehiclecustomerform = SearchVehicleCustomerForm(post, prefix='search_customer')

    display_form = True
    display_results = False
    display_booking_date_start = display_booking_date_end = booking_date_start = booking_date_end = vehicles = agency = category = customer = None
    #vehicles_list = Vehicle.objects.filter(brand='Renault').order_by('-date_immatriculation')

    # Si l'ensemble du formulaire est valide
    if searchvehiclecategoriesform.is_valid() \
            and searchvehicledatesform.is_valid() \
            and searchvehiclecustomerform.is_valid() \
            and searchvehicleagencyform.is_valid():

        # On vérifie la disponibilité de véhicules demandés pour les critères indiqués
        # Agence, dates, modèle
        # récupération du modèle

        category_id = searchvehiclecategoriesform.cleaned_data.get('label')
        category = Category.objects.get(id=category_id)
        print('category = ' + str(category))

        # récupération de l'agence
        agency_id = searchvehicleagencyform.cleaned_data.get('name')
        agency = Agency.objects.get(id=agency_id)

        # Liste des contrats en cours pour l'agence considérée
        display_booking_date_start = searchvehicledatesform.cleaned_data.get('date_start')  # on récupère la date de début souhaitée pour la location
        display_booking_date_end = searchvehicledatesform.cleaned_data.get('date_end')  # on récupère la date de début souhaitée pour la location

        booking_date_start = post.get('search_dates-date_start')
        booking_date_end = post.get('search_dates-date_end')

        # variable customer
        customer_name = searchvehiclecustomerform.cleaned_data.get('name')
        customer_email = searchvehiclecustomerform.cleaned_data.get('email')
        customer_phone = searchvehiclecustomerform.cleaned_data.get('phone')
        customer = Customer(name=customer_name, email=customer_email, phone=customer_phone)

        #liste des contrats déjà conclus aux dates indiquées (dont la date de fin est postérieure à la date de début de la location recherchée) pour l'agence souhaitée
        already_contracted = Contract.objects.all() \
            .filter(agence=agency) \
            .filter(date_end__gt=booking_date_start)



        # Liste des véhicules disponible correspondant à l'agence et au modèle et étant actifs et dont on exclut ceux concernés par les contrats déjà conclus (requête "already_contracted" ci dessus)
        vehicles = Vehicle.objects.all() \
            .filter(active=True) \
            .filter(category=category) \
            .filter(agence=agency) \
            .exclude(id__in=Subquery(already_contracted.values('vehicle')))
        print('query = ' + str(vehicles.query))
        for vehicle in vehicles:
            print('vehicle = ' + str(vehicle))

        display_form = False
        display_results = True

    return render(request, 'rental/pyloc.html',{'searchvehicledatesform' : searchvehicledatesform,
                                                'searchvehiclecategoriesform' : searchvehiclecategoriesform,
                                                'searchvehicleagencyform' : searchvehicleagencyform,
                                                'searchvehiclecustomerform' : searchvehiclecustomerform,
                                                'display_form' : display_form,
                                                'display_results':  display_results,
                                                'vehicles' : vehicles,
                                                'booking_date_start': booking_date_start,
                                                'booking_date_end': booking_date_end,
                                                'display_booking_date_start':display_booking_date_start,
                                                'display_booking_date_end': display_booking_date_end,
                                                'agency' : agency,
                                                'category' : category,
                                                'customer': customer})

def register_contract(request):

    from .forms import RentVehicleAgencyDatesForm
    post = request.POST or None

    # formulaire custom pour la validation des données


    rentvehicleagencydatesform = RentVehicleAgencyDatesForm(post)

    print('rentvehicleagencydatesform')
    print(rentvehicleagencydatesform.is_valid())
    print(rentvehicleagencydatesform.errors)

    if (request.user == None or request.user.is_authenticated==False):
        return redirect('/rental/registration')


    elif rentvehicleagencydatesform.is_valid():
        contract = customer = ctr_error = agency = vehicle = None
        # récupération de l'agence
        agency_id = rentvehicleagencydatesform.cleaned_data.get('agency_id')
        agency = Agency.objects.get(id=agency_id)

        # récupération du véhicule
        vehicle_id = rentvehicleagencydatesform.cleaned_data.get('vehicle_id')
        vehicle = Vehicle.objects.all().get(id=vehicle_id, active=True)
        print('vehicle = ' + str(vehicle))

        booking_date_start = rentvehicleagencydatesform.cleaned_data.get('booking_date_start')  # on récupère la date de début souhaitée pour la location
        booking_date_end = rentvehicleagencydatesform.cleaned_data.get('booking_date_end')  # on récupère la date de début souhaitée pour la location

        #On vérifie qu'aucun contrat n'est en cours
        already_contracted = Contract.objects.all().filter(agence=agency).filter(vehicle=vehicle).filter(date_end__gt=booking_date_start)
        print('already_contracted = ' + str(already_contracted))

        #erreurs
        error = ''
        if already_contracted.count() > 0:
            ctr_error = 'Impossible de réserver à partir des choix transmis. Le véhicule demandé n\'est plus disponible.'
        else:
            # création d'un compte client
            ctr_error = ''

            # variable customer
            customer_name = rentvehicleagencydatesform.cleaned_data.get('customer_name')
            customer_email = rentvehicleagencydatesform.cleaned_data.get('customer_email')
            customer_phone = rentvehicleagencydatesform.cleaned_data.get('customer_phone')
            customer = Customer(name=customer_name, email=customer_email, phone=customer_phone)
            customer.save()


            contract = Contract(vehicle=vehicle, customer=customer, agence=agency, date_start=booking_date_start, date_end=booking_date_end,scheduled_date_end=booking_date_end)
            contract.save()


        #context
    context = {
            'ctr_error': ctr_error,
            'agency': agency,
            'vehicle': vehicle,
            'booking_date_start': booking_date_start,
            'booking_date_end': booking_date_end,
            'rentvehicleagencydatesform': rentvehicleagencydatesform,
            'customer': customer,
            'contract': contract,

        }
    print('kerkrkkrk')
    print(ctr_error)

    return render(request, 'rental/register-contract.html', context)