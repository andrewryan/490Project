from django.shortcuts import render, get_object_or_404
from .deleteDatabase import deleteDatabase
from django.http import JsonResponse

from .models import *


def database(request):
    house_list = House.objects.all()
    # num_of_houses = House.objects.count()
    # num_of_houses = House.objects.all.count()
    context = {
        'house_list':house_list,
        'title':"Code Violations",
        }
    return render(request,'database.html',context)

def propertyInfo(request, caseNum):
    property_info = get_object_or_404(House, caseNum=caseNum)
    context = {
        'property_info':property_info,
        'title':"Property Info",
        }
    return render(request,'propertyInfo.html',context)

def runscript(request):
    test = deleteDatabase()
    context = {
        'test':test,
        'title':"runscript",
        }
    return render(request,'runscript.html',context)
