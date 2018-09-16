from django import forms
import datetime

class RentalForm(forms.Form):
    rental_date= forms.DateField()
    surrender_date= forms.DateField()
    choosen_city= forms.CharField()

    def clean_rental_date(self):
        data= self.cleaned_data['rental_date']
        #Selected date can't be in the past
        if data < datatime.date.today():
            raise ValidationError(_('Invalid date- you cant rent in the past, Thats not "Back to the Future"'))
        return data
