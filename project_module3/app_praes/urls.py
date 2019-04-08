from django.urls import path 
from rest_framework.authtoken import views
from .apiviews import TemperaturaAPI, HumedadAPI, PresionAtmosfericaAPI, MaterialParticuladoAPI, \
                      NO2API, PolvoAPI, O3API, SO2API, COAPI, CO2API, MetanoPropanoCOAPI, \
                      LuzUVAPI, MaterialOrganicoAPI, CH4API, AnemometroAPI, \
                      CrearUsuarioAPI, LoginView

from rest_framework_swagger.views import get_swagger_view
from .views import index, medicion_actual, monitoreo_lecturas, control_ESP32

app_name = "app_praes"
schema_view = get_swagger_view(title='Temperatura API')

urlpatterns = [
    path('login/', views.obtain_auth_token, name="login"),
    path('usuario/', CrearUsuarioAPI.as_view(), name="crear-usuario"),
    path('docs/', schema_view),
    path('temperatura/', TemperaturaAPI.as_view(), name="praes-temperatura"),
    path('humedad/', HumedadAPI.as_view(), name="praes-humedad"),
    path('presion-atmosferica/', PresionAtmosfericaAPI.as_view(), name="praes-presion-atmosferica"),
    path('material-particulado/', MaterialParticuladoAPI.as_view(), name="praes-material-particulado"),
    path('no2/', NO2API.as_view(), name="praes-no2"),
    path('polvo/', PolvoAPI.as_view(), name="praes-polvo"),
    path('o3/', O3API.as_view(), name="praes-o3"),
    path('so2/', SO2API.as_view(), name="praes-so2"),
    path('co/', COAPI.as_view(), name="praes-co"),
    path('co2/', CO2API.as_view(), name="praes-co2"),
    path('metano-propano-co/', MetanoPropanoCOAPI.as_view(), name="praes-metano-propano-co"),
    path('luz-uv/', LuzUVAPI.as_view(), name="praes-luz-uv"),
    path('material-organico/', MaterialOrganicoAPI.as_view(), name="praes-material-organico"),
    path('ch4/', CH4API.as_view(), name="praes-ch4"),
    path('anemometro/', AnemometroAPI.as_view(), name="praes-anemometro"),
    path('index/', index, name="index-praes"),
    path('medicion_actual/', medicion_actual, name="medicion-actual"),
    path('monitoreo_lecturas/', monitoreo_lecturas, name="monitoreo-lecturas"),
    path('control_kit/', control_ESP32, name="control-kit"),
]