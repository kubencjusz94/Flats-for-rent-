import datetime
from django.forms import ModelForm, TextInput, DateInput
from rentals.models import Reservations
from django.core.exceptions import ValidationError, MultipleObjectsReturned
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q

class SearchModelForm(ModelForm):
    class Meta:
        model =  Reservations
        fields = ['data_wynajecia', 'data_oddania']
        #Specify fields manually by widgets to fit their format to BootStrap Datepicker and give some css attr's
        widgets = {
            'data_wynajecia': DateInput(attrs = {'type':'text', 'class':'form-control datepicker', 'placeholder':'Data wynajęcia', 'autocomplete':'off'},format = '%Y-%m-%d'),
            'data_oddania': DateInput(attrs = {'type':'text', 'class':'form-control datepicker', 'placeholder':'Data oddania', 'autocomplete':'off'}, format = '%Y-%m-%d')
        }
    def clean(self):
        cleaned_data = super(SearchModelForm, self).clean()

        date_of_rent = cleaned_data.get('data_wynajecia')
        date_of_surrender = cleaned_data.get('data_oddania')

        if (date_of_rent or date_of_surrender)  == None:
            raise ValidationError(_('Invalid date - dates required'), code = 'invalid')
        if (date_of_rent or date_of_surrender)  < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'), code = 'invalid')
        if date_of_rent > date_of_surrender:
            raise ValidationError(_('Invalid date - date of rent must be lower'), code = 'invalid')
        return cleaned_data

class ReserveModelForm(ModelForm):
    class Meta:
        model = Reservations
        fields = ['nazwisko', 'telefon', 'data_wynajecia', 'data_oddania']
        widgets = {
            'nazwisko': TextInput(attrs = {'type':'text', 'class':'form-control', 'placeholder':'Lastname'}),
            'telefon': TextInput(attrs = {'type':'text', 'class':'form-control', 'placeholder':'Phone (optional)'}),
            'data_wynajecia': DateInput(attrs = {'type':'text', 'class':'form-control datepicker', 'placeholder':'From...', 'autocomplete':'off'},format = '%Y-%m-%d'),
            'data_oddania': DateInput(attrs = {'type':'text', 'class':'form-control datepicker', 'placeholder':'To..', 'autocomplete':'off'}, format = '%Y-%m-%d')
        }
    def clean(self):
        cleaned_data = super(ReserveModelForm, self).clean()

        date_of_rent = cleaned_data.get('data_wynajecia')
        date_of_surrender = cleaned_data.get('data_oddania')

        if (date_of_rent or date_of_surrender)  == None:
            raise ValidationError(_('Invalid date - dates required'), code = 'invalid')
        if (date_of_rent or date_of_surrender)  < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'), code = 'invalid')
        if date_of_rent > date_of_surrender:
            raise ValidationError(_('Invalid date - date of rent must be lower'), code =' invalid')
        try:
            filter =Reservations.objects.get(Q(data_wynajecia__range = [date_of_rent, date_of_surrender]) | Q(data_oddania__range = [date_of_rent, date_of_surrender]) | Q(data_wynajecia__lt = date_of_rent, data_oddania__gt = date_of_surrender))
            raise ValidationError(_('This appartment is busy at this time'), code =' invalid')
        except Reservations.DoesNotExist:
            pass
        except MultipleObjectsReturned:
            raise ValidationError(_('This appartment is busy at this time'), code =' invalid')
        return cleaned_data
