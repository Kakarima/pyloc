from django import forms
from django.contrib.auth.models import User

from .models import Customer


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