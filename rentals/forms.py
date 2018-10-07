import datetime
from django.forms import ModelForm, Select, TextInput, DateInput
from rentals.models import Reservations
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class RentalModelForm(ModelForm):

    class Meta:
        model =  Reservations
        fields = ['data_wynajecia', 'data_oddania']
        #Specify fields manually by widgets to fit their format to BootStrap Datepicker and give some css attr's
        widgets = {
            'data_wynajecia': DateInput(attrs = {'type':'text', 'class':'form-control datepicker', 'placeholder':'From...', 'autocomplete':'off'},format = '%Y-%m-%d'),
            'data_oddania': DateInput(attrs = {'type':'text', 'class':'form-control datepicker', 'placeholder':'To...', 'autocomplete':'off'}, format = '%Y-%m-%d')
        }
    def clean(self):
        cleaned_data = super(RentalModelForm, self).clean()
        date_of_rent = cleaned_data.get('data_wynajecia')
        date_of_surrender = cleaned_data.get('data_oddania')
        if date_of_rent == None:
            raise ValidationError(_('Invalid date - date of rent is required'))
        if date_of_surrender == None:
            raise ValidationError(_('Invalid date - date of surrender is required'))
        if date_of_rent < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        if date_of_surrender < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        if date_of_rent > date_of_surrender:
            raise ValidationError(_('Invalid date - date of rent must be lower'))
        if date_of_surrender < date_of_rent:
            raise ValidationError(_('Invalid date - date of surrender must be greater'))
        return cleaned_data
