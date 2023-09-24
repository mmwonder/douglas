from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .models import Productos
from .carrito import Carrito

# Create your views here.

def tienda(request):
    productos=Productos.objects.all()
    return render(request,'carrito/tiendaonline.html',{'productos':productos})

def agregar_producto(request,prod_id):

    carrito=Carrito(request)
    producto=Productos.objects.get(id=prod_id)
    carrito.agregar(producto)
    return  redirect('/tienda')

def Sacar_producto(request,prod_id):

    carrito=Carrito(request)
    producto=Productos.objects.get(id=prod_id)
    carrito.sacar(producto)
    return redirect('/tienda')

def limpiar_carrito(request):
    carrito=Carrito(request)
    carrito.limpiar()
    return redirect('/tienda')


