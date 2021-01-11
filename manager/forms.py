from django import forms
from rental.models import Vehicle, Agency, Category


# Create a model form which is linked to model vehicle and we retrieve the agencies and the categories
# to form a combo box where we can choose the different agencies and vehicles


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('brand', 'manufacturer_name', 'registration', 'engine_serial_number')
        labels = {
            "brand": "Marque",
            "manufacturer_name": "Fabricant",
            "registration": "Immatriculation",
            "engine_serial_number": "Numéro de série"
        }

    agencies = forms.ModelMultipleChoiceField(label='Agence', queryset=Agency.objects.all())
    categories = forms.ModelMultipleChoiceField(label='Catégorie', queryset=Category.objects.all())
