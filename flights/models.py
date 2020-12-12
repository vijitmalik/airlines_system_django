from django.db import models


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    def __str__(self):
        return f" {self.city}({self.code}) "


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete= models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete= models.CASCADE, related_name= 'arrivals')
    duration = models.IntegerField()
    def __str__(self):
        return f"{self.id}: From {self.origin} to {self.destination}"

class Passenger(models.Model):
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    