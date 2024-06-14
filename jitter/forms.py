# import the standard Django Forms
# from built-in library
from django import forms 
from .models import Bunkform

from django.forms import ModelForm
  
# creating a form  
class BunkFormm(forms.Form): 
    your_name = forms.CharField(max_length = 200) 
    other_name = forms.CharField(max_length = 200) 
   