from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import SearchVehicleDatesForm, SearchVehicleCategoriesForm, \
    SearchVehicleCustomerForm, SearchVehicleAgencyForm
from .models import Category, Agency, Customer, Contract, Vehicle, User
from .forms import UserRegistrationForm, UserEditForm, CustomerEditForm
from django.db.models import Subquery


def tourism_categories(request):
    categories = Category.objects.all()
    context = {'category_list': categories}
    return render(request, 'rental/tourisme.html', context)


def tourism_category(request, id_category):
    try:
        category = Category.objects.get(id=id_category)
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


def conditions(request):
    return render(request, 'rental/conditions.html')


def confidentialite(request):
    return render(request, 'rental/confidentialite.html')


def partenaires(request):
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
                          {'user_form': user_form, 'customer_form': customer_form, 'next': next_page})
    else:
        user_form = UserRegistrationForm(
            initial={'username': request.GET.get('username'), 'email': request.GET.get('email')})
        customer_form = CustomerEditForm(
            initial={'phone': request.GET.get('phone')})
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
    if request.GET.get("edit") is None:
        edit = False
    else:
        edit = request.GET.get("edit")
    if request.user.is_authenticated is True and not edit:
        try:
            contract = Contract.objects.all().get(customer_id=request.user.customer.id)
        except Contract.DoesNotExist:
            contract = None

        if contract is not None:
            context = {
                'ctr_error': '',
                'agency': contract.agence,
                'vehicle': contract.vehicle,
                'booking_date_start': contract.date_start,
                'booking_date_end': contract.date_end,
                'customer': contract.customer,
                'contract': contract}
            return render(request, 'rental/register-contract.html', context)



    post = request.POST or None
    searchvehicledatesform = SearchVehicleDatesForm(post, prefix='search_dates')
    searchvehiclecategoriesform = SearchVehicleCategoriesForm(post, prefix='search_vehicle_category')
    searchvehicleagencyform = SearchVehicleAgencyForm(post, prefix='search_agency')
    if post is None and request.user.is_authenticated :
        searchvehiclecustomerform = SearchVehicleCustomerForm(prefix='search_customer', initial={
            'name': request.user.username,
            'email': request.user.email,
            'phone': request.user.customer.phone})
    else :
        searchvehiclecustomerform = SearchVehicleCustomerForm(post, prefix='search_customer')

    display_form = True
    display_results = False
    display_booking_date_start = display_booking_date_end = \
        booking_date_start = booking_date_end = vehicles = agency = category = customer = already_contracted = None

    # vehicles_list = Vehicle.objects.filter(brand='Renault').order_by('-date_immatriculation')

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
        display_booking_date_start = searchvehicledatesform.cleaned_data.get('date_start')
        # on récupère la date de début souhaitée pour la location
        display_booking_date_end = searchvehicledatesform.cleaned_data.get('date_end')
        # on récupère la date de début souhaitée pour la location

        booking_date_start = post.get('search_dates-date_start')
        booking_date_end = post.get('search_dates-date_end')

        # variable customer
        customer_name = searchvehiclecustomerform.cleaned_data.get('name')
        customer_email = searchvehiclecustomerform.cleaned_data.get('email')
        customer_phone = searchvehiclecustomerform.cleaned_data.get('phone')
        customer = Customer(name=customer_name, email=customer_email, phone=customer_phone)

        # liste des contrats déjà conclus aux dates indiquées
        # (dont la date de fin est postérieure à la date de début de la location recherchée) pour l'agence souhaitée
        already_contracted = Contract.objects.all() \
            .filter(agence=agency) \
            .filter(date_end__gt=booking_date_start) \
            .filter(date_start__lt=booking_date_end)

        # Liste des véhicules disponible correspondant à l'agence et au modèle et étant actifs et
        # dont on exclut ceux concernés par les contrats déjà conclus (requête "already_contracted" ci dessus)
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

    return render(request, 'rental/pyloc.html', {'searchvehicledatesform': searchvehicledatesform,
                                                 'searchvehiclecategoriesform': searchvehiclecategoriesform,
                                                 'searchvehicleagencyform': searchvehicleagencyform,
                                                 'searchvehiclecustomerform': searchvehiclecustomerform,
                                                 'display_form': display_form,
                                                 'display_results':  display_results,
                                                 'vehicles': vehicles,
                                                 'already_contracted': already_contracted,
                                                 'booking_date_start': booking_date_start,
                                                 'booking_date_end': booking_date_end,
                                                 'display_booking_date_start': display_booking_date_start,
                                                 'display_booking_date_end': display_booking_date_end,
                                                 'agency': agency,
                                                 'category': category,
                                                 'customer': customer})


