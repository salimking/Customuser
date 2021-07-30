from django import  forms
from django.contrib.auth.forms import UserCreationForm
from django.core.checks import messages
from django.db.models import fields
from django.forms import models, widgets
from .models import Customer,Adminuser

class Customerf(UserCreationForm):
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),label='username')
  
   


    class Meta(UserCreationForm):
        model=Customer
        fields=['username']      

        

class Admin(UserCreationForm):
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),label='username')
  
   


    class Meta(UserCreationForm):
        model=Adminuser
        fields=['username']      
    