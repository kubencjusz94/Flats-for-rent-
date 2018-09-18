from django.shortcuts import render
from rentals.models import Cities, Flats
from django.views import generic

import datetime
from django.http import HttpResponse
from django.urls import reverse
from rentals.forms import RentalForm

def index(request):
    available_flats = Flats.objects.filter(status='d').count()
    context = {
        'available_flats': available_flats,
    }
    return render(request, 'index.html', context=context)

def rental_form(request):
    available_flats_gda = Cities.objects.filter(nazwa='Gdańsk',flats__status__contains='d').count()
    available_flats_gdy = Cities.objects.filter(nazwa='Gdynia',flats__status__contains='d').count()
    available_flats_sop = Cities.objects.filter(nazwa='Sopot',flats__status__contains='d').count()
    context = {
        'available_flats_gda': available_flats_gda,
        'available_flats_gdy': available_flats_gdy,
        'available_flats_sop': available_flats_sop,
    }
    return render(request, 'rentals/rental_form.html', context)

def search(request):
    if request.method == 'POST':
        return HttpResponse("Hello POST method")
    else:
        cityname = request.GET['city-name']

    cityname_filter =  Flats.objects.filter(miasto__nazwa__contains=cityname);

    context = {
        'cityname' : cityname,
        'cityname_filter': cityname_filter,
    }
    return render(request, 'rentals/flats_list.html',context)
