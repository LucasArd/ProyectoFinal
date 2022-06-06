from django.db import models

class pasajero(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.nombre + ' ' + self.apellido

class azafatas(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    legajo = models.IntegerField()
    def __str__(self) -> str:
        return self.nombre + ' ' + self.apellido + ' ' + str(self.legajo)


class piloto(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    horasDeVuelo = models.IntegerField()
    def __str__(self) -> str:
        return self.nombre + ' ' + self.apellido + ' ' + str(self.horasDeVuelo)

class boleto(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    numeroDeVuelo = models.IntegerField()
    def __str__(self) -> str:
        return self.nombre + ' ' + self.apellido + ' ' + str(self.numeroDeVuelo)
