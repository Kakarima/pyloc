from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import Http404
from .forms import SearchVehicleDatesForm, SearchVehicleCategoriesForm, \
    SearchVehicleCustomerForm, SearchVehicleAgencyForm
from .models import Category, Agency, Customer, Contract, Vehicle
from .forms import UserRegistrationForm, UserEditForm, CustomerEditForm
from django.db.models import Subquery
from django.contrib.auth.models import Group


def customer_only_check(user):  # we try to check if a user is in the group 'customers'
    return user.groups.filter(name='customers').exists()


def tourism_categories(request):  # We retrieve all the vehicle categories from the table category
    # then we pass the list to the page tourisme.html
    categories = Category.objects.all()
    contracts = None
    if request.user.is_authenticated:
        contracts = Contract.objects.filter(customer_id=request.user.customer.id)
    context = {'category_list': categories,'contracts':contracts}
    return render(request, 'rental/tourisme.html', context)


def tourism_category(request, id_category):  # we retrieve the exact id vehicle category from the table category
    # then pass the id category to the page tourism_category.html
    try:
        category = Category.objects.get(id=id_category)
    except Category.DoesNotExist:
        raise Http404
    contracts = None
    if request.user.is_authenticated:
        contracts = Contract.objects.filter(customer_id=request.user.customer.id)
    context = {'category': category,'contracts':contracts}
    return render(request, 'rental/tourism_category.html', context)


def services_categories(request):  # we render the page services.html
    contracts = None
    if request.user.is_authenticated:
        contracts = Contract.objects.filter(customer_id=request.user.customer.id)
    return render(request, 'rental/services.html', {'contracts': contracts})


def agences(request):  # We retrieve all the agencies from the table agency
    # then we pass the list to the page agences.html
    toutesLesAgences = Agency.objects.all()
    contracts = None
    if request.user.is_authenticated:
        contracts = Contract.objects.filter(customer_id=request.user.customer.id)
    return render(request, 'rental/agences.html', {'agences': toutesLesAgences, 'contracts': contracts})


def agence(request, id_agency):  # we retrieve the exact id agency from the table agency
    # then pass the id agency to the page agency.html
    try:
        lAgence = Agency.objects.get(id=id_agency)
    except Agency.DoesNotExist:
        raise Http404
    contracts = None
    if request.user.is_authenticated:
        contracts = Contract.objects.filter(customer_id=request.user.customer.id)

    return render(request, 'rental/agence.html', {'agency': lAgence,'contracts':contracts})


def entreprise_categories(request):
    contracts=None
    if request.user.is_authenticated:
        contracts = Contract.objects.filter(customer_id=request.user.customer.id)
    return render(request, 'rental/entreprise.html', {'contracts': contracts})


def contact_categories(request):
    contracts = None
    if request.user.is_authenticated:
        contracts = Contract.objects.filter(customer_id=request.user.customer.id)
    return render(request, 'rental/contact.html', {'contracts': contracts})


def conseils(request):
    contracts = None
    if request.user.is_authenticated:
        contracts = Contract.objects.filter(customer_id=request.user.customer.id)
    return render(request, 'rental/conseils.html', {'contracts': contracts})


def conditions(request):
    contracts = None
    if request.user.is_authenticated:
        contracts = Contract.objects.filter(customer_id=request.user.customer.id)
    return render(request, 'rental/conditions.html', {'contracts': contracts})


def confidentialite(request):
    contracts = None
    if request.user.is_authenticated:
        contracts = Contract.objects.filter(customer_id=request.user.customer.id)
    return render(request, 'rental/confidentialite.html', {'contracts': contracts})


def partenaires(request):
    contracts = None
    if request.user.is_authenticated:
        contracts = Contract.objects.filter(customer_id=request.user.customer.id)
    return render(request, 'rental/partenaires.html', {'contracts': contracts})


