import requests, json
from bs4 import BeautifulSoup
from datetime import date
from django.utils import timezone
from datetime import datetime

from webscraper.models import *

def updateDatabase():
    # url = "http://www.citizenserve.com/Sacramento/CitizenController?Action=SacramentoOpenHousingCases&CtzPagePrefix=Sa&InstallationID=43"
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
                # date_added = todaysDate
                # Used to find lat/long of property to be used for
                # google maps street view
                # location = house_streetNum + " " + house_streetName + ", " + "Sacramento" + "," + " CA"
                # location = location.replace(",","%2C")
                # location = location.replace(" ","+")
                # # geo_results = geocodeLookup(location)
                # addProperty = House(caseNum=house_caseNum,
                #                     streetNum=house_streetNum,
                #                     streetName=house_streetName,
                #                     category=house_category,
                #                     dateAdded=date_added,
                #                     daysOld='0',)
                #                     # geoLookup=geo_results,)
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
                    date_added = todaysDate
                    addProperty = House(caseNum=house_caseNum,
                                        streetNum=house_streetNum,
                                        streetName=house_streetName,
                                        category=house_category,
                                        dateAdded=date_added,
                                        daysOld='0',
                                        geoLookup=geo_results,)
                    addProperty.save()
        i += 1

# return House.objects.all() to use with ajax call,
# comment out everything but leave return db for testing

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
        # Testing if latitude and longitude were saved as local variables
        if 'latitude' in locals() and 'longitude' in locals():
            geoLookup = str(latitude) + "," + str(longitude)
        # Either latitude or longitude were missing from response
        else:
            geoLookup = ""
        return(geoLookup)
