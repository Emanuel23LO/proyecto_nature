from django.db import models

class Cabaña(models.Model):
    location = models.CharField(max_length=10, unique=True)
    description= models.CharField(max_length=300)
    availability = models.CharField(max_length=10)
    value = models.DateField()
    status = models.BooleanField(default=True)
    comodidad = models.ForeignKey('comodidades.Comodidad', on_delete=models.DO_NOTHING)
    tipo_cabaña = models.ForeignKey('tipo_cabañas.Tipo_cabaña', on_delete=models.DO_NOTHING)

def __str__(self):
    return self.value