def register(request):
    next_page = request.GET.get('next', '')  # we retrieve the information sent by POST
    # after the user has finished to fill the form
    if request.method == 'POST':  # if the method is POST
        user_form = UserRegistrationForm(request.POST)  # then we need to create the user registration form
        customer_form = CustomerEditForm(request.POST, files=request.FILES)  # and we need to create the customer form
        if user_form.is_valid() and customer_form.is_valid():  # if the 2 forms are valid
            user = user_form.save(commit=False)  # then we save the user form
            user.set_password(user_form.cleaned_data['password'])  # we retrieve the password
            user.save()  # we save the user and the password
            customer_group = Group.objects.get(name='customers')  # we retrieve all the 'customers'
            # from the table auth_group
            customer_group.user_set.add(user)  # we add the user to the group 'customer'
            # so the user is saved in the table auth_user_groups
            customer = customer_form.save(commit=False)  # we save the customer form
            customer.user = user  # we linked the customer to the auth_user table because customer is the fk of user
            customer.save()  # we save the customer and all the information sent
            return render(request, 'registration/registration_done.html',
                          {'new_user': user, 'next': next_page})  # we render the page registration_done and
            # we redirect the customer to the front page rental
        else:
            messages.error(request, "Error")  # if the form is not valid then we render an error message and we send
            # the user back to the page registration.html so he/she can register again
            return render(request, 'registration/registration.html',
                          {'user_form': user_form, 'customer_form': customer_form, 'next': next_page})
    else:
        user_form = UserRegistrationForm(
            initial={'username': request.GET.get('username'), 'email': request.GET.get('email')})  # we show
        # the user registration form so the user can fill the data
        customer_form = CustomerEditForm(
            initial={'phone': request.GET.get('phone')})  # same for the customer
        return render(request, 'registration/registration.html',
                      {'user_form': user_form, 'customer_form': customer_form, 'next': next_page})


@login_required(login_url='rental:login')  # the login is required to access to the edit form
@user_passes_test(customer_only_check, login_url='rental:forbidden')  # only the customer can edit the form
def edit_customer(request):
    if request.method == 'POST':  # if the method is POST (we submit the form)
        user_form = UserEditForm(request.POST, instance=request.user)  # we retrieve the fields from the UserEditForm
        customer_form = CustomerEditForm(request.POST, instance=request.user.customer, files=request.FILES)
        # same for the customer
        if user_form.is_valid() and customer_form.is_valid():  # if all the forms are valid then we save everything
            user_form.save()
            customer_form.save()
            next_page = request.GET.get('next')
            return redirect(next_page)
    else:  # we show the UserEditForm
        user_form = UserEditForm(instance=request.user)
        customer_form = CustomerEditForm(instance=request.user.customer)
        next_page = request.GET.get('next')
        return render(request, 'rental/edit_customer.html',
                      {'user_form': user_form, 'customer_form': customer_form, 'next': next_page})


def recap_contracts(request):
    if request.user.is_authenticated is True:  # if the user is authenticated
        try:
            contract = Contract.objects.filter(customer_id=request.user.customer.id)  # then we retrieve all
            # the contract that the user has
        except Contract.DoesNotExist:  # if there is no contract, then contract = 0
            contract = None

        if contract is not None:  # if there is a contract, then we retrieve the contract
            # agency, the vehicle, the start_date, and so on
            context = {'contracts': contract}
            return render(request, 'rental/register-contract.html', context)  # we render the page
            # to show the information
    else:

        return render(request, 'rental/remerciements.html')


def remerciements(request):
    contracts = None
    if request.user.is_authenticated:
        contracts = Contract.objects.filter(customer_id=request.user.customer.id)
    return render(request, 'rental/remerciements.html', {'contracts': contracts})


