from django import forms
from django.db.models import Count
from .models import Image
from django.contrib.auth import get_user_model 
from django.contrib.auth.models import 	User
from django.forms import ValidationError
#from django.core.validators import MaxValueValidator

class ImageUploadForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ('image',)


class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ('username','email')
	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password']!=cd['password2']:
			raise forms.validationError("passwords don't match")
		return cd['password2']