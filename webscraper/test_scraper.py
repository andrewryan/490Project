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




# Testing urls
house_streetNum = "123"
house_streetName = "Main St"
location = house_streetNum + house_streetName + "," + "Sacramento" + "," + "CA"
location = location.replace(",","%2C")
location = location.replace(" ","+")
print(location)

from urllib.parse import urlparse
location = urlparse(location)
print(location)

# import urllib2
location = urllib.parse.urlencode({})

from urllib.parse import urlencode
final_location = urlencode(location)
print(final_location)

123+Main+St%2C+Sacramento%2C+CA

3341+10th+Ave%2C+Sacramento%2C+CA+95817
3341%2010th%20Ave%2C%20Sacramento%2C%20CA%2095817
"lat" : 38.542917,
"lng" : -121.470322
38.542917,-121.470322

https://maps.googleapis.com/maps/api/geocode/json?address=3341+10th+Ave%2C+Sacramento%2C+CA+95817&key=AIzaSyDWGLTRDyhM0EuhzZ3Jfk1WqA5MbHjrt78

https://www.google.com/maps/@?api=1&map_action=pano&3341%2010th%20Ave%2C%20Sacramento%2C%20CA%2095817
