from django.forms import ModelForm
from django import forms
from .models import Customer


class CustomerForm(ModelForm):

	class Meta:
		model = Customer
		fields = ['first_name', 'last_name', 'user_email']
