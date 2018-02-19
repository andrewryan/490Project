import re
import requests
from bs4 import BeautifulSoup
from .models import *

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
        print(repr(string).replace("'", ""))
    i += 1
#############################################################################

from webscraper.models import *
i = 0
j = 0
for string in soup.table.stripped_strings:
    # if i > 8 and i < 25:
    if i > 8:
        if j == 0:
            house_caseNum = repr(string).replace("'", "")
            print('j = ' + str(j) + " , caseNum = " + house_caseNum)
            j += 1
        elif j == 1:
            house_streetNum = repr(string).replace("'", "")
            print('j = ' + str(j) + " , streetNum = " +  house_streetNum)
            j += 1
        elif j == 2:
            house_streetName = repr(string).replace("'", "")
            print('j = ' + str(j) + " , streetName = " +  house_streetName)
            j += 1
        elif j == 3:
            house_category = repr(string).replace("'", "")
            print('j = ' + str(j) + " , category = " +  house_category)
            addProperty = House(caseNum=house_caseNum,
                                streetNum=house_streetNum,
                                streetName=house_streetName,
                                category=house_category)
            addProperty.save()
            j = 0
    i += 1


######### loop to delete entire contents of House model #########
for x in House.objects.all().iterator(): x.delete()

###### returns the first four property listings
i = 0
for string in soup.table.stripped_strings:
    if i > 8 and i < 25:
        print(repr(string).replace("'", ""))
    i += 1
