from django.urls import path
from AppAero import views

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('pasajeros', views.pasajero, name='pasajero'),
    path('boletos', views.boleto, name='boleto'),
    path('azafatas', views.azafatas, name='azafatas'),
    path('pilotos', views.piloto, name='piloto'),

]
