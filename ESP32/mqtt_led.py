from machine import Pin
import machine
import time
from  umqtt.simple import MQTTClient
import ubinascii
import micropython


def sub_cb(topic, msg):
    
    if msg == b"ESP32-LED":
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


    