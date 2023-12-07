from django.db import models

class Reserva(models.Model):
    description= models.CharField(max_length=300)
    number_people = models.CharField(max_length=10)
    date = models.CharField(max_length=20)
    availability=models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    cabaña = models.ForeignKey('cabañas.Cabaña', on_delete=models.DO_NOTHING)
    

def __str__(self):
    return self.availability