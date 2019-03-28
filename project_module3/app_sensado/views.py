from django.shortcuts import render
from .models import Temperatura, Humedad, Gases, Sensores
from django.views.decorators.csrf import csrf_exempt

from datetime import timedelta
from django.utils import timezone
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, "app_sensado/index.html", {})

def main_index(request):
    return render(request, "main_index.html", {})

def accion_raspberry(request):
    import paho.mqtt.publish as publish
    topico = "UIS/LP/213"
    IP_broker = "192.168.0.108"
    usuario_broker = "pi"
    password_broker = "raspberry"
    publish.single(topico, "LED-ON-OFF", port=1883, hostname=IP_broker,
    auth={"username": usuario_broker, "password":password_broker})
    return render(request, "app_sensado/accion_raspberry.html",{"topico": topico})

def presentacion_datos(request):
    hora_actual = timezone.now()
    resultado = {"fecha": hora_actual}
    return render(request, "app_sensado/presentacion_datos.html", resultado)

def historico_datos(request):
    """ para presentar todos los datos almacenados
    en la base de datos"""
    resultado = {}
    return render(request, "app_sensado/historico_datos.html", resultado)

def historico_datos_json(request):
    temp = Temperatura.objects.all()
    temperatura = temp.values("valor_temperatura", "fecha")
    temperatura = list(map(lambda datos: [datos["fecha"].timestamp(), datos["valor_temperatura"]], temperatura))
    del(temp)

    gases = Sensores.objects.filter(nombre_sensor="MQ135")
    id_MQ135 = gases.values("id")
    id_MQ135 = list(map(lambda datos: datos["id"] ,id_MQ135))
    print(id_MQ135)

    gases = Sensores.objects.filter(nombre_sensor="MQ137")
    id_MQ137 = gases.values("id")
    id_MQ137 = list(map(lambda datos: datos["id"] ,id_MQ137))
    print(id_MQ137)

    gases = Sensores.objects.filter(nombre_sensor="MQ3")
    id_MQ3 = gases.values("id")
    id_MQ3 = list(map(lambda datos: datos["id"] ,id_MQ3))
    print(id_MQ3)

    hum = Humedad.objects.all()
    humedad = hum.values("valor_humedad", "fecha")
    humedad = list(map(lambda datos: [datos["fecha"].timestamp(), datos["valor_humedad"]], humedad))
    del(hum)

    gas_amoniaco = Gases.objects.filter(sensor_id__in=id_MQ135)
    amoniaco = gas_amoniaco.values("valor", "fecha")
    amoniaco = list(map(lambda datos: [datos["fecha"].timestamp(), datos["valor"]], amoniaco))
    del(gas_amoniaco)

    gas_CO = Gases.objects.filter(sensor_id__in=id_MQ137)
    CO = gas_CO.values("valor", "fecha")
    CO = list(map(lambda datos: [datos["fecha"].timestamp(), datos["valor"]], CO))
    del(gas_CO)

    gas_alcohol = Gases.objects.filter(sensor_id__in=id_MQ3)
    alcohol = gas_alcohol.values("valor", "fecha")
    alcohol = list(map(lambda datos: [datos["fecha"].timestamp(), datos["valor"]], alcohol))
    del(gas_alcohol)
    resultado = {"temperatura": temperatura,
                     "humedad": humedad,
                     "amoniaco": amoniaco,
                     "CO": CO,
                     "alcohol": alcohol}
    return JsonResponse(resultado)

@csrf_exempt # a)
def presentacion_datos_json(request):
    if request.method == "POST":
        # b) lectura de los datos del cliente y configuracion hora
        hora_actual = timezone.now()
        dato_cliente = request.POST
        print(dato_cliente)
        hora_pasada = hora_actual-timedelta(hours=int(dato_cliente['hora']))

        # c) consulta de la base de datos de los modelos Temperatura, Humedad y Gases
        temp = Temperatura.objects.filter(fecha__range=(hora_pasada, hora_actual))
        temperatura = temp.values("valor_temperatura", "fecha")
        temperatura = list(map(lambda datos: [datos["fecha"].timestamp(), datos["valor_temperatura"]], temperatura))
        del(temp)

        hum = Humedad.objects.filter(fecha__range=(hora_pasada, hora_actual))
        humedad = hum.values("valor_humedad", "fecha")
        humedad = list(map(lambda datos: [datos["fecha"].timestamp(), datos["valor_humedad"]], humedad))
        del(hum)

        gas_amoniaco = Gases.objects.filter(fecha__range=(hora_pasada, hora_actual), sensor_id = 7)
        amoniaco = gas_amoniaco.values("valor", "fecha")
        amoniaco = list(map(lambda datos: [datos["fecha"].timestamp(), datos["valor"]], amoniaco))
        del(gas_amoniaco)

        gas_CO = Gases.objects.filter(fecha__range=(hora_pasada, hora_actual), sensor_id = 8)
        CO = gas_CO.values("valor", "fecha")
        CO = list(map(lambda datos: [datos["fecha"].timestamp(), datos["valor"]], CO))
        del(gas_CO)

        gas_alcohol = Gases.objects.filter(fecha__range=(hora_pasada, hora_actual), sensor_id = 9)
        alcohol = gas_alcohol.values("valor", "fecha")
        alcohol = list(map(lambda datos: [datos["fecha"].timestamp(), datos["valor"]], alcohol))
        del(gas_alcohol)

        resultado = {"temperatura": temperatura, 
                     "fecha":hora_actual,
                     "humedad": humedad,
                     "amoniaco": amoniaco,
                     "CO": CO,
                     "alcohol": alcohol}
    else:
        resultado = {}
    return JsonResponse(resultado)