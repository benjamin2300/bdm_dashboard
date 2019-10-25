from django.db import models

# Create your models here.
class employee(models.Model):

  name = models.CharField(max_length=100)
  position = models.CharField(max_length=130)

  def __str__(self):
    return self.name

class logon(models.Model):
  event_id = models.CharField(max_length=100, read_only=True)
  datetime = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(employee,
                           on_delete=models.CASCADE,
                           related_name = "logon-record")
  pc = models.CharField(max_length=20)
  activity = models.CharField(max_length=30)
  
  def __str__(self):
    return event_id

class device(models.Model):
  event_id = models.CharField(max_length=100, read_only=True)
  datetime = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(employee,
                           on_delete=models.CASCADE,
                           related_name = "device-record")
  pc = models.CharField(max_length=20)
  activity = models.CharField(max_length=30)

  def __str__(self):
    return event_id