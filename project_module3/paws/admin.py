from django.contrib import admin
from .models import DeviceCapabilities, DeviceDescriptor
# Register your models here.
admin.site.register(DeviceCapabilities)
admin.site.register(DeviceDescriptor)

