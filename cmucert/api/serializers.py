from rest_framework import serializers
from cmucert.models import Device, Employee, Logon

class DeviceSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Device
    exclude = ("user", )
    

class LogonSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Logon
    exclude = ("user", )

class EmployeeSerializer(serializers.ModelSerializer):

  logoons = LogonSerializer(many=True, read_only=True)
  devices = DeviceSerializer(many=True, read_only=True)
  class Meta:
    model = Employee
    fields = "__all__"