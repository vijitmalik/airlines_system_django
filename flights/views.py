from django.shortcuts import render
from .models import Flight, Airport,Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets
from . seralizers import AirportSerializer


# class FlightViewSet(viewsets.ModelViewSet):
#     queryset = Flight.objects.all()
#     serializer_class = FlightSerializer
class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer




def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    passengers = flight.passengers.all()
    non_passengers = Passenger.objects.exclude(flights=flight).all()
    return render(request, "flights/flight.html", {
        "flight":flight,
        "passengers": passengers ,
        "non_passengers": non_passengers
    })

def book(request, flight_id):
    if request.method =="POST":
        # we are booking usin flight_id
        flight = Flight.objects.get(pk= flight_id)
        #pass_id from submitted form
        passenger = Passenger.objects.get(pk = int(request.POST["passenger"]))
        #add the new flight to that passernger's flight list
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,) ))