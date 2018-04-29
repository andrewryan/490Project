import requests, json
from bs4 import BeautifulSoup
from datetime import date
from django.utils import timezone
from datetime import datetime

from webscraper.models import *

def updateDatabase():
    url = "http://www.citizenserve.com/Sacramento/CitizenController?Action=SacramentoOpenHousingCases&CtzPagePrefix=Sa&InstallationID=43"
    request = requests.get(url)
    soup = BeautifulSoup(request.content, "html.parser")
    housingData = soup.find_all("td")

    i = 0
    j = 0
    todaysDate = timezone.now().date()

    for string in housingData:
        if i > 22:
            if j == 0:
                house_caseNum = string.text.strip()
                j += 1

            elif j == 1:
                house_streetNum = string.text.strip()
                j += 1

            elif j == 2:
                house_streetName = string.text.strip()
                j += 1

            elif j == 3:
                house_category = string.text.strip()
                j = 0
                # If the property exists then update the days_old field,
                # otherwise add the property to the database
                if House.objects.filter(caseNum=house_caseNum).exists():
                    cur_listing = House.objects.get(caseNum=house_caseNum)
                    dateAdded = cur_listing.dateAdded
                    # dateAdded is stored as a string in the DB, used
                    # to convert dateAdded back to datetime.date() form
                    dateListed = datetime.strptime(dateAdded, '%Y-%m-%d').date()
                    days_old = todaysDate - dateListed
                    days_old = days_old.days
                    cur_listing.daysOld = days_old
                    cur_listing.save(update_fields=['daysOld'])
                else:
                    # Used to find lat/long of property to be used for
                    # google maps street view
                    location = house_streetNum + " " + house_streetName + ", " + "Sacramento" + "," + " CA"
                    location = location.replace(",","%2C")
                    location = location.replace(" ","+")
                    geo_results = geocodeLookup(location)
                    # Parsing geo_results to separate lat/long and zip code
                    lat_long = geo_results[0]
                    zipCode = geo_results[1]
                    date_added = todaysDate

                    addProperty = House(caseNum=house_caseNum,
                                        streetNum=house_streetNum,
                                        streetName=house_streetName,
                                        category=house_category,
                                        dateAdded=date_added,
                                        daysOld='0',
                                        geoLookup=lat_long,
                                        zipCode=zipCode,)
                    addProperty.save()
                    # Used to retrieve and save additional property details to object
                    if house_streetNum != "" and house_streetName != "":
                        propertyDetails(house_streetNum, house_streetName, house_caseNum, zipCode)
        i += 1

def geocodeLookup(location):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address="
    apiKey = "&key=AIzaSyDWGLTRDyhM0EuhzZ3Jfk1WqA5MbHjrt78"
    finalURL = url + location + apiKey
    request = requests.get(finalURL)
    # Successful response returned
    if request.status_code == 200:
        # Extracting data in json format
        json_obj = request.json()
        # Testing for results returned with populated data
        if json_obj.get("results", []):
            # Extracting latitude and longitude
            latitude = json_obj["results"][0]["geometry"]["location"]["lat"]
            longitude = json_obj["results"][0]["geometry"]["location"]["lng"]
            # Returning zip code to use in property details function
            addressComponent = json_obj['results'][0]['address_components']
            for x in addressComponent:
                if x['types'] == ['postal_code']:
                    zipCode = x['long_name']
        # Testing if latitude and longitude were saved as local variables
        if 'latitude' in locals() and 'longitude' in locals():
            geoLookup = str(latitude) + "," + str(longitude)
        # Either latitude or longitude were missing from response
        else:
            geoLookup = ""
        if 'zipCode' not in locals():
            zipCode = ""
        return(geoLookup, zipCode)

