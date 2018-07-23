from django import forms
from .models import PersonalData
from django.core.exceptions import ValidationError


class PersonalInfoForm(forms.ModelForm):
	fullname = forms.CharField(help_text="Enter Your Fullname")
	email = forms.CharField(help_text="Enter Your Email")

	class Meta:
		model = PersonalData
		fields = ['fullname', 'email']

	def clean(self):
		cleaned_data = super(PersonalInfoForm, self).clean()
		fullname = cleaned_data.get('fullname')
		email = cleaned_data.get('email')
		if not fullname and not email:
			raise forms.ValidationError("Please, Enter Your Details before Submission")
