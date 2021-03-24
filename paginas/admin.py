from django.contrib import admin
from .models import Equipo
from django.utils.html import format_html

# Register your models here.


class EquipoAdmin(admin.ModelAdmin):
    def Perfil(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.foto.url))

    Perfil.short_description = 'Foto' # CAMBIAR DE NOMBRE LA COLUMNA

    list_display = ('id', 'Perfil','nombre', 'designacion', 'fec_creacion') #LLAMAR COLUMNAS
    list_display_links = ('id','Perfil','nombre',) # PONERLO COMO LINK
    search_fields = ('nombre','apellido','designacion') #CAJA DE TEXTO PARA BUSCAR
    list_filter = ('designacion',)

admin.site.register(Equipo,EquipoAdmin)
