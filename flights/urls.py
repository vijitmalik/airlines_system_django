from django.contrib import admin
from django.urls import include,path
from . import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('flights', views.FlightViewSet)
router = routers.DefaultRouter()
router.register('airport', views.AirportViewSet)

app_name="flights"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name ="book"),
    # path("flightapi", include(router.urls)),
    # path("api-auth/", include('rest_framework.urls',
    #     namespace = 'rest_framework'))
    path("airportapi", include(router.urls)),
    path("api-auth/", include('rest_framework.urls',
        namespace = 'rest_framework'))
    ]