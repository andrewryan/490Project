######################### for county website #########################################

import requests
from bs4 import BeautifulSoup
from webscraper.models import *

url = "http://www.citizenserve.com/Sacramento/CitizenController?Action=SacramentoOpenHousingCases&CtzPagePrefix=Sa&InstallationID=43"
request = requests.get(url)

soup = BeautifulSoup(request.content, "html.parser")

numberOfCases = soup.find("p", {"class": "style5"})

############## Returns the number of properties listed ###################
numStr = re.search('\d+', numberOfCases.text)
numInt = numStr.group(0)
print(numInt.replace("'",""))

############# Returns property info on county website #####################
i = 0
for string in soup.table.stripped_strings:
    if i > 4:
        print(string)
    i += 1
#############################################################################


#############################################################################
############################ THIS IS WORKING ################################
#############################################################################
housingData = soup.find_all("td")

i = 0
j = 0
# numHouses = 0
for string in housingData:
    if i > 22:
        # if string.text == "":
        #     # print("*** NOT A STRING, OR BLANK ***")
        #     j += 1
        if j == 0:
            house_caseNum = string.text.strip()
            print('j = ' + str(j) + " , caseNum = " + house_caseNum)
            j += 1
        elif j == 1:
            house_streetNum = string.text.strip()
            print('j = ' + str(j) + " , streetNum = " +  house_streetNum)
            j += 1
        elif j == 2:
            house_streetName = string.text.strip()
            print('j = ' + str(j) + " , streetName = " +  house_streetName)
            j += 1
        elif j == 3:
            house_category = string.text.strip()
            print('j = ' + str(j) + " , category = " +  house_category)
            addProperty = House(caseNum=house_caseNum,
                                streetNum=house_streetNum,
                                streetName=house_streetName,
                                category=house_category)
            addProperty.save()
            j = 0
            # numHouses += 1
    i += 1
# propertyTotal(house_total = numHouses).save()
# create another model (propertyTotal) just to store the number of
# houses in database

######### loop to delete entire contents of House model #########
for x in House.objects.all().iterator(): x.delete()


# soup.table.stripped_strings strips away the empty fields,
# which messes up populating my House model objects
# this combo works to find the empty data fields
housingData = soup.find_all("td")
i = 0
j = 0
for string in housingData:
    if i > 8:
        print(string.text)
        # if string.text == "":
        #     j += 1
        #     print("empty string " + str(j) + "   *** NOT A STRING, OR BLANK ***")
    i += 1

i = 0
j = 0
for string in housingData:
    if i > 17:
        print(string.text)
        # if string.text == "":
        #     j += 1
        #     print("empty string " + str(j) + "   *** NOT A STRING, OR BLANK ***")
    i += 1

################# testing for blank data fields
i = 0
j = 0
for string in soup.table.stripped_strings:
# for string in housingData:
# for string in soup.table.strings:
    # if i > 9:
    if i > 8:
        print(string)
        # print(string.text)
        # print(string.text.strip())
        # print(string.text.replace("\n",""))
        # if string.text == "":
        #     j += 1
        #     print("empty string " + str(j) + "   *** NOT A STRING, OR BLANK ***")
        # returns too many results
        # if string.text.strip() == "":
        #     print("*** NOT A STRING, OR BLANK ***")
    i += 1



########### working need to check for blank data fields ####################
from webscraper.models import *
i = 0
j = 0
for string in soup.table.stripped_strings:
    # if i > 8 and i < 25:
    if i > 8:
        if j == 0:
            house_caseNum = string
            print('j = ' + str(j) + " , caseNum = " + house_caseNum)
            j += 1
        elif j == 1:
            house_streetNum = string
            print('j = ' + str(j) + " , streetNum = " +  house_streetNum)
            j += 1
        elif j == 2:
            house_streetName = string
            print('j = ' + str(j) + " , streetName = " +  house_streetName)
            j += 1
        elif j == 3:
            house_category = string
            print('j = ' + str(j) + " , category = " +  house_category)
            addProperty = House(caseNum=house_caseNum,
                                streetNum=house_streetNum,
                                streetName=house_streetName,
                                category=house_category)
            addProperty.save()
            j = 0
    i += 1
#######################################################################


######### loop to delete entire contents of House model #########
for x in House.objects.all().iterator(): x.delete()

###### returns the first four property listings
i = 0
for string in soup.table.stripped_strings:
    if i > 8 and i < 25:
        print(repr(string).replace("'", ""))
    i += 1






#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
housingData = soup.find_all("tbody")
housingData = soup.find_all("td") # closest match
housingData = soup.find_all("tr") # no addresses
# unless print item.text

