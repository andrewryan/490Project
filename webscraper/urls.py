from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', database),
    url(r'^propertyInfo/(?P<caseNum>[\d]+\-?[\d]+)/$', propertyInfo),
    url(r'^updateDatabase', updateDatabase),
]
