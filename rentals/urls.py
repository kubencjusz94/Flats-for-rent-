from django.urls import path
from rentals.views import (index, get_flats_count, search)
from django.conf.urls import url

urlpatterns = [
    path('', index, name='index'),
    path('city_panels/', get_flats_count, name='city_panels'),
    path('searching_panel/<cityname>/', search, name='searching_panel')
]
