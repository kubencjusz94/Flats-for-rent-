from django.urls import path
from rentals import views

urlpatterns = [
    path('', views.index, name='index'),
    path('flats_list/',views.FlatsListView.as_view(), name='flats'),
]
