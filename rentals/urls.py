from django.urls import path
from rentals import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rental_form/', views.rental_flats, name='rental_form'),
    path('flats_list/', views.FlatsListView.as_view(), name='flats'),
]
