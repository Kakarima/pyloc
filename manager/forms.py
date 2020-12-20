from django import forms
from rental.models import Vehicle, Agency, Category

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('brand', 'manufacturer_name', 'registration', 'engine_serial_number')

    agencies = forms.ModelMultipleChoiceField(queryset=Agency.objects.all())
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

