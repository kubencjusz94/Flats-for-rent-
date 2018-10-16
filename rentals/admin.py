from django.contrib import admin
from rentals.models import City, Flat, Reservations

class CityAdmin(admin.ModelAdmin):
    display = ('name')
admin.site.register(City, CityAdmin)

class ReservationsInline(admin.TabularInline):
    model = Reservations
    extra = 0

class FlatAdmin(admin.ModelAdmin):
    list_display = ('adress', 'city' , 'status')
    actions = ['change_to_unavailable', 'change_to_available']
    inlines = [ReservationsInline]

    def change_to_unavailable(self, request, queryset):
        queryset.update(status='u')
    change_to_unavailable.short_description='Change status to unavailable'

    def change_to_available(self, request, queryset):
        queryset.update(status='a')
    change_to_available.short_description='Change status to available'
admin.site.register(Flat, FlatAdmin)

class ReservationsAdmin(admin.ModelAdmin):
    list_display=('id', 'flat', 'phone_number', 'date_of_rent', 'date_of_surrender')
admin.site.register(Reservations, ReservationsAdmin)
