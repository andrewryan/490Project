import requests
from bs4 import BeautifulSoup
from datetime import date
from django.utils import timezone
from datetime import datetime

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
    # todaysDate = timezone.now().date()
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
    #             date_added = todaysDate
    #             addProperty = House(caseNum=house_caseNum,
    #                                 streetNum=house_streetNum,
    #                                 streetName=house_streetName,
    #                                 category=house_category,
    #                                 dateAdded=date_added,
    #                                 daysOld='0',)
    #             j = 0
    #             # If the property exists then update the days_old field,
    #             # otherwise add the property to the database
    #             if House.objects.filter(caseNum=house_caseNum).exists():
    #                 cur_listing = House.objects.get(caseNum=house_caseNum)
    #                 dateAdded = cur_listing.dateAdded
    #                 # dateAdded is stored as a string in the DB, used
    #                 # to convert dateAdded back to datetime.date() form
    #                 dateListed = datetime.strptime(dateAdded, '%Y-%m-%d').date()
    #                 days_old = todaysDate - dateListed
    #                 days_old = days_old.days
    #                 cur_listing.daysOld = days_old
    #                 cur_listing.save(update_fields=['daysOld'])
    #             else:
    #                 addProperty.save()
    #     i += 1
