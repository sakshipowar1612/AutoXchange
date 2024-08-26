from django import forms
from .models import Location
from localflavor.in_.forms import INZipCodeField

class LocationForm(forms.ModelForm):
    address_1 = forms.CharField(required=True)
    pin_code = INZipCodeField(required=True)

    class Meta:
        model = Location
        fields = ['address_1', 'address_2', 'city', 'state', 'pin_code']
