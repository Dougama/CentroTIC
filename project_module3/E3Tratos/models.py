from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.
class Variables(models.Model):
    """
    Esta clase hace referencia a las variables guardadas en JSON
    """
    variables = JSONField()
    fecha = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)



