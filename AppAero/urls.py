from django.urls import path
from AppAero import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pasajerosformulario', views.PasajerosFormulario, name='pasajerosformulario'),
    path('azafatasformulario', views.AzafatasFormulario, name='azafatasformulario'),
    path('boletosformulario', views.BoletosFormulario, name='boletosformulario'),
    path('pilotosformulario', views.PilotosFormulario, name = 'pilotosformulario'),
    path('buscar/', views.Buscar, name = 'buscar'),
    path('busquedaapellido', views.BusquedaApellido, name = 'busquedaapellido'),

]