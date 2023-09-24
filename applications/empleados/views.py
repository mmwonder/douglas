from typing import Any, Dict
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy #mejorar las redicciones 
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView
from django.core.paginator import Paginator
from .models import Empleado

# Create your views here.

class InicioView(TemplateView):
    template_name='inicio.html'

class listAllempleados(ListView):
    template_name= 'persona/list_all.html'
    paginate_by=4
    ordering='first_name'
    
    def get_queryset(self):
        palabra_clave=self.request.GET.get("kword",'')
        lista= Empleado.objects.filter(
            first_name__icontains=palabra_clave)
        #print('====',palabra_clave)
        #print('Lista resultado: ',lista)
        return lista

    

class listadepa(ListView):
    template_name= 'persona/list_depa.html'
    '''queryset=Empleado.objects.filter(departamento__name='Finanzas')'''

    def get_queryset(self):
        area=self.kwargs['name']
        lista= Empleado.objects.filter(departamento__name=area)
        return lista
    
    
class listaempleadoinput(ListView):
    template_name='persona/porpalabra.html'
    context_object_name='empleados'

    def get_queryset(self):
        print('*******************')
        palabra_clave=self.request.GET.get("kword",'')
        lista= Empleado.objects.filter(
            first_name=palabra_clave)
        #print('====',palabra_clave)
        #print('Lista resultado: ',lista)
        return lista
    
class listhabilidades(ListView):
    template_name='persona/habilidades.html'
    context_object_name='habilidades'

    def get_queryset(self):
        empleado=Empleado.objects.get(id=6) #recuperar empleado 
        return empleado.habilidades.all()



class empleado_detalle(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context=super(empleado_detalle,self).get_context_data(**kwargs)
        context['titulo']='Empleado del mes'
        return context
 
class Success(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    fields=[
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'avatar',
    ]
    success_url=reverse_lazy('persona_app:empleados_admin')

    def form_valid(self,form):
        empleado=form.save()
        empleado.full_name=empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)
    

class EmpleadpUpdateView(UpdateView):
    model=Empleado
    template_name = "persona/update.html"
    fields=[
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'avatar',
    ]
    success_url= reverse_lazy('persona_app:empleados_admin')

    
class EmpleadoDeleteView(DeleteView):
        model = Empleado
        template_name = "persona/delete.html"

        success_url=reverse_lazy('persona_app:empleados_admin')

class ListaEmpleadosAdmin(ListView):
    template_name= 'persona/lista_empleados.html'
    paginate_by=10
    ordering='first_name'
    model=Empleado
    
    