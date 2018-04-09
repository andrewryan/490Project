from django.db import models
from django.conf import settings


class House(models.Model):
    ########### County property listing info #############
    caseNum = models.CharField(max_length=20)
    streetNum = models.CharField(max_length=20)
    streetName = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    ########### House Canary property info ###############
    squareFootage = models.CharField(max_length=10, null=True)
    buildingConditionScore = models.CharField(max_length=5, null=True)
    exteriorWalls = models.CharField(max_length=50, null=True)
    fireplace = models.CharField(max_length=10, null=True)
    garageCount = models.CharField(max_length=10, null=True)
    numStories = models.CharField(max_length=10, null=True)
    numBedrooms = models.CharField(max_length=10, null=True)
    pool = models.CharField(max_length=10, null=True)
    propertyType = models.CharField(max_length=50, null=True)
    roofCover = models.CharField(max_length=30, null=True)
    propertyAcreage = models.CharField(max_length=20, null=True)
    style = models.CharField(max_length=50, null=True)
    numBaths = models.CharField(max_length=10, null=True)
    yearBuilt = models.CharField(max_length=10, null=True)
    ########### Property tax info #######################
    apn = models.CharField(max_length=30, null=True)
    assessmentYear = models.CharField(max_length=20, null=True)
    taxYear = models.CharField(max_length=10, null=True)
    totalAssessedValue = models.CharField(max_length=20, null=True)
    taxAmount = models.CharField(max_length=20, null=True)
    ########### Other property info #####################
    daysOld = models.CharField(max_length=10)
    dateAdded = models.CharField(max_length=20)
    geoLookup = models.CharField(max_length=30)
    zipCode = models.CharField(max_length=20)


    def __str__(self):
        return u'%s %s' % (self.streetNum, self.streetName)
