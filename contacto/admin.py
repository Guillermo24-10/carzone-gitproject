from django.contrib import admin
from .models import Contacto
# Register your models here.


class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'car_tittle', 'ciudad', 'fecha_creacion')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email', 'car_tittle')
    list_per_page = 25

admin.site.register(Contacto,ContactoAdmin)
