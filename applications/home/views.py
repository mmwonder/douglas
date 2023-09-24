from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from .models import prueba
from .form import PruebaForm

# Create your views here.
class IndexView(TemplateView):
    template_name='home/home.html'

class PruebalistView(ListView):
    template_name= 'home/lista.html'
    queryset= ['A','B','C']
    context_object_name='lista_prueba'

#model se utiliza para listar o conectar
class Modelo_ListView(ListView):
    model = prueba
    template_name = "home/pruebas.html"
    context_object_name='list_prueba'

class pruebacreateview(CreateView):
    template_name= 'home/add.html'
    model=prueba
    form_class=PruebaForm
    success_url='/'