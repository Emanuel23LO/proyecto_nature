from django.db import models

class Comodidad(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=255)
    status = models.BooleanField(default=True)
    

def __str__(self):
    return self.name
