from django.db import models
from applications.departamentos.models import Departamento
from ckeditor.fields import RichTextField #importar el editor keditor

# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class meta:
        verbose_name='Habilidad'
        verbose_name_plural='Habilidades Empleados'
    def __str__(self):
        return str(self.id) + '-' + self.habilidad 

class Empleado(models.Model):
    '''Modelo para la tabla empleado'''
    JOB_CHOICES=(
        ('0','Contador' ),
        ('1','Administrador' ),
        ('2','Economista' ),
        ('3','Otro' ),
        
        )
    first_name = models.CharField('Nombre', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name= models.CharField('Nombres_completo',max_length=120,blank=True)
    avatar=models.ImageField(upload_to='empleados',blank=True,null=True)
    job = models.CharField('Trabajo', max_length=1,choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    hojavida=RichTextField() #agregar el keditor
    #image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    class Meta:
        verbose_name='Empleado'
        verbose_name_plural='Personal del la Empresa'
        ordering=('first_name','last_name')

    def __str__(self) -> str:
       return str(self.id) + ' ' + self.first_name + ' ' + self.last_name 

   