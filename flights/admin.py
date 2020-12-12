from django.contrib import admin

from .models import Flight, Airport, Passenger

#Customize Admin Interface
class FlightAdmin(admin.ModelAdmin):
    list_display=("id","origin","destination","duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_vertical=("flights",) 

class AirportAdmin(admin.ModelAdmin):
    list_display=("city","code")

# Register your models here.
admin.site.register(Airport, AirportAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