housingData = soup.find_all("table")


########### working the best ###########
for string in soup.table.stripped_strings:
    print(repr(string).replace("'", ""))


# finds all tags that start with a 'b' and lists their text
for tag in soup.find_all(re.compile("^b")):
    print(tag.text.replace("\n",""))

for item in housingData:
    print(item.text.replace("\n",""))

# print(soup.table.text.replace("     ",""))
############## returns the same thing as:
# housingData = soup.find_all("tr")    , then,
# for item in housingData:
#     print(item.text)

# one row = 4 columns
# iterate through the soup and create 1 row
# for every 4 items

for item in housingData:
    print(item.text.replace("\n",""))

for item in housingData:
    print(item.text)

for item in housingData:
    print(item.contents)

for item in housingData:
    print(item.contents[1])

for item in housingData:
    print(item.contents[1].text.replace("\n",""))

################################################################################
################################################################################



if House.objects.filter(caseNum='16-02620').exists():
    print("object exists")
else:
    print("does not exist")
    break

num_of_houses = House.objects.count()
print(num_of_houses)

from django.utils import timezone
timezone.now()
# returns:
datetime (YYYY-MM-DD HH:MM:SS)

# for just date
myDate = timezone.now()
myDate.date()
# returns:
datetime.date(2018, 3, 10)

#####################################
from datetime import date

d0 = date(2008, 8, 18)
d1 = date(2008, 9, 26)
delta = d1 - d0
print(delta.days)
#####################################

dateAdded = timezone.now().date()
todaysDate = timezone.now().date()
numDays = todaysDate - dateAdded
print(numDays.days)


######################### Testing geocode api #################################

import json, requests
from webscraper.models import *

3632    52ND ST AKA 3640 52ND ST.
5011	ALCOTT DR
7504	29TH ST
2961	29TH AV
house_streetNum = "5011"
house_streetName = "ALCOTT DR"

house_streetNum = "3341"
house_streetName = "10th Ave"
location = house_streetNum + " " + house_streetName + ", " + "Sacramento" + "," + " CA"
location = location.replace(",","%2C")
location = location.replace(" ","+")
print(location)

location = house_streetNum + " " + house_streetName + ", " + "Sacramento" + "," + " CA"
location = location.replace(",","%2C")
location = location.replace(" ","+")
geocodeLookup(location)



# def geocodeLookup(location):
url = "https://maps.googleapis.com/maps/api/geocode/json?address="
apiKey = "&key=AIzaSyDWGLTRDyhM0EuhzZ3Jfk1WqA5MbHjrt78"
finalURL = url + location + apiKey
request = requests.get(finalURL)
if request.status_code == 200:
    # Extracting data in json format
    json_obj = request.json()
    # Testing for valid address
    # if json_obj.get("status", "ZERO_RESULTS"):
    #     print("ZERO RESULTS")
    # Testing for results returned with populated data
    if json_obj.get("results", []):
        # Extracting latitude and longitude
        # of the first matching location
        latitude = json_obj['results'][0]['geometry']['location']['lat']
        longitude = json_obj['results'][0]['geometry']['location']['lng']
        # Returning zip code to use in property details function
        addressComponent = json_obj['results'][0]['address_components']
        for x in addressComponent:
            if x['types'] == ['postal_code']:
                zipCode = x['long_name']
    # Testing if latitude and longitude existed
    if 'latitude' in locals() and 'longitude' in locals():
        geoLookup = str(latitude) + "," + str(longitude)
        # return(geoLookup)
        # print(geoLookup)
    else:
        # Either latitude or longitude were missing from response
        geoLookup = "missing either latitude or longitude"
    if 'zipCode' not in locals():
        zipCode = ""
    # print('geoLookup = ' + geoLookup + ' zipCode = ' + zipCode)
    print(geoLookup, zipCode)
    # geo_results = geoLookup, zipCode

########################### House Canary #####################################
import json, requests
from webscraper.models import *

def propertyDetails(location, zipCode):
url = 'https://api.housecanary.com/v2/property/details'
house_streetNum = "3341"
house_streetName = "10th Ave"
zipCode = "95817"
address = house_streetNum + " " + house_streetName
params = {'address': address ,'zipcode': zipCode}
response = requests.get(url, params=params, auth=('BJ0FREFH19V6WSLM6QPW', 'CIPKYkzl4qjQVzFIlUQGl411w4H6ZPsu'))



addressComponent = json_obj['results'][0]['address_components']
for x in addressComponent:
    if x['types'] == ['postal_code']:
        print(x['long_name'])
