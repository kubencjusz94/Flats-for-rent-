from django.shortcuts import render
from rentals.models import Cities, Flats, Reservations
from django.views import generic
from django.db.models import Q
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
    myform = RentalModelForm(request.GET or None)
    filter = Flats.objects.filter(miasto__nazwa__contains = cityname)
    if 'Submit' in request.GET:
        if myform.is_valid():
            date_of_rent = myform.cleaned_data['data_wynajecia']
            date_of_surrender= myform.cleaned_data['data_oddania']
            myform = RentalModelForm(initial={'data_wynajecia': date_of_rent, 'data_oddania':date_of_surrender})
            filter = Flats.objects.filter(miasto__nazwa__contains=cityname).filter((Q(reservations__data_wynajecia__gt = date_of_rent) & Q(reservations__data_wynajecia__gt = date_of_surrender)) | (Q(reservations__data_wynajecia__lt = date_of_rent) & Q(reservations__data_oddania__lt = date_of_surrender)) | (Q(reservations__data_wynajecia = None)))
    context = {
        'form': myform,
        'cityname': cityname,
        'filter': filter,
    }
    return render(request, 'rentals/searching_panel.html',context)
