from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Category, Agency, Customer
from datetime import datetime


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Répéter le mot de passe', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Les mots de passe ne correspondent pas')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class CustomerEditForm(forms.ModelForm):
    user = forms.CharField(label='', widget=forms.HiddenInput, required=False)

    class Meta:
        model = Customer
        fields = ('licence_scan', 'licence_number', 'address', 'postal_code', 'city', 'phone', 'age', 'user')

        
def get_VehiclesCategories():
    return tuple([(None, '')] + list(Category.objects.values_list('id', 'label').distinct()))
 main


def get_agencies():
    return tuple([(None, '')] + list(Agency.objects.values_list('id', 'name').distinct()))


class SearchVehicleAgencyForm(ModelForm):
    class Meta:
        model = Agency
        fields = ['name']
        widgets = {'name': forms.Select(choices=get_agencies())}


class SearchVehicleCategoriesForm(ModelForm):
            class Meta:
                model = Category
                fields = ['label']
                widgets = {'label': forms.Select(choices=get_VehiclesCategories())}


class DateTimeLocalInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class SearchVehicleDatesForm(forms.Form):
    now = datetime.now()
    date_input_formats = ['%Y-%m-%dT%H:%M', '%d/%m/%Y %H:%M', '%m/%d/%y']

    date_start = forms.DateTimeField(label='Date de depart',
                                     input_formats=['%Y-%m-%dT%H:%M'],
                                     widget=forms.DateTimeInput(attrs={'type': 'datetime-local'},
                                                                format='%Y-%m-%dT%H:%M'),
                                     required=True
                                     )

    date_end = forms.DateTimeField(widget=DateTimeLocalInput(),
                                   required=True,
                                   input_formats=date_input_formats)


class SearchVehicleCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email']


class RentVehicleAgencyDatesForm(forms.Form):
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
