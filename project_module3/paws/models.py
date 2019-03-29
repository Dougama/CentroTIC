from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.


class Point(models.Model):
    latitude = models.CharField(max_length=25)
    longitude = models.CharField(max_length=25)

class Ellipse(models.Model):
    semiMajorAxis = models.FloatField()
    semiMinorAxis = models.FloatField()
    orientation = models.FloatField()
    center = models.ForeignKey(Point, on_delete=models.CASCADE)


class Geolocation(models.Model):
    """
    Para expresar las coordenadas en unidades de grados y metros
    """
    point = models.ForeignKey(Ellipse, on_delete=models.CASCADE)
    confidence = models.IntegerField(default=95)


class AntennaCharacteristics(models.Model):
    """
    AGL: Above Ground Level (default)
    AMSL: Above Mean Sea Level)
    """
    height = models.FloatField()
    AGL = "AGL"
    AMSL = "AMSL"
    enum_heigtType =  ((AGL, "Above Ground Level"), (AMSL, "AMSL: Above Mean Sea Level"))
    heightType = models.CharField(max_length=50, choices=enum_heigtType, default=AGL)
    antenna_direction = models.CharField(max_length=20, blank=True)
    antenna_radiation_pattern = models.CharField(max_length=15, blank=True)
    antenna_gain = models.FloatField(blank=True)

class FrequencyRange(models.Model):
    """
    Provee informacion adicional que puede ayudar a determinal la disponibilidad del espectro,
    provee las frecuencias en las que el dispositivo puede operar
    """
    startHz = models.FloatField()
    stopHz = models.FloatField()

class DeviceCapabilities(models.Model):
    frequencyRanges = models.ForeignKey(FrequencyRange, on_delete=models.CASCADE)


class DeviceDescriptor(models.Model):
    """
    Contiene parametros para identificar el dispositivo especifico

    """
    serialNumber = models.CharField(max_length=25)
    manufacturerId = models.CharField(max_length=25)
    modelId = models.CharField(max_length=25)
    rulesetIds = JSONField()
    anttenna_characteristics = models.ForeignKey(AntennaCharacteristics, on_delete=models.CASCADE)
    devicecapabilities = models.ForeignKey(DeviceCapabilities, on_delete=models.CASCADE)
    geolocation = models.ForeignKey(Geolocation, on_delete=models.CASCADE)

class DeviceOwner(models.Model):
    """
    Provee informacion de los propietarios
    """
    owner = JSONField()
    operator = JSONField()
    devicedescriptor = models.ForeignKey(DeviceDescriptor, on_delete=models.CASCADE)

class RulsetInfo(models.Model):
    """
    Contiene las reglas de dominio del ente regulador
    """
    authority = models.CharField(max_length=50)
    rulsetId = models.CharField(max_length=50)
    maxLocationChange = models.FloatField(blank=True)
    maxPollingSecs = models.FloatField(blank=True)


class EventTime(models.Model):
    """ Indica el periodo de tiempo sobre el cual el espectro
    es valido
    """
    startTime = models.DateTimeField(auto_now=False, auto_now_add=False)
    stopTime = models.DateTimeField(auto_now=False, auto_now_add=False)

class Spectrum(models.Model):
    resolutionBwHz = models.FloatField()
    profiles = JSONField()
    geolocation = models.ForeignKey(Geolocation, on_delete=models.CASCADE)

class SpectrumProfilePoint(models.Model):
    hz = models.FloatField()
    dbm = models.FloatField()
    
class SpectrumProfile(models.Model):
    """Se caracteriza por una lista ordenada de la potencia maxima permitida
    """
    list1= models.ForeignKey(SpectrumProfilePoint, on_delete=models.CASCADE)
    rulsetinfo = models.ForeignKey(RulsetInfo, on_delete=models.CASCADE)


class SpectrumSchedule(models.Model):
    """Indica el periodo de tiempo sobre el cual ese espectro esta disponible
    """
    eventTime = models.ForeignKey(EventTime, on_delete=models.CASCADE)
    spectrum = models.ForeignKey(Spectrum, on_delete=models.CASCADE)


class SpectrumSpec(models.Model):
    """Muestra la disponibilidad de espectro para un conjunto de reglas
    """
    rulsetInfo = models.ForeignKey(RulsetInfo, on_delete=models.CASCADE)
    spectrumSchedules = models.ForeignKey(SpectrumSchedule, on_delete=models.CASCADE)
    timeRange = models.ForeignKey(EventTime, on_delete=models.CASCADE)
    frequencyRanges = JSONField(encoder="")
    needsSpectrumReport = models.BooleanField()
    maxTotalBwHz = models.FloatField(blank=True)
    maxContiguousBwHz = models.FloatField(blank=True)
    geolocation = models.ForeignKey(Geolocation, on_delete=models.CASCADE)

class DeviceValidity(models.Model):
    deviceDesc = models.ForeignKey(DeviceDescriptor, on_delete=models.CASCADE)
    isValid = models.BooleanField()
    reason = models.CharField(max_length=150)