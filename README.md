# CentroTIC

Este proyecto hace referencia a las aplicaciones de:

* Diplomado IoT
* KIT PRAES
* Protocolo PAWS con SDR
* Nariz Electronica
* Sistemas GRIPV
* E3Tratos

Para lanzar el proyecto se requiere realizar los siguiente:

* Clonar el repositorio: `` git clone https://github.com/LuisDiazM/CentroTIC.git ``
* Crear un entorno virtual con virtualenv `` virtualenv -p python3 env_centrotic ``
* Activar el entorno virtual `` source env_centrotic/bin/activate ``
* (Para desactivar el entorno virtual ``deactivate``)
* Instalar los paquetes pip del archivo requeriments.txt `` pip install -r requeriments.txt``
* Instalar postgresql ``sudo apt-get install postgresql``
* Ingresar al usuario postgres ``sudo su postgres``
* Item Abrir postgres usando ``psql``
* Crear una contraseña al usuario postgres `` \password postgres ``
* Crear una base de datos vacía ``CREATE DATABASE centrotic;``
* Salir ``\q``
* ``exit``
* Realizar las migraciones ``python manage.py makemigrations`` 
* ``python manage.py migrate``
* Lanzar el servidor ``python manage.py runserver``

Ahora puede disfrutar del proyecto de manera local.