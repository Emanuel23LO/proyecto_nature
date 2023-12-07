from django.db import models

class Servicio(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=255)
    value = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

    

def __str__(self):
    return self.name