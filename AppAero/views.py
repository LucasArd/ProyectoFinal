
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

def inicio (request):
    return render(request, "AppAero/inicio.html")

def pasajero (request):
    return render(request, "AppAero/pasajeros.html")

def azafatas (request):
    return render(request, "AppAero/azafatas.html")

def piloto (request):
    return render(request, "AppAero/pilotos.html")

def boleto (request):
    return render(request, "AppAero/boletos.html")
