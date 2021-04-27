from django.db import models
from datetime import datetime
# Create your models here.
class Contacto(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car_id = models.IntegerField()
    customer_need = models.CharField(max_length=100)
    car_tittle = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=100)
    mensaje = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    fecha_creacion = models.DateTimeField(blank=True,default=datetime.now)


    def __str__(self):
        return self.email
