from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.WSdatabase, name='WSdatabase'),
]
# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]
