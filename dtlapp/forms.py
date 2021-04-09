from django.forms import ModelForm
from django import forms

from django.contrib.auth.models import User

from dtlapp.models import update

from django.contrib.auth.forms import UserCreationForm


class Userreg(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'form-control','placeholder':'Enter password1'
		}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'form-control','placeholder':'Enter confirm password'
		}))
	class Meta:
		model=User
		fields = ['username','email']
		widgets={
		'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}),
		'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email'}),
		}



class Uppro(ModelForm):
	class Meta:
		model=User
		fields=['username','first_name','last_name','email']
		widgets={
		'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username','readonly':True}),
		'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter first_name'}),
		'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter last_name'}),
		'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'enter Your email','readonly':True}),
		}

class imagepro(forms.ModelForm):
	class Meta:
		model = update
		fields = ['age','image']
		widgets={
		'age':forms.NumberInput(attrs={'class':'form-control'})
		}