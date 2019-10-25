from django.db import models

# Create your models here.
class Employee(models.Model):

  name = models.CharField(max_length=100)
  position = models.CharField(max_length=130)

  def __str__(self):
    return self.name

class Logon(models.Model):
  event_id = models.CharField(max_length=100)
  datetime = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(Employee,
                           on_delete=models.CASCADE,
                           related_name = "logons")
  pc = models.CharField(max_length=20)
  activity = models.CharField(max_length=30)
  
  def __str__(self):
    return event_id

class Device(models.Model):
  event_id = models.CharField(max_length=100)
  datetime = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(Employee,
                           on_delete=models.CASCADE,
                           related_name = "devices")
  pc = models.CharField(max_length=20)
  activity = models.CharField(max_length=30)

  def __str__(self):
    return event_id