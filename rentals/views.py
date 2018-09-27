from django.shortcuts import render
from rentals.models import Cities, Flats
from django.views import generic

import datetime
from django.http import HttpResponse
from django.urls import reverse
from rentals.forms import RentalModelForm

def index(request):
    available_flats = Flats.objects.filter(status='d').count()
    context = {
        'available_flats': available_flats,
    }
    return render(request, 'index.html', context=context)

def get_flats_count(request):
    available_flats_gda = Cities.objects.filter(nazwa='Gdańsk',flats__status__contains='d').count()
    available_flats_gdy = Cities.objects.filter(nazwa='Gdynia',flats__status__contains='d').count()
    available_flats_sop = Cities.objects.filter(nazwa='Sopot',flats__status__contains='d').count()
    context = {
        'available_flats_gda': available_flats_gda,
        'available_flats_gdy': available_flats_gdy,
        'available_flats_sop': available_flats_sop,
    }
    return render(request, 'rentals/city_panels.html', context)

def search(request, cityname):
    selected_city = Cities.objects.get(nazwa=cityname)
    #'miasto' is ForeignKey for Flats, so I need to 'filter' it by Cities (second table)
    myform = RentalModelForm(request.GET or None, initial={'miasto':selected_city})
    if 'Submit' in request.GET:
        if myform.is_valid():
            cityname = myform.cleaned_data['miasto']
            date_of_rent = myform.cleaned_data['data_wynajecia']
            date_of_surrender= myform.cleaned_data['data_oddania']
        myform = RentalModelForm(initial={'miasto':selected_city, 'data_wynajecia': date_of_rent, 'data_oddania':date_of_surrender})
    cityname_filter = Flats.objects.filter(miasto__nazwa__contains=cityname)
    context = {
        'form': myform,
        'cityname': cityname,
        'cityname_filter': cityname_filter,
    }
    return render(request, 'rentals/searching_panel.html',context)
