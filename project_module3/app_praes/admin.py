from django.contrib import admin
from .models import Departamento, Ciudad, Kit, Colegio, Sensores, Semillero, Temperatura
# Register your models here.

admin.site.register(Departamento)
admin.site.register(Ciudad)
admin.site.register(Kit)
admin.site.register(Colegio)
admin.site.register(Semillero)
admin.site.register(Sensores)
admin.site.register(Temperatura)
