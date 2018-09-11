from django.shortcuts import render
from rentals.models import Cities, Flats

def index(request):
    all_flats=Flats.objects.all().count();

    context = {
        'all_flats': all_flats,
    }

    return render(request, 'index.html', context=context)
