from urequests import urequests
import utime 
fecha = utime.localtime()
print(fecha)
valor = 200
pyload = {
    "fecha": fecha,
    "valor": valor,
    "sensor": 1
}
r = urequests.post("http://34.73.25.149/app_praes/temperatura/", data=pyload, headers={"Authorization": " Token d2865cc229825bd3b05d765f11f21b6b80c0fff6",'Content-Type': 'application/json'})
print(r.content)
r.close()