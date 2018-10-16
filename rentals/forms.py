import datetime
from django.forms import ModelForm, TextInput, DateInput, HiddenInput, RegexField
from rentals.models import Reservations
from django.core.exceptions import ValidationError, MultipleObjectsReturned
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from django.core.validators import RegexValidator

class SearchModelForm(ModelForm):
    class Meta:
        model =  Reservations
        fields = ['date_of_rent', 'date_of_surrender']
        #Specify fields manually by widgets to fit their format to BootStrap Datepicker and give some css attr's
        widgets = {
            'date_of_rent': DateInput(attrs = {'type':'text', 'class':'form-control datepicker', 'placeholder':'From...', 'autocomplete':'off'},format = '%Y-%m-%d'),
            'date_of_surrender': DateInput(attrs = {'type':'text', 'class':'form-control datepicker', 'placeholder':'To...', 'autocomplete':'off'}, format = '%Y-%m-%d')
        }
    def clean(self):
        cleaned_data = super(SearchModelForm, self).clean()

        form_date_of_rent = cleaned_data.get('date_of_rent')
        form_date_of_surrender = cleaned_data.get('date_of_surrender')

        if (form_date_of_rent or form_date_of_surrender)  == None:
            raise ValidationError(_('Invalid date - dates required'), code = 'invalid')
        if (form_date_of_rent or form_date_of_surrender)  < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'), code = 'invalid')
        if form_date_of_rent > form_date_of_surrender:
            raise ValidationError(_('Invalid date - date of rent must be lower'), code = 'invalid')
        return cleaned_data

class ReserveModelForm(ModelForm):
    class Meta:
        model = Reservations
        fields = ['lastname', 'phone_number', 'date_of_rent', 'date_of_surrender', 'flat']
        widgets = {
            'lastname': TextInput(attrs = {'type':'text', 'class':'form-control', 'placeholder':'Lastname'}),
            'phone_number': TextInput(attrs = {'type':'text', 'class':'form-control', 'placeholder':'Phone number'}),
            'date_of_rent': DateInput(attrs = {'type':'text', 'class':'form-control detail-datepicker', 'placeholder':'From...', 'autocomplete':'off'},format = '%Y-%m-%d'),
            'date_of_surrender': DateInput(attrs = {'type':'text', 'class':'form-control detail-datepicker', 'placeholder':'To..', 'autocomplete':'off'}, format = '%Y-%m-%d'),
            'flat': HiddenInput()
        }
    def clean(self):
        cleaned_data = super(ReserveModelForm, self).clean()

        form_date_of_rent = cleaned_data.get('date_of_rent')
        form_date_of_surrender = cleaned_data.get('date_of_surrender')
        form_flat = cleaned_data.get('flat')
        form_phone_number = cleaned_data.get('phone_number')
        phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'")
        phone_regex(form_phone_number)

        if (form_date_of_rent or form_date_of_surrender)  == None:
            raise ValidationError(_('Invalid date - dates required'), code = 'invalid')
        if (form_date_of_rent or form_date_of_surrender)  < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'), code = 'invalid')
        if form_date_of_rent > form_date_of_surrender:
            raise ValidationError(_('Invalid date - date of rent must be lower'), code =' invalid')
        if form_phone_number == None:
            raise ValidationError(_('Invalid date - renewal in past'), code = 'invalid')

        try:
            filter = Reservations.objects.get(Q(flat = form_flat) & (Q(date_of_rent__range = [form_date_of_rent, form_date_of_surrender]) | Q(date_of_surrender__range = [form_date_of_rent, form_date_of_surrender]) | Q(date_of_rent__lt = form_date_of_rent, date_of_surrender__gt = form_date_of_surrender)))
            raise ValidationError(_('That appartment is busy at this time'), code =' invalid')
        except Reservations.DoesNotExist:
            pass
        except MultipleObjectsReturned:
            raise ValidationError(_('That appartment is busy at this time'), code =' invalid')

        return cleaned_data
