from django.shortcuts import render
from rentals.models import Cities, Flats, Reservations
from django.views import generic
from django.db.models import Q
import datetime
from django.http import HttpResponse
from django.urls import reverse
from rentals.forms import SearchModelForm, ReserveModelForm
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

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
    myform = SearchModelForm(request.GET or None)
    filter = Flats.objects.filter(miasto__nazwa__contains = cityname)
    if 'Submit' in request.GET:
        if myform.is_valid():
            date_of_rent = myform.cleaned_data['data_wynajecia']
            date_of_surrender = myform.cleaned_data['data_oddania']
            myform = SearchModelForm(initial={'data_wynajecia': date_of_rent, 'data_oddania':date_of_surrender})
            filter = Flats.objects.filter(miasto__nazwa__contains = cityname).exclude(Q(reservations__data_wynajecia__range = [date_of_rent,date_of_surrender]) | Q(reservations__data_oddania__range = [date_of_rent,date_of_surrender]))
    context = {
        'form': myform,
        'cityname': cityname,
        'filter': filter,
    }
    return render(request, 'rentals/searching_panel.html', context)

class FlatsDetailView(generic.DetailView):
    model = Flats
    form_class = ReserveModelForm
    template_name = 'rentals/flats_detail.html'

    def post(self, request, pk):
        self.object = self.get_object()
        myform = self.form_class(request.POST)
        if myform.is_valid():
            validation = True
            last_name = myform.cleaned_data['nazwisko']
            tel_number = myform.cleaned_data['telefon']
            date_of_rent = myform.cleaned_data['data_wynajecia']
            date_of_surrender = myform.cleaned_data['data_oddania']
            new_reservation = myform.save(commit = False)
            new_reservation.mieszkanie = self.object
            new_reservation.save()
            myform.save_m2m()
            mess = 'Reservation successfully!'
        else:
            validation = False
            mess = 'Form is valid, try again'
        context = {
            'form': myform,
            'flats': self.object,
            'validation': validation,
            'mess': mess,
        }
        return render(request, self.template_name, context)

    def get(self, request, pk):
        self.object = self.get_object()
        myform = self.form_class()
        myform.fields['mieszkanie'].initial = self.object
        return render(request, self.template_name, {'form': myform, 'flats':self.object})
