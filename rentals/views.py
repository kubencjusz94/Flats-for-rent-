from django.shortcuts import render
from rentals.models import Cities, Flats
from django.views import generic

import datetime
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from rentals.forms import RentalForm

def index(request):
    available_flats = Flats.objects.filter(status='d').count()
    context = {
        'available_flats': available_flats,
    }
    return render(request, 'index.html', context=context)

def rental_flats(request):
    available_flats_gda = Cities.objects.filter(nazwa='Gdańsk',flats__status__contains='d').count()
    available_flats_gdy = Cities.objects.filter(nazwa='Gdynia',flats__status__contains='d').count()
    available_flats_sop = Cities.objects.filter(nazwa='Sopot',flats__status__contains='d').count()
    context = {
        'available_flats_gda': available_flats_gda,
        'available_flats_gdy': available_flats_gdy,
        'available_flats_sop': available_flats_sop,
    }
    return render(request, 'rentals/rental_form.html', context)

class FlatsListView(generic.ListView):
    model = Flats
    def get_queryset(self):
        return Flats.objects.filter(miasto__nazwa__contains='Gdańsk');
