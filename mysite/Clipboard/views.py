from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.http import JsonResponse
import json
from django.db import IntegrityError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LinkSerializers
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
        try :
            object=Linkmodel(Link=Link)
            object.save()
            messages.add_message(request,messages.INFO,'Link Was Saved !')
            return redirect('clipboard')
        except IntegrityError :
            messages.add_message(request,messages.ERROR,'Link already exists in database')
            return redirect ('clipboard')

def fileholder(request):
    if request.method=="POST" :
        File=request.FILES.get("File")
        object=Filemodel(File=File)
        object.save()
        messages.add_message(request,messages.INFO,'File Was Saved !')
        return redirect('clipboard')

def textholder(request):
    if request.method=="POST":
        Text=request.POST.get("Text")
        try:
            object=Textmodel(Text=Text)
            object.save()
            messages.add_message(request,messages.INFO,'Text Was Saved !')
            return redirect('clipboard')
        except IntegrityError :
            messages.add_message(request,messages.ERROR,'Text already exits in database')
            return redirect('clipboard')


def viewclipboard(request):
    Linkitems = Linkmodel.objects.all()
    Textitems = Textmodel.objects.all()
    Fileitems = Filemodel.objects.all()
    # messages.add_message(request,messages.ERROR,'Its working')
    return render(request , 'viewclipboard.html',{'Linkitems':Linkitems,'Textitems':Textitems,'Fileitems':Fileitems})


def delitems(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        objecttype = data.get('objecttype')
        print(name)
        print(objecttype)
        if objecttype=="Text":
            entry = Textmodel.objects.get(Text=name)
            entry.delete()
        elif objecttype =="File":
            entry = Filemodel.objects.get(File=name)
            entry.delete()
        elif objecttype== "Link" :
            entry = Linkmodel.objects.get(Link=name)
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
        # obj = Linkmodel.objects.get(id=data['id'])
        # obj.delete()
        return Response({
            "message" : "Link Deleted !"
        })
        