def home(request):
    """ User home page"""

    post = request.POST or None  # we verify that the form is well-filled
    searchvehicledatesform = SearchVehicleDatesForm(post, prefix='search_dates')  # we create the
    # search vehicle date form
    searchvehiclecategoriesform = SearchVehicleCategoriesForm(post, prefix='search_vehicle_category')
    # same for category
    searchvehicleagencyform = SearchVehicleAgencyForm(post, prefix='search_agency')  # same for agency
    if post is None and request.user.is_authenticated:  # if the user is authenticated
        searchvehiclecustomerform = SearchVehicleCustomerForm(prefix='search_customer', initial={
            'name': request.user.username,
            'email': request.user.email,
            'phone': request.user.customer.phone})  # we prefilled the name, email, and phone
        # of the user in the search form
    else:
        searchvehiclecustomerform = SearchVehicleCustomerForm(post, prefix='search_customer')  # we display
        # the search vehicle form

    display_form = True
    display_booking_date_start = display_booking_date_end = \
        booking_date_start = booking_date_end = vehicles = agency = category = customer = already_contracted = None
    # all the fields = 0

    # if all the forms are valid -> we verify from the search
    # that the vehicle is available (with the criteria of agency, date and sample)
    if searchvehiclecategoriesform.is_valid() \
            and searchvehicledatesform.is_valid() \
            and searchvehiclecustomerform.is_valid() \
            and searchvehicleagencyform.is_valid():

        category_id = searchvehiclecategoriesform.cleaned_data.get('sample')  # we retrieve the category
        category = Category.objects.get(id=category_id)
        print('category = ' + str(category))

        # we retrieve the agency
        agency_id = searchvehicleagencyform.cleaned_data.get('name')
        agency = Agency.objects.get(id=agency_id)

        # we retrieve the booking date start
        display_booking_date_start = searchvehicledatesform.cleaned_data.get('date_start')
        # we retrieve the booking date end
        display_booking_date_end = searchvehicledatesform.cleaned_data.get('date_end')

        booking_date_start = post.get('search_dates-date_start')  # we retrieve the booking date start
        booking_date_end = post.get('search_dates-date_end')  # we retrieve the booking date end

        # we retrieve the name, email and phone of the customer
        customer_name = searchvehiclecustomerform.cleaned_data.get('name')
        customer_email = searchvehiclecustomerform.cleaned_data.get('email')
        customer_phone = searchvehiclecustomerform.cleaned_data.get('phone')
        customer = {'name': customer_name, 'email': customer_email, 'phone': customer_phone}

        # we search for the agency selected, booking date start and end selected if there is a contract
        already_contracted = Contract.objects.all() \
            .filter(agence=agency) \
            .filter(date_end__gt=booking_date_start) \
            .filter(date_start__lt=booking_date_end)

        # we retrieve all the vehicles available that match with the agency, and the sample requested
        # we exclude all the "already_contracted"
        vehicles = Vehicle.objects.all() \
            .filter(active=True) \
            .filter(category=category) \
            .filter(agence=agency) \
            .exclude(id__in=Subquery(already_contracted.values('vehicle')))
        print('query = ' + str(vehicles.query))
        for vehicle in vehicles:
            print('vehicle = ' + str(vehicle))

        display_form = False

    contracts = None
    if request.user.is_authenticated:
        contracts = Contract.objects.filter(customer_id=request.user.customer.id)

    return render(request, 'rental/pyloc.html', {'searchvehicledatesform': searchvehicledatesform,
                                                 'searchvehiclecategoriesform': searchvehiclecategoriesform,
                                                 'searchvehicleagencyform': searchvehicleagencyform,
                                                 'searchvehiclecustomerform': searchvehiclecustomerform,
                                                 'display_form': display_form,
                                                 'display_results': not display_form,
                                                 'vehicles': vehicles,
                                                 'already_contracted': already_contracted,
                                                 'booking_date_start': booking_date_start,
                                                 'booking_date_end': booking_date_end,
                                                 'display_booking_date_start': display_booking_date_start,
                                                 'display_booking_date_end': display_booking_date_end,
                                                 'agency': agency,
                                                 'category': category,
                                                 'customer': customer,
                                                 'contracts': contracts})


@login_required(login_url='rental:login')  # in order to register a contract, the user should be connected
@user_passes_test(customer_only_check, login_url='rental:forbidden')  # and it should be a customer
# because a manager can't rent a car
def register_contract(request):
    from .forms import RentVehicleAgencyDatesForm  # it import the forms from forms.py
    post = request.POST or None

    rentvehicleagencydatesform = RentVehicleAgencyDatesForm(post)  # we affect the form

    contract = agency = vehicle = None
    customer = None

    if rentvehicleagencydatesform.is_valid():  # if the form is valid
        customer = Customer.objects.all().get(id=request.user.customer.id)  # we retrieve the id
        # customer from the table customer

        # we retrieve the agency
        agency_id = rentvehicleagencydatesform.cleaned_data.get('agency_id')
        agency = Agency.objects.get(id=agency_id)

        # same for the vehicle
        vehicle_id = rentvehicleagencydatesform.cleaned_data.get('vehicle_id')
        vehicle = Vehicle.objects.all().get(id=vehicle_id, active=True)

        booking_date_start = rentvehicleagencydatesform.cleaned_data.get('booking_date_start')
        # we retrieve the booking date start
        booking_date_end = rentvehicleagencydatesform.cleaned_data.get('booking_date_end')
        # same for the date end

        # we create its contract
        contract = Contract(vehicle=vehicle, customer=customer, agence=agency, date_start=booking_date_start,
                            date_end=booking_date_end, scheduled_date_end=booking_date_end)
        contract.save()  # we save the contract

    return render(request, 'rental/reservation.html', {'contract': contract})


