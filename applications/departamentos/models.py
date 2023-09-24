from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombre Corto', max_length=20)
    anulate = models.BooleanField('Anulado',default=False)

    class Meta:
        verbose_name= 'Mi Departamento'
        verbose_name_plural='Areas de la Empresa'
        ordering=['-name'] #ordena los campos por nombre
        unique_together=('name','shor_name')#que no se repitan los campos introducidos

    def __str__(self) -> str:
       return str(self.id) + '-' + self.name + '-' + self.shor_name
  