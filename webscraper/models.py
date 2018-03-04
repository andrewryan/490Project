from django.db import models
from django.conf import settings


class House(models.Model):
    # County property listing info
    caseNum = models.CharField(max_length=20)
    streetNum = models.CharField(max_length=20)
    streetName = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    # WhitePages property info
    neighborhood = models.CharField(max_length=40)
    propertyType = models.CharField(max_length=30)
    squareFootage = models.CharField(max_length=20)
    lotSize = models.CharField(max_length=20)
    beds = models.CharField(max_length=20)
    baths = models.CharField(max_length=20)
    yearBuilt = models.CharField(max_length=20)
    yearSold = models.CharField(max_length=20)
    purchasePrice = models.CharField(max_length=20)
    priceSqFt = models.CharField(max_length=20)
    # equity = models.CharField(max_length=10)

    def __str__(self):
        return u'%s %s' % (self.streetNum, self.streetName)
