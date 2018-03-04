from django.conf.urls import url

# from . import views
from .views import *

urlpatterns = [
    url(r'^$', WSdatabase),
    url(r'^propertyInfo/(?P<caseNum>[\d]+\-?[\d]+)/$', propertyInfo),
]
# url(r'^$', views.WSdatabase, name='WSdatabase'),
# url(r'propertyInfo', views.propertyInfo, name='propertyInfo'),
