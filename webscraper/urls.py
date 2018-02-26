from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.WSdatabase, name='WSdatabase'),
    url(r'propertyInfo',views.propertyInfo, name='propertyInfo'),
]
