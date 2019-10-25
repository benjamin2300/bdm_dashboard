from django.contrib import admin
from cmucert.models import Device, Employee, Logon 

# Register your models here.
admin.site.register(Device)
admin.site.register(Employee)
admin.site.register(Logon)