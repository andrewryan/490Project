from django.shortcuts import render
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
    all_houses = House.objects.all()
    num_of_houses = House.objects.count()
    # num_of_houses = House.objects.annotate(Count('caseNum'))
    # num_of_houses = House.objects.all.count()
    # num_of_houses = House.objects.filter(streetNum='3341').count()
    context = {
        # 'house_total':num_of_houses,
        'house_list':all_houses,
        'title':"WSdatabase",
        }
    return render(request,'wsdatabase.html',context, num_of_houses)

def propertyInfo(request):
    context = {
        'title':"Property Info",
        }
    return render(request,'propertyInfo.html',context)
