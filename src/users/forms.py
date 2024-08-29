from django import forms
from .models import Location, Profile
from localflavor.in_.forms import INZipCodeField
from .models import User

class UserForm(forms.ModelForm):

    class Meta:
        #we can view it wouldn't able to change it.
        username = forms.CharField(disabled=True)
        model = User
        fields = ('username', 'first_name', 'last_name')

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('photo', 'bio', 'phone_number')

class LocationForm(forms.ModelForm):
    address_1 = forms.CharField(required=True)
    pin_code = INZipCodeField(required=True)

    class Meta:
        model = Location
        fields = ['address_1', 'address_2', 'city', 'state', 'pin_code']
