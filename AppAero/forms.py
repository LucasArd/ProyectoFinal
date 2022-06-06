from tkinter.tix import Form
from django import forms

class Pilotosformulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    horasDeVuelo = forms.IntegerField()

class Pasajerosformulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    
class Boletosformulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    numeroDeVuelo = forms.IntegerField()

class Azafatasformulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    legajo = forms.IntegerField()

