from django.shortcuts import render
from django.views.generic.edit import FormView
from applications.empleados.models import Empleado
from .models import Departamento
from .forms import NewDepartamentoform
from django.views.generic import ListView

# Create your views here.
class Listadepartamento(ListView):
    model=Departamento
    template_name='departamentos/lista.html'



class NewDepartamento(FormView):
    template_name='departamentos/newdepartamento.html'
    form_class=NewDepartamentoform
    success_url='/'

    def form_valid(self,form):
        print('--------------estamos en el form valid-----------')
        depa= Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shorname'],
        )
        depa.save()
        nombre=form.cleaned_data['nombre']
        apellido=form.cleaned_data['apellido']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='4',
            departamento=depa

        )
        
        return super(NewDepartamento,self).form_valid(form)