from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.http import JsonResponse
import json
from django.db import IntegrityError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LinkSerializers ,TextSerializers ,FileSerializers

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
            object=Linkmodel(Link=Link,user_obj=user_obj)
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
    

    
@api_view(['POST','GET','DELETE'])
def apilink(request):
    if request.method == 'POST':
        data=request.data
        serializer = LinkSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == "GET":
        obj = Linkmodel.objects.all()
        serializer = LinkSerializers(obj,many=True)
        return Response(serializer.data)
    elif request.method == "DELETE":
        data = request.data
        print(data)
        print(data['id'])
        obj = Linkmodel.objects.filter(id=data['id'])
        obj.delete()
        return Response({
            "message" : "Link Deleted !"
        })

@api_view(['POST','GET','DELETE'])        
def apitext(request):
    if request.method == "POST":
        data = request.data
        serializer = TextSerializers
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == "GET":
        obj = Textmodel.objects.all()
        serializer = TextSerializers(obj,many=True)
        return Response(serializer.data)
    elif request.method == "DELETE":
        data = request.data
        print(data)
        print(data['id'])
        obj = Linkmodel.objects.filter(id=data['id'])
        obj.delete()
        return Response({
            "message" : "Link Deleted !"
        })
    
