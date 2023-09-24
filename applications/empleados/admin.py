from django.contrib import admin
from .models import Empleado,Habilidades
# Register your models here.


admin.site.register(Habilidades)#tabla habilidades

#crear un decorador para que en el admin  nos aparesca como tabla
class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
        'id',
    )
    #crear una funcion para agregar un campo que no se encuentra en nuestro modelo de datos
    def full_name(self,obj):
        print (obj.first_name)
        return obj.first_name + ' ' + obj.last_name
    #

    
    search_fields=('first_name',) #agregar un buscador al admin de django
    list_filter=('job','habilidades','departamento',) #agregar filtro al admin django
    filter_horizontal=('habilidades',) #agrega un buscador cuando existen muchas opciones de seleccion y funciona en la relacion mucho a mucho
admin.site.register(Empleado,EmpleadoAdmin) #tabla empleado

