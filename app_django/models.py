from django.db import models


class OtroModelo(models.Model):
    atributo = models.CharField(max_length=50)


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    correo = models.EmailField()

    def __str__(self):
        return self.nombre


# Create your models here.
