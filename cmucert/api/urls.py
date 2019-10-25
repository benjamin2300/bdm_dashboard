from django.urls import path
from cmucert.api.views import (EmployeeDetailAPIView, EmployeeListCreateAPIView)

urlpatterns = [
  path("employees/", 
       EmployeeListCreateAPIView.as_view(), 
       name="employee-list"),
  path("emplyees/<int:pk>/",
       EmployeeDetailAPIView.as_view(),
       name="emplyee-detail")
]