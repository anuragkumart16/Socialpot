from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.

def home(request):
    return redirect('signinuser')
    

def signinview(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username =username ,password = password)
        if user is not None:
            login(request,user)
            messages.add_message(request,messages.INFO,'Login Sucessful !')
            return redirect ('clipboard')
        else:
            messages.add_message(request,messages.INFO,'invalid Credentials !')
            return render(request,'signin.html')
    else: 
        return render(request,'signin.html')

def signupview(request):
    if request.method == "POST":
        username= request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try :
            user = User.objects.create_user(username,email,password)
            user.save()
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.add_message(request,messages.INFO,'Account Sucessfully Created !')
                return redirect ('clipboard')
        except IntegrityError :
            messages.add_message(request,messages.ERROR,'Username already taken !')
            return redirect('signupuser')

        user.save()
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.add_message(request,messages.INFO,'Account Sucessfully Created !')
            return redirect ('clipboard')
    else:
        return render(request,'signup.html')
        

def logoutview(request):
    logout(request)
    messages.add_message(request,messages.INFO,' logout Successful !')
    return redirect('signinuser')


# views.py

from django.http import JsonResponse

def check_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)
