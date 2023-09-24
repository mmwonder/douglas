from django.db import models

# Create your models here
# agregamos models.Model para agregar una base de datos.
class prueba(models.Model):
    titulo=models.CharField(max_length=30)
    subtitulo = models.CharField( max_length=50)
    cantidad=models.DecimalField(max_digits=8,decimal_places=2)