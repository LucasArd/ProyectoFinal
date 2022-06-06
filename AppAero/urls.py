from django.urls import path
from AppAero import views

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('pasajeros', views.pasajero, name='pasajero'),
    path('boletos', views.boleto, name='boleto'),
    path('azafatas', views.azafatas, name='azafatas'),
    path('pilotos', views.piloto, name='piloto'),
    path('pasajerosformulario', views.PasajerosFormulario, name='pasajerosformulario'),
    path('azafatasformulario', views.AzafatasFormulario, name='azafatasformulario'),
    path('boletosformulario', views.BoletosFormulario, name='boletosformulario'),
    path('pilotosformulario', views.PilotosFormulario, name = 'pilotosformulario'),


]
