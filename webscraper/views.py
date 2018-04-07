from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.db.models import Q
from .deleteDatabase import deleteDatabase
from .updateDatabase import updateDatabase

from .models import *


def database(request):
    house_list = House.objects.all()
    # num_of_houses = House.objects.count()
    # queryset_list = House.objects.all()
    category_query = request.GET.get("category")
    condition_query = request.GET.get("condition")
    numBedrooms_query = request.GET.get("numBedrooms")
    yearBuilt_query = request.GET.get("yearBuilt")
    propertyType_query = request.GET.get("propertyType")
    if category_query:
        house_list = house_list.filter(
            Q(category__icontains=category_query),
            # Q(buildingConditionScore__icontains=condition_query),
            # Q(numBedrooms__icontains=numBedrooms_query),
            # Q(yearBuilt__icontains=yearBuilt_query),
            # Q(propertyType__icontains=propertyType_query)
            )

    num_of_houses = house_list.count()
    context = {
        'num_of_houses':num_of_houses,
        'house_list':house_list,
        'title':"Code Violations",
        }
    return render(request,'database.html',context)

def propertyInfo(request, caseNum):
    property_info = get_object_or_404(House, caseNum=caseNum)
    cur_property = House.objects.get(caseNum=caseNum)
    if cur_property.geoLookup != "":
        street_view_url = "https://www.google.com/maps/embed/v1/streetview?&location=" + cur_property.geoLookup + "&key=AIzaSyDWGLTRDyhM0EuhzZ3Jfk1WqA5MbHjrt78"
    else:
        street_view_url = ""

    context = {
        'street_view_url':street_view_url,
        'property_info':property_info,
        'title':"Property Info",
        }
    return render(request,'propertyInfo.html',context)

def runUpdate(request):
    # updateDatabase()
    context = {
        'title':"Update Database",
        }
    return render(request,'runUpdate.html',context)
