from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.http import JsonResponse
import json
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LinkSerializers ,TextSerializers ,FileSerializers, AnotherTextSerializers, AnotherFileSerializers, AnotherLinkSerializers
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.

def clipboard(request):
    if request.user.is_authenticated:
        return render (request,'clipboard.html')
    else :
        messages.add_message(request,messages.INFO,'please Login to view this page !')
        return redirect('signinuser')

def linkholder(request):
    if request.method=="POST":
        Link=request.POST.get("Link")
        user_obj = request.user.username
        try :
            object=Linkmodel(Link=Link,user = user_obj)
            object.save()
            messages.add_message(request,messages.INFO,'Link Was Saved !')
            return redirect('clipboard')
        except IntegrityError :
            messages.add_message(request,messages.ERROR,'Link already exists in database')
            return redirect ('clipboard')

def fileholder(request):
    if request.method=="POST" :
        File=request.FILES.get("File")
        user_obj = request.user.username
        object=Filemodel(File=File,user_obj=user_obj)
        object.save()
        messages.add_message(request,messages.INFO,'File Was Saved !')
        return redirect('clipboard')

def textholder(request):
    if request.method=="POST":
        Text=request.POST.get("Text")
        user_obj = request.user.username
        try:
            object=Textmodel(Text=Text,user_obj=user_obj)
            object.save()
            messages.add_message(request,messages.INFO,'Text Was Saved !')
            return redirect('clipboard')
        except IntegrityError :
            messages.add_message(request,messages.ERROR,'Text already exits in database')
            return redirect('clipboard')


def viewclipboard(request):
    Linkitems = Linkmodel.objects.filter( user_obj = request.user.username)
    Textitems = Textmodel.objects.filter(user_obj = request.user.username)
    Fileitems = Filemodel.objects.filter(user_obj = request.user.username)
    # messages.add_message(request,messages.ERROR,'Its working')
    return render(request , 'viewclipboard.html',{'Linkitems':Linkitems,'Textitems':Textitems,'Fileitems':Fileitems})


def delitems(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        objecttype = data.get('objecttype')
        idname = data.get('idname')
        print(name)
        print(objecttype)
        if objecttype=="Text":
            entry = Textmodel.objects.get(id=idname)
            entry.delete()
        elif objecttype =="File":
            entry = Filemodel.objects.get(id=idname)
            entry.delete()
        elif objecttype== "Link" :
            entry = Linkmodel.objects.get(id=idname)
            entry.delete()
        else :
            response_data = {
                'error':'Something Went Wrong'
            }
            return JsonResponse(response_data,status=400)
        return redirect('viewclipboard')
    

    
class linkhandler(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data = request.data
        print(data)
        serializer = LinkSerializers(data=data)
        if not serializer.is_valid():
            return Response({
                'status' : 400,
                'message':'Bad request, invaild Item given',
                'details':serializer.errors
            },status.HTTP_400_BAD_REQUEST)
        print(serializer.data)
        instance = Linkmodel(Link = serializer.data['Link'],user= request.user.username)
        instance.save()
        return Response({
            'status' : 200,
            'message' : 'link Stored Successfully',
        },status.HTTP_200_OK)

    def get(self,request):
        obj = Linkmodel.objects.filter(user=request.user.username)
        serializer = AnotherLinkSerializers(obj,many=True)
        return Response({
            'status':200,
            'message':'Fetch Successful',
            'data':serializer.data
        },status.HTTP_200_OK)
    
    def delete(self,request):
        data = request.data
        instance = Linkmodel.objects.get(id=data['id'])
        instance.delete()
        return Response({
            'status':200,
            'message': 'Link deleted'
        },status.HTTP_200_OK)



class texthandler(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data = request.data
        serializer = TextSerializers(data=data)
        if not serializer.is_valid():
            return Response({
                'status' : 400,
                'message':'Bad request, invaild Item given',
            },status.HTTP_400_BAD_REQUEST)

        instance = Textmodel(Text = serializer.data['Text'],user = request.user.username)    
        instance.save()
        return Response({
            'status' : 200,
            'message' : 'Text Stored Successfully',
        },status.HTTP_200_OK)

    def get(self,request):
        obj = Textmodel.objects.filter(user=request.user.username)
        serializer = AnotherTextSerializers(obj,many=True)
        return Response({
            'status':200,
            'message':'Fetch Successful',
            'data':serializer.data
        },status.HTTP_200_OK)
    
    def delete(self,request):
        data = request.data
        instance = Textmodel.objects.get(id=data['id'])
        instance.delete()
        return Response({
            'status':200,
            'message': 'Text deleted'
        },status.HTTP_200_OK)

class filehandler(APIView):
    permission_classes =[IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
    def post (self,request):
        data = request.data.copy()
        data['user_obj'] = request.user.username
        serializer = FileSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':200,
                'message':'The file is uploaded'
            },status.HTTP_200_OK)
        else:
            return Response({
            'status':400,
            'message':'Invalid Value Entered'
            },status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        data = Filemodel.objects.filter(user_obj=request.user.username)
        serializer = FileSerializers(data , many=True)
        return Response({
            'status':200,
            'message':'fetch Successful',
            'data': serializer.data
        },status.HTTP_200_OK)
    
    def delete(self,request):
        data = request.data
        instance = Filemodel.objects.get(id = data['id'])
        instance.delete()
        return Response({
            'status':200,
            'message': 'Item Deleted'
        },status.HTTP_200_OK)
