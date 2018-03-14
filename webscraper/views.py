from django.shortcuts import render, get_object_or_404
from .deleteDatabase import deleteDatabase
from .updateDatabase import updateDatabase
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse

from .models import *


def database(request):
    house_list = House.objects.all()
    num_of_houses = House.objects.count()

    context = {
        'num_of_houses':num_of_houses,
        'house_list':house_list,
        'title':"Code Violations",
        }
    return render(request,'database.html',context)

def propertyInfo(request, caseNum):
    property_info = get_object_or_404(House, caseNum=caseNum)
    cur_property = House.objects.get(caseNum=caseNum)
    street_view_url = "https://www.google.com/maps/embed/v1/streetview?&location=" + cur_property.geoLookup + "&key=AIzaSyDWGLTRDyhM0EuhzZ3Jfk1WqA5MbHjrt78"

    context = {
        'street_view_url':street_view_url,
        'property_info':property_info,
        'title':"Property Info",
        }
    return render(request,'propertyInfo.html',context)

def runUpdate(request):
    # updateDatabase()
    # return HttpResponseRedirect('/')
    context = {
        'title':"Update Database",
        }
    return render(request,'updateDatabase.html',context)
