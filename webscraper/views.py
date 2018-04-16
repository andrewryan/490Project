from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.db.models import Q
from .deleteDatabase import deleteDatabase
from .updateDatabase import updateDatabase
import csv, pickle

from .models import *


def database(request):
    house_list = House.objects.all()
    zip_codes = House.objects.values('zipCode').distinct()
    category_query = request.GET.get("category")
    condition_query = request.GET.get("condition")
    numBedrooms_query = request.GET.get("numBedrooms")
    zipCode_query = request.GET.get("zipCode")
    propertyType_query = request.GET.get("propertyType")
    if category_query or condition_query or numBedrooms_query or zipCode_query or propertyType_query and numBedrooms_query != "5":
        house_list = house_list.filter(
            Q(category__icontains=category_query),
            Q(buildingConditionScore__icontains=condition_query),
            Q(numBedrooms__icontains=numBedrooms_query),
            Q(zipCode__icontains=zipCode_query),
            Q(propertyType__icontains=propertyType_query)
            )
    elif category_query or condition_query or numBedrooms_query or zipCode_query or propertyType_query and numBedrooms_query == "5":
        house_list = house_list.filter(
            Q(category__icontains=category_query),
            Q(buildingConditionScore__icontains=condition_query),
            Q(numBedrooms__gte=5),
            Q(zipCode__icontains=zipCode_query),
            Q(propertyType__icontains=propertyType_query)
            )

    with open('SearchResults.csv', 'w', newline='') as csv_file:
        thewriter = csv.writer(csv_file)
        thewriter.writerow(['Case #', 'Street #', 'Street', 'Category'])
        csv_list = house_list.values_list('caseNum', 'streetNum', 'streetName', 'category')
        for data in csv_list:
            thewriter.writerow(data)

    num_of_houses = house_list.count()
    # request.session['house_list'] = house_list
    request.session['test'] = '123'
    # request.session['csv_list'] = json.dump(house_list)
    context = {
        # 'csv_file':csv_file,
        'zip_codes':zip_codes,
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


# def downloadLink(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="SearchResults.csv"'
#     with open('SearchResults.csv', 'rb') as csv:
#         response = HttpResponse(csv.read())
#
#     context = {
#         'response':response,
#         'title':"Update Database",
#         }
#     return render(request,'downloadLink.html',context)


def downloadLink(request):
    # house_list = request.session.get('house_list')
    test = request.session.get('test')
    # csv_list = request.session.get('csv_list')

    # with open('SearchResults.csv') as fh:
    #     a = json.load(fh)
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    # writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    # writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    with open('SearchResults.csv', 'w', newline='') as csv_file:
        # thewriter = csv.writer(csv_file)
        writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
        writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
        writer.writerow([test])
        # thewriter.writerow(['Case #', 'Street #', 'Street', 'Category'])
        # csv_list = house_list.values_list('caseNum', 'streetNum', 'streetName', 'category')
        # for data in csv_list:
        #     thewriter.writerow(data)

    # with open('SearchResults.csv', 'w', newline='') as csv_file:
    #     # writer = csv.writer(csv_file)
    #     writer.writerow(['Case #', 'Street #', 'Street', 'Category'])
    #     # csv_file = house_list.values_list('caseNum', 'streetNum', 'streetName', 'category')
    #     for data in house_list:
    #         writer.writerow(data)

    return response
