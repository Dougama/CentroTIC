import json

class Init():
    def __init__(self):
        pass
    
    def init_request(self):
        """
        Este método se ejecuta en el Master
        """
        INIT_REQUEST = {
        "jsonrpc": "2.0",
        "method": "spectrum.paws.init",
        "params": {
        "type": "INIT_REQ",
        "version": "1.0",
        "deviceDesc": { "serialNumber": "XXX", "fccId": "YYY",
                        "rulesetIds": ["FccTvBandWhiteSpace-2010"]
                        },
        "location": {"point": 
                            { "center": {"latitude": 37.0, "longitude": -101.3}
                            }
                    }
        },
        "id": "xxxxxx"
        }
    
    def init_response(self):
        """
        Este método se ejecuta en la base de datos (servidor web)
        """
        INIT_RESPONSE = {
            "jsonrpc": "2.0",
            "result": {
            "type": "INIT_RESP",
            "version": "1.0",
            "rulesetInfos": [
            {
                "authority": "us",
                "rulesetId": "FccTvBandWhiteSpace-2010",
                "maxLocationChange": 100,
                "maxPollingSecs": 86400
            }
            ]
            },
            "id": "xxxxxx"
        }

class GetSpectrum():
    def __init__(self,):
        pass
    
    def avail_spectrum_request(self):
        """ 
        Este metodo se ejecuta en el USRP-Slave
        """
        AVAIL_SPECTRUM_REQ =  {
        "jsonrpc": "2.0",
        "method": "spectrum.paws.getSpectrum",
        "params": {
        "type": "AVAIL_SPECTRUM_REQ",
        "version": "1.0",
        "deviceDesc": {
        "serialNumber": "XXX",
        "fccId": "YYY",
        "rulesetIds": ["FccTvBandWhiteSpace-2010"]
        },
        "location": {
        "point": {
        "center": {"latitude": 37.0, "longitude": -101.3}
        }
        },
        "antenna": {"height": 10.2, "heightType": "AGL"}
        },
        "id": "xxxxxx"
        }

    def avail_spectrum_response(self):
        """Este metodo se ejecuta en la base de datos (servidor web)
        """
        AVAIL_SPECTRUM_RESPONSE = {
        "jsonrpc": "2.0",
        "result": {
        "type": "AVAIL_SPECTRUM_RESP",
        "version": "1.0",
        "timestamp": "2013-03-02T14:30:21Z",
        "deviceDesc": {
        "serialNumber": "XXX",
        },
        "spectrumSpecs": [
        {
        "rulesetInfo": {
            "authority": "ANE",
        },
        "needsSpectrumReport": False,
        "spectrumSchedules": [
            {
            "eventTime": {
            "startTime": "2013-03-02T14:30:21Z",
            "stopTime": "2013-03-02T20:00:00Z"
            },
            "spectra": [
            {
                "resolutionBwHz": 6e6,
                "profiles": [
                ...
                [
                {"hz":5.18e8, "dbm":30.0},
                {"hz":5.36e8, "dbm":30.0},
                {"hz":5.36e8, "dbm":36.0},
                {"hz":5.42e8, "dbm":36.0}
                ],
                [
                {"hz":6.20e8, "dbm":30.0},
                {"hz":6.26e8, "dbm":30.0}
                ],
                ]
            },
            {
                "resolutionBwHz": 1e5,
                "profiles": [
                [
                {"hz":5.18e8, "dbm":27.0},
                {"hz":5.36e8, "dbm":27.0},
                {"hz":5.36e8, "dbm":30.0},
                {"hz":5.42e8, "dbm":30.0}
                ],
                [
                {"hz":6.20e8, "dbm":27.0},
                {"hz":6.26e8, "dbm":27.0}
                ],
                ]
            }
            ]
            },
            {
            "eventTime": {
            "startTime": "2013-03-02T22:00:00Z",
            "stopTime": "2013-03-03T14:30:21Z"
            },
            "spectra": [
            ]
            }
        ]
        }
        ]
        },
        "id": "xxxxxx"
        }

class Register():
    def __init__(self,):
        pass
    
    def registration_request(self):
        """ Esta informacion la envía el Maestro
        tiene que ser de la misma forma en que se 
        almacena en la base de datos
        """
        REGISTRATION_REQUEST = {
            "deviceDesc": {"DeviceDescriptor Base datos":[]},
            "location": {"Geolocation Base datos":[]},
            "deviceOwner": {"DeviceOwner Base datos":[]},
            "antenna": {"AntennaCharacteristics Base datos": []}
        }
    
    def registration_response():
        """Esta informacion la envia la Base de datos (servidor web)
        """
        REGISTRATION_RESP = {
            "rulsetInfos": ["RuleSetInfo Base datos"],
        }


class VerifyDevice():
    def __init__(self,):
        pass
    
    def dev_valid_req(self):
        """Este metodo lo ejecuta el MAestro
        """
        DEV_VALID_REQ = {
            "deviceDescs": ["DeviceDescriptor Base datos"]
        }

    def dev_valid_response(self):
        """Este método lo ejecuta la base de datos (servidor web)
        """
        DEV_VALID_RESP = {
            "deviceValidities": ["DeviceDescriptor Base datos"],
            "isValid" : True,
            "reason": "este dispositivo ha sido registrado previamente"
        }

class NotifySpectrumUse():

    def __init__(self, ):
        pass
    
    def spectrum_use_notify(self):
        """ Este metodo lo ejecuta el maestro
        en esta ocacion el dispositivo esclavo
        se anticipa a usar el espectro, la validacion
        final la da la base de datos, pero puede ser un posible candidato de 
        uso del espectro, si le involucramos el sensado dentro del dispositivo 
        esclavo"""
        SPECTRUM_USE_NOTIFY = {
            "deviceDesc": ["DeviceDescriptor Base datos"],
            "location" : ["Geolocation Base datos"],
            "spectra": ["Spectrum Base de datos"]
        }

    def spectrum_use_response(self):
        """Este metodo lo ejecuta la base de datos (servidor web) para indicar que 
        la notificacion data por el maestro sigue vigente y puede usar ese espectro,
        en caso de que sea positivo debe registrar esa novedad y notificarle al maestro
        sobre el cambio
        """
        SPECTRUM_USE_RESP = {
            "databaseChange": True
        }