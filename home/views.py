from django.contrib.auth import forms
from django.http.response import HttpResponse
from django.shortcuts import render
from .form import Customerf,Admin
from django.contrib import messages
from .models import CustomUser,Customer,Adminuser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login

# Create your views here.
def creg(request):
    form=Customerf()
    if request.method=='POST':
        form=Customerf(request.POST)
        if form.is_valid():
            
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            
            
            

            user=CustomUser.objects.create_user(username=username,password=password,u_t=2)
            user.save()
            
            messages.success(request,"Thank ur 4 registration")



    context={
        'form':form
    }
    return render(request,'Customer_Registration.html',context)
    

      

def areg(request):
    form=Admin()
    if request.method=='POST':
        form=Admin(request.POST)
        if form.is_valid():
            
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            
            
            

            user=CustomUser.objects.create_user(username=username,password=password,u_t=1)
            user.save()
            
            messages.success(request,"Thank ur 4 registration")



    context={
        'form':form
    }
    return render(request,'Admin_Registration.html',context)    

def log(request):
    form=AuthenticationForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            login(request,user)
            if user.u_t=="1":
                return HttpResponse('U R Admin')
            else:
                return HttpResponse('U R Customer')   
    con={
        'form':form
    }
    return render(request,'cus.html',con)
