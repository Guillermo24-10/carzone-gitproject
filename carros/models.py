from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField ## LIBRERIA PARA HOJA DE TEXTO
from multiselectfield import MultiSelectField
# Create your models here.

class Carro(models.Model):

    estado_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))

    caracteristicas_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )




    puertas_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )


    car_tittle = models.CharField(max_length=255)
    estado = models.CharField(choices=estado_choice, max_length=100)
    ciudad = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condicion = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = RichTextField()
    foto = models.ImageField(upload_to='foto/%Y/%m/%d/')
    foto_1 = models.ImageField(upload_to='foto/%Y/%m/%d/', blank=True)
    foto_2 = models.ImageField(upload_to='foto/%Y/%m/%d/', blank=True)
    foto_3 = models.ImageField(upload_to='foto/%Y/%m/%d/', blank=True)
    foto_4 = models.ImageField(upload_to='foto/%Y/%m/%d/', blank=True)
    caracteristicas = MultiSelectField(choices=caracteristicas_choices)
    estilo_cuerpo = models.CharField(max_length=100)
    motor= models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    millas = models.IntegerField()
    puertas = models.CharField(choices=puertas_choices,max_length=10)
    pasajeros = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    kilometraje = models.IntegerField()
    tipo_combustible = models.CharField(max_length=50)
    propietarios = models.CharField(max_length=100)
    destacado = models.BooleanField(default=False)
    fec_creacion = models.DateTimeField(default=datetime.now(), blank=True)


    def __str__(self):
        return self.car_tittle
