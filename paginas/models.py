from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    designacion = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=100)
    twiter_link = models.URLField(max_length=100)
    google_plus = models.URLField(max_length=100)
    fec_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
