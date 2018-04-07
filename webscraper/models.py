from django.db import models
from django.conf import settings


class House(models.Model):
    ########### County property listing info #############
    caseNum = models.CharField(max_length=20)
    streetNum = models.CharField(max_length=20)
    streetName = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    ########### House Canary property info ###############
    squareFoot = models.CharField(max_length=10)
    buildingConditionScore = models.CharField(max_length=5)
    exteriorWalls = models.CharField(max_length=50)
    fireplace = models.CharField(max_length=10)
    garageCount = models.CharField(max_length=10)
    numStories = models.CharField(max_length=10)
    numBedrooms = models.CharField(max_length=10)
    pool = models.CharField(max_length=10)
    propertyType = models.CharField(max_length=50)
    roofCover = models.CharField(max_length=30)
    propertyAcreage = models.CharField(max_length=20)
    style = models.CharField(max_length=50)
    numBaths = models.CharField(max_length=10)
    yearBuilt = models.CharField(max_length=10)
    ########### Tax property info #######################
    apn = models.CharField(max_length=30)
    assessmentYear = models.CharField(max_length=20)
    taxYear = models.CharField(max_length=10)
    totalAssessedValue = models.CharField(max_length=20)
    taxAmount = models.CharField(max_length=20)
    ########### Other property info #####################
    daysOld = models.CharField(max_length=10)
    dateAdded = models.CharField(max_length=20)
    geoLookup = models.CharField(max_length=30)
    # latitude = models.CharField(max_length=30)
    # longitude = models.CharField(max_length=30)
    zipCode = models.CharField(max_length=20)


    def __str__(self):
        return u'%s %s' % (self.streetNum, self.streetName)
