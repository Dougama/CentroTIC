from urequests import urequests
import utime 

from machine import Pin
import machine
import time
from  umqtt.simple import MQTTClient
import ubinascii
import micropython

"""
Este archivo contiene las funciones MQTT y enviar a traves de la API
La URL especificada
"""

def enviar_API(url, fecha, valor, sensor):
    """ Esta funcion se encarga de enviar los datos
    a la API para que sean almacenados en la base de datos
    de acuerdo a la url especificada.
    """
    date = str(fecha[0])+"-"+str(fecha[1])+"-"+str(fecha[2])+" "+str(fecha[3])+":"+str(fecha[4])+":"+str(fecha[5])
    pyload = {
        "fecha": date,
        "valor": valor,
        "sensor": sensor
    }
    r = urequests.post(url, json=pyload, headers={"Authorization": " Token d2865cc229825bd3b05d765f11f21b6b80c0fff6"})
    print(r.content)
    print(r.status_code)
    r.close()
    # podria retornarse el status HTTP para indicar a un led que todo esta  bien

def sub_cb(topic, msg):
    """ Esta es la funcion que se encarga de interpretar todas las 
    acciones enviadas por MQTT, es decir, el menu dado por 
    Control KIT ambiental
    """
    if msg == b"ESP32-LED":

        #envio de datos a la API
        fecha = utime.localtime()
        url = "http://34.73.25.149/app_praes/temperatura/"
        sensor = 1
        valor = 1000
        enviar_API(url, fecha, valor, sensor)

        #encender led para indicar que la comunicacion ha sido correcta        
        p22 = Pin(22, Pin.OUT)   
        p2 = Pin(2, Pin.OUT)
        for i in range(10):
            p22.on()  
            time.sleep(200e-3)
            p22.off()
            time.sleep(200e-3)

                
# Default MQTT server to connect to
SERVER = "34.73.25.149"
TOPIC = b"UIS/LP/213"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
print("client id {}".format(CLIENT_ID))
client = MQTTClient(client_id=CLIENT_ID, server=SERVER, port=1883, user="pi", password="raspberry")
client.set_callback(sub_cb)
client.connect()
client.subscribe(TOPIC)
print("suscripcion exitosa")
try: 
    while True:
        micropython.mem_info()
        client.wait_msg()
finally:
    client.disconnect()



