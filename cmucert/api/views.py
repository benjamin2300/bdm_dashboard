from rest_framework import generics

from cmucert.models import Logon, Device, Employee
from cmucert.api.serializers import (LogonSerializer,
                                     DeviceSerializer,
                                     EmployeeSerializer)

class EmployeeListCreateAPIView(generics.ListCreateAPIView):
  queryset = Employee.objects.all().order_by("-id")
  serializer_class = EmployeeSerializer

class EmployeeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer