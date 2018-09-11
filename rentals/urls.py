from django.urls import path
from rentals import views

urlpatterns = [
    path('', views.index, name='index'),
]
