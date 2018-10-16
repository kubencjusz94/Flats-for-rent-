from django.urls import path, re_path
from rentals.views import (index, get_flats_count, search, FlatDetailView)
from django.conf.urls import url

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^city_panels/$', get_flats_count, name='city_panels'),
    re_path(r'^searching_panel/(?P<cityname>[-\w]+)$', search, name='searching_panel'),
    re_path(r'^flat /(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', FlatDetailView.as_view(), name='flat_detail'),
]
