from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.http import JsonResponse
import json
from django.db import IntegrityError
# Create your views here.
def clipboard(request):
    return render (request,'clipboard.html')

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