import re
import requests
from bs4 import BeautifulSoup

url = "http://www.citizenserve.com/Sacramento/CitizenController?Action=SacramentoOpenHousingCases&CtzPagePrefix=Sa&InstallationID=43"
req = requests.get(url)

soup = BeautifulSoup(req.content, "html.parser")

numberOfCases = soup.find("p", {"class": "style5"})

# Returns the number of properties listed
numStr = re.search('\d+', numberOfCases.text)
numInt = numStr.group(0)
print(numInt.replace("'",""))

# housingData = soup.find_all("tbody")
housingData = soup.find_all("td") # closest match
housingData = soup.find_all("tr") # no addresses
# unless print item.text

housingData = soup.find_all("table")


########### working the best ###########
for string in soup.table.stripped_strings:
    print(repr(string).replace("'", ""))

for i in range(0,len(soup.table)):
    print(i)
    for string in soup.table.stripped_strings:
        if i > 4:
            print(repr(string).replace("'", ""))

###### works how I want it to, gets only the property data inside of the table
i = 0
for string in soup.table.stripped_strings:
    i += 1
    if i > 5:
        print(repr(string).replace("'", ""))
##############################################################################


# finds all tags that start with a 'b' and lists their text
for tag in soup.find_all(re.compile("^b")):
    print(tag.text.replace("\n",""))


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
