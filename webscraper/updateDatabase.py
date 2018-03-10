import requests
from bs4 import BeautifulSoup
from webscraper.models import *
from .views import *

def updateDatabase():
    test = "testing"
    return test

    # url = "http://www.citizenserve.com/Sacramento/CitizenController?Action=SacramentoOpenHousingCases&CtzPagePrefix=Sa&InstallationID=43"
    # request = requests.get(url)
    # soup = BeautifulSoup(request.content, "html.parser")
    # housingData = soup.find_all("td")
    #
    # i = 0
    # j = 0
    #
    # for string in housingData:
    #     if i > 22:
    #         if j == 0:
    #             house_caseNum = string.text.strip()
    #             j += 1
    #
    #         elif j == 1:
    #             house_streetNum = string.text.strip()
    #             j += 1
    #
    #         elif j == 2:
    #             house_streetName = string.text.strip()
    #             j += 1
    #
    #         elif j == 3:
    #             house_category = string.text.strip()
    #             addProperty = House(caseNum=house_caseNum,
    #                                 streetNum=house_streetNum,
    #                                 streetName=house_streetName,
    #                                 category=house_category)
    #             # addProperty.save()
    #             j = 0
    #             if House.objects.filter(caseNum=house_caseNum).exists():
    #                 break
    #             else:
    #                 addProperty.save()
    #     i += 1
