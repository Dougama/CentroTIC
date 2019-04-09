import requests
import requests.auth 
import datetime

fecha = datetime.datetime.now()
valor = 200
pyload = {
    "fecha": fecha,
    "valor": valor,
    "sensor": 1
}

# # para obtener el token de un usuario se realiza lo siguiente
# data = {"username": "luismiguel", "password": "1uis2016"}

# r = requests.post("http://127.0.0.1:8000/app_praes/login/", data=data)
# print("token del usuario luismiguel {}" .format(r.text))

# # para guardar un dato por usuario se requiere un token, por ejemplo: para el usuario: luismiguel
# # se obtuvo el siguiente Token 1b6c7a70e04dc71259197a359ba947bc8cc41271
# r = requests.post("http://127.0.0.1:8000/app_praes/temperatura/", data=pyload, headers={"Authorization": " Token 0da7795909a18584059f0a7714ade7f82ca3256f"})


r = requests.post("http://34.73.25.149/app_praes/temperatura/", data=pyload, headers={"Authorization": " Token d2865cc229825bd3b05d765f11f21b6b80c0fff6"})

print(r.text)
r.close()