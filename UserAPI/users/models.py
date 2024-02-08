from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=255)
  id_number = models.CharField(max_length=10, unique=True)
  phone = models.CharField(max_length=10)

class Meta:
  app_label = 'users'

def __str__(self):
  return self.name