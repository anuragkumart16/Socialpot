from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from .serializers import UsernameSerializer, EmailSerializer ,UserSerializer 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class Member(APIView):
    def post (self,request):
        data = request.data
        serializer = UserSerializer(data = data)
        if not serializer.is_valid():
            return Response({
                'status': 400,
                'message':serializer.errors
            },status.HTTP_400_BAD_REQUEST)
        else:
            instance = User.objects.create(username = data['username'],email = data['email'])
            instance.set_password(data['password'])
            instance.save()
            return Response({
                'status' : 201,
                'message':'User Creation Successful'
            },status.HTTP_201_CREATED)
    
    def get (self,request):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)
        obj = User.objects.all()
        serializer = UserSerializer(obj,many=True)
        return Response({
            'status':200,
            'message':'Fetch Successful',
            'data' : serializer.data
        },status.HTTP_200_OK)
    
    def delete(self,request):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)
        user_name = request.user.username
        instance = User.objects.get(username = user_name)
        instance.delete()
        return Response({
            'status':200,
            'message':'User Deleted Successfully'
        },status.HTTP_200_OK)
    
    def patch(self,request):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)
        username = request.user.username
        password = request.data['password']
        user = authenticate(username = username,password = password)
        if user is not None:
            id = request.data['id']
            instance = User.objects.get(id = id)
            if request.data['type'] == 'username':
                instance.username = request.data['username']
            elif request.data['type'] == 'email':
                instance.email = request.data['email']
            instance.save()
            return Response({
                'status': 200,
                'message': 'Update Successful'
            },status.HTTP_200_OK)
        else:
            return Response({
                'status':401,
                'message':'Invalid Username or Password'
            },status.HTTP_401_UNAUTHORIZED)
        

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
class getuserdetails(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        serializer = UserSerializer(request.user)
        return Response({
            'status':200,
            'message':'user details fetch successful',
            'username': serializer.data['username'],
            'email': serializer.data['email']
        })

class changepassword(APIView):
    def post(self,request):
        username = request.data['email']
        password = request.data['password']

        instance = User.objects.get(email = username)
        instance.set_password(password)
        instance.save()

        return Response({
            'status':200,
            'message':'Password Updated Successfully'
        })

        
