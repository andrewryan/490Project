from django.db import models
from django.conf import settings


class House(models.Model):
    ########### County property listing info ##########
    caseNum = models.CharField(max_length=20)
    streetNum = models.CharField(max_length=20)
    streetName = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    ########### WhitePages property info ##############
    equity = models.CharField(max_length=10)
    zipCode = models.CharField(max_length=10)
    currentlyOccupied = models.CharField(max_length=10)
    lastSaleDate = models.CharField(max_length=40)
    totalValue = models.CharField(max_length=20)
    owners = models.CharField(max_length=100)
    age = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    phoneNumber = models.CharField(max_length=40)
    phoneType = models.CharField(max_length=40)
    currentResidents = models.CharField(max_length=200)


    def __str__(self):
        return u'%s %s' % (self.streetNum, self.streetName)
