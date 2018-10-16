from django.shortcuts import render
from rentals.models import City, Flat, Reservations
from django.views import generic
from django.db.models import Q
import datetime
from django.http import HttpResponse
from django.urls import reverse
from rentals.forms import SearchModelForm, ReserveModelForm
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    available_flats = Flat.objects.filter(status='a').count()
    context = {
        'available_flats': available_flats,
    }
    return render(request, 'index.html', context=context)

def get_flats_count(request):
    available_flats_gda = City.objects.filter(name='Gdańsk',flat__status__contains='a').count()
    available_flats_gdy = City.objects.filter(name='Gdynia',flat__status__contains='a').count()
    available_flats_sop = City.objects.filter(name='Sopot',flat__status__contains='a').count()
    context = {
        'available_flats_gda': available_flats_gda,
        'available_flats_gdy': available_flats_gdy,
        'available_flats_sop': available_flats_sop,
    }
    return render(request, 'rentals/city_panels.html', context)

def search(request, cityname):
    myform = SearchModelForm(request.GET or None)
    filter = Flat.objects.filter(city__name__contains = cityname)
    if 'Submit' in request.GET:
        if myform.is_valid():
            buff_date_of_rent = myform.cleaned_data['date_of_rent']
            buff_date_of_surrender = myform.cleaned_data['date_of_surrender']
            myform = SearchModelForm(initial={'date_of_rent': buff_date_of_rent, 'date_of_surrender':buff_date_of_surrender})
            filter = Flat.objects.filter(city__name__contains = cityname).exclude(Q(reservations__date_of_rent__range = [buff_date_of_rent,buff_date_of_surrender]) | Q(reservations__date_of_surrender__range = [buff_date_of_rent,buff_date_of_surrender]))
    context = {
        'form': myform,
        'cityname': cityname,
        'filter': filter,
    }
    return render(request, 'rentals/searching_panel.html', context)

class FlatDetailView(generic.DetailView):
    model = Flat
    form_class = ReserveModelForm
    template_name = 'rentals/flat_detail.html'

    def post(self, request, pk):
        self.object = self.get_object()
        myform = self.form_class(request.POST)
        if myform.is_valid():
            validation = True
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
            'flat': self.object,
            'validation': validation,
            'mess': mess,
        }
        return render(request, self.template_name, context)

    def get(self, request, pk):
        self.object = self.get_object()
        myform = self.form_class()
        myform.fields['flat'].initial = self.object
        return render(request, self.template_name, {'form': myform, 'flat':self.object})
