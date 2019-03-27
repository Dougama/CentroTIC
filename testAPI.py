import requests
import requests.auth 
import datetime

fecha = datetime.datetime.now()
valor = 20
pyload = {
    "fecha": fecha,
    "valor": valor,
    "sensor": 1
}

# para obtener el token de un usuario se realiza lo siguiente
data = {"username": "luismiguel", "password": "1uis2016"}

r = requests.post("http://127.0.0.1:8000/app_praes/login/", data=data)
print("token del usuario luismiguel {}" .format(r.text))

# para guardar un dato por usuario se requiere un token, por ejemplo: para el usuario: luismiguel
# se obtuvo el siguiente Token 1b6c7a70e04dc71259197a359ba947bc8cc41271
r = requests.post("http://127.0.0.1:8000/app_praes/temperatura/", data=pyload, headers={"Authorization": " Token 1b6c7a70e04dc71259197a359ba947bc8cc41271"})


