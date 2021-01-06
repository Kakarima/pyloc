from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Category, Agency, Customer
from datetime import datetime


class UserRegistrationForm(forms.ModelForm):  # We create the User registration form
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Répéter le mot de passe', widget=forms.PasswordInput)

    class Meta:  # the form is generated by Django so we need to tell them
        # in which table we need to retrieve the information
        model = User  # we take the information from the model user
        fields = ('username', 'last_name', 'first_name', 'email')  # we display the fields

    def clean_password2(self):  # we retrieve the password and we verify if the password matches the second one
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Les mots de passe ne correspondent pas')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        labels = {
            "first_name": "Prénom",
            "last_name": "Nom",
            "email": "E-mail"
        }
        fields = ('first_name', 'last_name', 'email')


class CustomerEditForm(forms.ModelForm):
    user = forms.CharField(label='', widget=forms.HiddenInput, required=False)

    class Meta:
        model = Customer
        fields = ('licence_scan', 'licence_number', 'address', 'postal_code', 'city', 'phone', 'age', 'user')
        labels = {
            "licence_scan": "Scan Permis de Conduire",
            "licence_number": "Numéro de Permis",
            "address": "Adresse",
            "postal_code": "Code Postal",
            "city": "Ville",
            "phone": "Téléphone",
            "age": "Âge",
            "user": "Utilisateur"
        }


def get_VehiclesCategories():  # we retrieve the couple id and sample from the table category and we display it
    return tuple([(None, '')] + list(Category.objects.values_list('id', 'sample').distinct()))


def get_agencies():  # we retrieve the couple id and name from the table agency and we display it
    return tuple([(None, '')] + list(Agency.objects.values_list('id', 'name').distinct()))


class SearchVehicleAgencyForm(ModelForm):
    class Meta:
        model = Agency
        fields = ['name']
        labels = {
            "name": "Agence"
        }
        widgets = {'name': forms.Select(choices=get_agencies())}  # we display the combo box of agencies


class SearchVehicleCategoriesForm(ModelForm):
    class Meta:
        model = Category
        fields = ['label']
        labels = {
            "label": "Catégorie"
        }
        widgets = {'label': forms.Select(choices=get_VehiclesCategories())}


class DateTimeLocalInput(forms.DateTimeInput):  # it is used in the class below
    input_type = 'datetime-local'  # we use the local date


class SearchVehicleDatesForm(forms.Form):
    now = datetime.now()  # it shows the time now
    date_input_formats = ['%Y-%m-%dT%H:%M', '%d/%m/%Y %H:%M', '%m/%d/%y']

    date_start = forms.DateTimeField(label='Date de depart',
                                     input_formats=['%Y-%m-%dT%H:%M'],
                                     widget=forms.DateTimeInput(attrs={'type': 'datetime-local'},
                                                                format='%Y-%m-%dT%H:%M'),
                                     required=True
                                     )

    date_end = forms.DateTimeField(label='Date de fin',
                                   widget=DateTimeLocalInput(),
                                   required=True,
                                   input_formats=date_input_formats)

    def clean_date_end(self):
        date_end = self.cleaned_data['date_end']
        date_start = self.cleaned_data['date_start']
        now = datetime.now()

        if date_end and date_start and date_end < date_start:
            raise forms.ValidationError('La date de fin ne peut pas être inférieure à la date début')


class SearchVehicleCustomerForm(forms.Form):  # we show the form of customer when we do the search
    name = forms.CharField(label='Nom', required=True, max_length=100)
    phone = forms.CharField(label='Téléphone', required=True, max_length=255)
    email = forms.EmailField(label="E-Mail", required=True, max_length=255)


class RentVehicleAgencyDatesForm(forms.Form):  # we show the form of the rentvehicle when we do the rent
    date_input_formats = ['%Y-%m-%dT%H:%M',
                          '%d/%m/%Y %H:%M',
                          '%m/%d/%y']
    agency_id = forms.IntegerField(required=True)
    vehicle_id = forms.IntegerField(required=True)
    booking_date_start = forms.DateTimeField(input_formats=date_input_formats, required=True)
    booking_date_end = forms.DateTimeField(input_formats=date_input_formats, required=True)
    customer_name = forms.CharField(required=True)
    customer_email = forms.EmailField(required=True)
    customer_phone = forms.CharField(required=True)
