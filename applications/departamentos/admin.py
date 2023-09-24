from django.contrib import admin
from .models import Departamento

# Register your models here.

#crear un decorador para que en el admin  nos aparesca como tabla
class DepAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'shor_name',
        'anulate',
    )
admin.site.register(Departamento,DepAdmin) #tabla departamento