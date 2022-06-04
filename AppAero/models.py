from django.db import models

class pasajero(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)

class azafatas(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    legajo = models.IntegerField()

class piloto(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    horasDeVuelo = models.IntegerField()

class boleto(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    numeroDeVuelo = models.IntegerField()
