# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Tarjetas(models.Model):
    """Hace referencia a la tabla tarjetas
    """
    nombre_tarjeta = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre_tarjeta

class Sensores(models.Model):
    """Hace referencia a la tabla sensores y
    la clave foranea llama a la clase Tarjetas.
    """
    nombre_sensor = models.CharField(max_length=50)
    tarjeta = models.ForeignKey(Tarjetas, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_sensor

class Temperatura(models.Model):
    """Hace referencia a la tabla temperatura y su 
    clave foranea llama a la clase Sensores.
    """
    valor_temperatura = models.FloatField()
    fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    sensor = models.ForeignKey(Sensores, on_delete=models.CASCADE)

class Humedad(models.Model):
    """Hace referencia a la tabla humedad y su clave foranea llama 
    a la clase Sensores.
    """
    valor_humedad = models.FloatField()
    fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    sensor = models.ForeignKey(Sensores, on_delete=models.CASCADE)

class LecturaTAGSRFID(models.Model):
    """Hace referencia a la tabla lectura_tags_rfid y su clave foranea
    llama a la clase Sensores.
    """
    fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    tag_leido = models.CharField(max_length=50)
    id_tag = models.CharField(max_length=50)
    sensor = models.ForeignKey(Sensores, on_delete=models.CASCADE)

class Gases(models.Model):
    """Hace referencia a la tabla gases, donde mide variables 
    del aire, su clave foranea llama a la clase Sensores.
    """
    fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    valor = models.FloatField()
    sensor = models.ForeignKey(Sensores, on_delete=models.CASCADE)


