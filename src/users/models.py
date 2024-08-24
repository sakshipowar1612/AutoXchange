import re
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from localflavor.in_.models import INStateField
from .utils import user_directory_path
# from localflavor.in_.models import INZipCodeField
# Create your models here.
class INZipCodeField(models.CharField):
    """
    A model field that validates input as an Indian ZIP code.
    Accepts formats XXXXXXX or XXX XXX, converts to XXXXXXX format.
    """
    
    default_validators = [RegexValidator(
        regex=r'^\d{6}$|^\d{3}\s?\d{3}$',
        message='Enter a zip code in the format XXXXXX or XXX XXX.'
    )]
    max_length = 6  # Indian ZIP codes are always 6 digits long

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('blank', True)
        super().__init__(*args, **kwargs)

    def clean(self, value, *args, **kwargs):
        value = super().clean(value, *args, **kwargs)
        if value in self.empty_values:
            return value
        # Convert to "XXXXXX" if "XXX XXX" given
        value = re.sub(r'^(\d{3})\s(\d{3})$', r'\1\2', value)
        if not re.match(r'^\d{6}$', value):
            raise ValidationError(self.default_error_messages['invalid'])
        return value

class Location(models.Model):
    address_1 = models.CharField(max_length=128, blank=True)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64)
    state = INStateField(default="NY")
    pin_code = INZipCodeField(max_length=6)

    def __str__(self):
        return f'Location {self.id}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #when user get deleted it's model also get deleted.
    photo = models.ImageField(upload_to=user_directory_path ,null=True)
    bio = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'