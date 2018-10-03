from django.contrib import admin
from rentals.models import Cities, Flats, Reservations

class CitiesAdmin(admin.ModelAdmin):
    display = ('nazwa')
admin.site.register(Cities, CitiesAdmin)

class FlatsAdmin(admin.ModelAdmin):
    list_display = ('miasto', 'adres' , 'status')
    actions=['change_to_disable', 'change_to_available']

    def change_to_disable(self, request, queryset):
        queryset.update(status='n')
    change_to_disable.short_description='Change flat status to disable'

    def change_to_available(self, request, queryset):
        queryset.update(status='d')
    change_to_available.short_description='Change flat status to available'
admin.site.register(Flats, FlatsAdmin)

class ReservationsAdmin(admin.ModelAdmin):
    list_display=('id', 'mieszkanie', 'telefon', 'data_wynajecia', 'data_oddania')
admin.site.register(Reservations, ReservationsAdmin)