def propertyDetails(house_streetNum, house_streetName, house_caseNum, zipCode):
    url = 'https://api.housecanary.com/v2/property/details'
    address = house_streetNum + " " + house_streetName
    params = {'address': address ,'zipcode': zipCode}
    response = requests.get(url, params=params, auth=('BJ0FREFH19V6WSLM6QPW', 'CIPKYkzl4qjQVzFIlUQGl411w4H6ZPsu'))
    json_obj = response.json()
    # Checking response code for error
    api_code = json_obj[0]['property/details']['api_code']
    if str(api_code) == "204":
        return
    # Obtaining results from json response
    squareFootage = json_obj[0]['property/details']['result']['property']['building_area_sq_ft']
    buildingConditionScore = json_obj[0]['property/details']['result']['property']['building_condition_score']
    exteriorWalls = json_obj[0]['property/details']['result']['property']['exterior_walls']
    fireplace = json_obj[0]['property/details']['result']['property']['fireplace']
    garageCount = json_obj[0]['property/details']['result']['property']['garage_parking_of_cars']
    numStories = json_obj[0]['property/details']['result']['property']['no_of_stories']
    numBedrooms = json_obj[0]['property/details']['result']['property']['number_of_bedrooms']
    pool = json_obj[0]['property/details']['result']['property']['pool']
    propertyType = json_obj[0]['property/details']['result']['property']['property_type']
    roofCover = json_obj[0]['property/details']['result']['property']['roof_cover']
    propertyAcreage = json_obj[0]['property/details']['result']['property']['site_area_acres']
    style = json_obj[0]['property/details']['result']['property']['style']
    numBaths = json_obj[0]['property/details']['result']['property']['total_bath_count']
    yearBuilt = json_obj[0]['property/details']['result']['property']['year_built']
    # Property tax info
    apn = json_obj[0]['property/details']['result']['assessment']['apn']
    assessmentYear = json_obj[0]['property/details']['result']['assessment']['assessment_year']
    taxYear = json_obj[0]['property/details']['result']['assessment']['tax_year']
    totalAssessedValue = json_obj[0]['property/details']['result']['assessment']['total_assessed_value']
    taxAmount = json_obj[0]['property/details']['result']['assessment']['tax_amount']
    # Updating model fields before returning function
    cur_property = House.objects.get(caseNum=house_caseNum)

    cur_property.squareFootage = squareFootage
    cur_property.save(update_fields=['squareFootage'])

    cur_property.buildingConditionScore = buildingConditionScore
    cur_property.save(update_fields=['buildingConditionScore'])

    cur_property.exteriorWalls = exteriorWalls
    cur_property.save(update_fields=['exteriorWalls'])

    cur_property.fireplace = fireplace
    cur_property.save(update_fields=['fireplace'])

    cur_property.garageCount = garageCount
    cur_property.save(update_fields=['garageCount'])

    cur_property.numStories = numStories
    cur_property.save(update_fields=['numStories'])

    cur_property.numBedrooms = numBedrooms
    cur_property.save(update_fields=['numBedrooms'])

    cur_property.pool = pool
    cur_property.save(update_fields=['pool'])

    cur_property.propertyType = propertyType
    cur_property.save(update_fields=['propertyType'])

    cur_property.roofCover = roofCover
    cur_property.save(update_fields=['roofCover'])

    cur_property.propertyAcreage = propertyAcreage
    cur_property.save(update_fields=['propertyAcreage'])

    cur_property.style = style
    cur_property.save(update_fields=['style'])

    cur_property.numBaths = numBaths
    cur_property.save(update_fields=['numBaths'])

    cur_property.yearBuilt = yearBuilt
    cur_property.save(update_fields=['yearBuilt'])

    cur_property.apn = apn
    cur_property.save(update_fields=['apn'])

    cur_property.assessmentYear = assessmentYear
    cur_property.save(update_fields=['assessmentYear'])

    cur_property.taxYear = taxYear
    cur_property.save(update_fields=['taxYear'])

    cur_property.totalAssessedValue = totalAssessedValue
    cur_property.save(update_fields=['totalAssessedValue'])

    cur_property.taxAmount = taxAmount
    cur_property.save(update_fields=['taxAmount'])

    return
