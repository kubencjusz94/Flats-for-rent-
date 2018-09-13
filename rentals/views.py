from django.shortcuts import render
from rentals.models import Cities, Flats
from django.views import generic

def index(request):
    available_flats_gda = Cities.objects.filter(nazwa='Gdańsk',flats__status__contains='d').count();
    available_flats_gdy = Cities.objects.filter(nazwa='Gdynia',flats__status__contains='d').count();
    available_flats_sop = Cities.objects.filter(nazwa='Sopot',flats__status__contains='d').count();
    context = {
        'available_flats_gda': available_flats_gda,
        'available_flats_gdy': available_flats_gdy,
        'available_flats_sop': available_flats_sop,
    }

    return render(request, 'index.html', context=context)

class FlatsListView(generic.ListView):
    model = Flats

    def get_queryset(self):
        return Flats.objects.filter(miasto__nazwa__contains='Gdańsk');
