from django.urls import path
from rentals import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('rental_form/', views.rental_form, name='rental_form'),
    path('rental_form/flats_list/', views.search, name='flats_list'),
]
