from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *

# from django.db.models import Count

# Create your views here.
# def WSdatabase(request):
#     context = {
#         'title':"WSdatabase",
#         }
#     return render(request,'WSdatabase.html',context)

def WSdatabase(request):
    house_list = House.objects.all()
    num_of_houses = House.objects.count()
    # num_of_houses = House.objects.annotate(Count('caseNum'))
    # num_of_houses = House.objects.all.count()
    # num_of_houses = House.objects.filter(streetNum='3341').count()
    context = {
        # 'house_total':num_of_houses,
        'house_list':house_list,
        'title':"Code Violations",
        }
    return render(request,'wsdatabase.html',context, num_of_houses)

def propertyInfo(request, caseNum):
    # info = House.objects.all().filter(caseNum='17-012307')
    property_info = get_object_or_404(House, caseNum=caseNum)
    context = {
        'property_info':property_info,
        'title':"Property Info",
        }
    return render(request,'propertyInfo.html',context)
