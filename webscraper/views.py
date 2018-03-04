from django.shortcuts import render, get_object_or_404
from .models import *


def WSdatabase(request):
    house_list = House.objects.all()
    num_of_houses = House.objects.count()
    # num_of_houses = House.objects.all.count()
    context = {
        'house_list':house_list,
        'title':"Code Violations",
        }
    return render(request,'wsdatabase.html',context, num_of_houses)

def propertyInfo(request, caseNum):
    property_info = get_object_or_404(House, caseNum=caseNum)
    context = {
        'property_info':property_info,
        'title':"Property Info",
        }
    return render(request,'propertyInfo.html',context)
