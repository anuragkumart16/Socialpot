from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.db import IntegrityError
from rest_framework.decorators import api_view
from .serializers import UsernameSerializer, EmailSerializer ,RegisterSerializers 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
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


def changepassword(request):
    pass

# api for checking username availability
@api_view(['POST'])
def checkusername(request):
    if request.method == 'POST':
        data = request.data
        serializer = UsernameSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                'status':False,
                'message':'Entered Value is not Username'
            },status.HTTP_405_METHOD_NOT_ALLOWED)
        if User.objects.filter(username=data['username']).exists():
            return Response({
                'status':False,
                'message':'Username already exists'
            },status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'status':True,
                'message':'Username is available'
            },status.HTTP_200_OK)
        

# api for checking email availability
@api_view(['POST'])
def checkemail(request):
    if request.method == 'POST':
        data = request.data
        serializer = EmailSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                'status':False,
                'message':'Entered value is not an email'
            },status.HTTP_405_METHOD_NOT_ALLOWED)
        if User.objects.filter(email=data['email']).exists():
            return Response({
                'status':False,
                'message':'Email exists, login or create a new account'
            },status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'status':True,
                'message':'Email is available'
            },status.HTTP_200_OK)



# api for creating a user
class usercreationapi(APIView):
    def post(self,request):
        data = request.data
        serializer = RegisterSerializers(data=data)

        if not serializer.is_valid():
            return Response({
                'status':False,
                'message':'Serializer.error'
            },status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response({
            'status':True,
            'message':'User created! Logging you in...'
        },status.HTTP_201_CREATED)
        


