from django.forms import ModelForm, Select, TextInput, DateInput
from rentals.models import Flats

class RentalModelForm(ModelForm):
    class Meta:
        model =  Flats
        fields = ['data_wynajecia', 'data_oddania']
        #Specify fields manually by widgets to fit their format to BootStrap Datepicker and give some css attr's
        widgets = {
            'data_wynajecia': DateInput(attrs = {'type':'text', 'class':'form-control datepicker', 'placeholder':'From...', 'autocomplete':'off'},format = '%m/%d/%Y'),
            'data_oddania': DateInput(attrs = {'type':'text', 'class':'form-control datepicker', 'placeholder':'To...', 'autocomplete':'off'}, format = '%m/%d/%Y')
        }
