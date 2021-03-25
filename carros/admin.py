from django.contrib import admin
from .models import Carro
from django.utils.html import format_html ## FORMATO HTML DENTRO DE DJANGO
# Register your models here.

class CarroAdmin(admin.ModelAdmin):

    def Perfil(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.foto.url))

    Perfil.short_description = 'Imagen' # CAMBIAR DE NOMBRE LA COLUMNA

    list_display = ('id','Perfil','car_tittle','ciudad','color','modelo','year','estilo_cuerpo','tipo_combustible','destacado')
    list_display_links = ('id','Perfil','car_tittle')
    list_editable = ('destacado',)
    search_fields = ('id','car_tittle','ciudad','modelo','estilo_cuerpo')
    list_filter = ('ciudad','modelo','estilo_cuerpo','tipo_combustible')

admin.site.register(Carro, CarroAdmin)
