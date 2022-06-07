
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Pasajero, Piloto, Boleto, Azafatas
from AppAero.forms import  Pasajerosformulario, Pilotosformulario, Boletosformulario, Azafatasformulario

def inicio (request):
    return render(request, "AppAero/inicio.html")

def PasajerosFormulario (request):
    if request.method == 'POST':

        miFormulario = Pasajerosformulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            nombre= informacion['nombre']
            apellido= informacion['apellido']

            pasajero = Pasajero(nombre = nombre, apellido= apellido)

            pasajero.save()

            return render(request, "AppAero/inicio.html")
    else:
        miFormulario = Pasajerosformulario()
    return render(request, "AppAero/pasajerosformulario.html", {"miFormulario":miFormulario})

def AzafatasFormulario (request):
    if request.method == 'POST':

        miFormulario = Azafatasformulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            nombre= informacion['nombre']
            apellido= informacion['apellido']
            legajo = informacion['legajo']

            azafata = Azafatas(nombre = nombre, apellido= apellido, legajo= legajo)

            azafata.save()

            return render(request, "AppAero/inicio.html")
    else:
        miFormulario = Azafatasformulario()
    return render(request, "AppAero/azafatasformulario.html", {"miFormulario":miFormulario})

def BoletosFormulario (request):
    if request.method == 'POST':

        miFormulario = Boletosformulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            nombre= informacion['nombre']
            apellido= informacion['apellido']
            numeroDeVuelo = informacion['numeroDeVuelo']

            boletos = Boleto(nombre = nombre, apellido= apellido, numeroDeVuelo = numeroDeVuelo)

            boletos.save()

            return render(request, "AppAero/inicio.html")
    else:
        miFormulario = Boletosformulario()
    return render(request, "AppAero/boletosformulario.html", {"miFormulario":miFormulario})

def PilotosFormulario (request):
    if request.method == 'POST':

        miFormulario = Pilotosformulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            nombre= informacion['nombre']
            apellido= informacion['apellido']
            horasDeVuelo = informacion['horasDeVuelo']

            piloto = Piloto(nombre = nombre, apellido= apellido, horasDeVuelo = horasDeVuelo)

            piloto.save()

            return render(request, "AppAero/inicio.html")
    else:
        miFormulario = Pilotosformulario()
    return render(request, "AppAero/pilotosformulario.html", {"miFormulario":miFormulario})


def Buscar (request):
    if request.GET['apellido']:
        apellido = request.GET['apellido']
        pasajeros = Pasajero.objects.filter(apellido__icontains=apellido)
        pilotos = Piloto.objects.filter(apellido__icontains=apellido)
        azafatas = Azafatas.objects.filter(apellido__icontains=apellido)

        return render(request, "AppAero/resultadosbusqueda.html", {"apellido":apellido, "pasajeros":pasajeros, "pilotos":pilotos, "azafatas":azafatas})
    else:
        respuesta = "Los datos no fueron enviados correctamente."
    return HttpResponse(respuesta)

def BusquedaApellido (request):
    return render(request, "AppAero/busquedaApellido.html")