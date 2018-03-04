from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', WSdatabase),
    url(r'^propertyInfo/(?P<caseNum>[\d]+\-?[\d]+)/$', propertyInfo),
]
