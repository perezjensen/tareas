
from django.urls import path
from historial import views



urlpatterns = [
    path('historial/',views.get_history, name="verHistorial"),

]