def register_contract(request):

    from .forms import RentVehicleAgencyDatesForm
    post = request.POST or None

    # formulaire custom pour la validation des données

    rentvehicleagencydatesform = RentVehicleAgencyDatesForm(post)

    print('rentvehicleagencydatesform')
    print(rentvehicleagencydatesform.is_valid())
    print(rentvehicleagencydatesform.errors)

    customer = None
    user_exist = False
    if request.user is None or not request.user.is_authenticated:
        if post is not None:

            auth_user = User.objects.all() \
                .filter(username=rentvehicleagencydatesform.cleaned_data.get('customer_name')) \
                .filter(email=rentvehicleagencydatesform.cleaned_data.get('customer_email'))

            customers = Customer.objects.all() \
                .filter(phone=rentvehicleagencydatesform.cleaned_data.get('customer_phone')) \
                .filter(user_id__in=Subquery(auth_user.values('id')))

            if customers.count() > 0:
                customer = customers.first()
                user_exist = True
            else:
                return redirect('/rental/registration?username=' +
                                str(rentvehicleagencydatesform.cleaned_data.get('customer_name')) +
                                '&email=' +
                                str(rentvehicleagencydatesform.cleaned_data.get('customer_email')) +
                                '&phone=' +
                                str(rentvehicleagencydatesform.cleaned_data.get('customer_phone')) +
                                '&next=/rental')

    if rentvehicleagencydatesform.is_valid():
        contract = ctr_error = agency = vehicle = None
        if customer is None:
            if request.user.is_authenticated:
                customer = Customer.objects.all().get(id=request.user.customer.id)
            else:
                customer = None

        # récupération de l'agence
        agency_id = rentvehicleagencydatesform.cleaned_data.get('agency_id')
        agency = Agency.objects.get(id=agency_id)

        # récupération du véhicule
        vehicle_id = rentvehicleagencydatesform.cleaned_data.get('vehicle_id')
        vehicle = Vehicle.objects.all().get(id=vehicle_id, active=True)
        print('vehicle = ' + str(vehicle))

        booking_date_start = rentvehicleagencydatesform.cleaned_data.get('booking_date_start')
        # on récupère la date de début souhaitée pour la location
        booking_date_end = rentvehicleagencydatesform.cleaned_data.get('booking_date_end')
        # on récupère la date de début souhaitée pour la location

        # création d'un compte client
        ctr_error = ''

        # variable customer
        if customer is None:
            customer_name = rentvehicleagencydatesform.cleaned_data.get('customer_name')
            customer_email = rentvehicleagencydatesform.cleaned_data.get('customer_email')
            customer_phone = rentvehicleagencydatesform.cleaned_data.get('customer_phone')
            customer = Customer(name=customer_name, email=customer_email, phone=customer_phone)
            customer.save()


        contract = Contract(vehicle=vehicle, customer=customer, agence=agency, date_start=booking_date_start,
                            date_end=booking_date_end, scheduled_date_end=booking_date_end)
        contract.save()

    if user_exist:
        return redirect('/rental/login?next=/rental')

    # context
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
    return render(request, 'rental/register-contract.html', context)
