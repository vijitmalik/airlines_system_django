from rest_framework import serializers
from .models import Flight,Passenger,Airport



# class FlightSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Flight
#         fields = ('id','origin', 'destination', 'duration')

class AirportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Airport
        fields = ('id','code', 'city')
