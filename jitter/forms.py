# import the standard Django Forms
# from built-in library
from django import forms 
from .models import Bunkform

from django.forms import ModelForm
  
# creating a form  
class BunkFormm(forms.ModelForm): 
    # username = forms.CharField(max_length = 200) 
    # other_user = forms.CharField(max_length = 200) 
    class Meta:
        model=Bunkform
        fields = ['username', 'other_user']
