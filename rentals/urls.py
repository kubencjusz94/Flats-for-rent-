from django.urls import path, re_path
from rentals.views import (index, get_flats_count, search, FlatsDetailView)
from django.conf.urls import url

urlpatterns = [
    path('', index, name='index'),
    path('city_panels/', get_flats_count, name='city_panels'),
    path('searching_panel/<cityname>/', search, name='searching_panel'),
    re_path(r'^flat /(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', FlatsDetailView.as_view(), name='flats_detail'),
]
