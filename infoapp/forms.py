from django import forms
from .models import PersonalData
from django.core.exceptions import ValidationError


class PersonalInfoForm(forms.ModelForm):
    surname = forms.CharField(help_text="Enter Your Fullname")
    email = forms.CharField(help_text="Enter Your Email")

    class Meta:
        model = PersonalData
	fields = ['surname', 'othername', 'email', 'phone', 'state', 'address', ]    