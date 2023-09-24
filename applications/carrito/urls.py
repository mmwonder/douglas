from django.contrib import admin
from django.urls import path
from .views import tienda,limpiar_carrito,agregar_producto,Sacar_producto

app_name= "carrito_app"
urlpatterns = [
    path('tienda/',tienda, name='tienda'),
    path('agregar/<int:prod_id>',agregar_producto, name='Agregar'),
     path('Sacar/<int:prod_id>',Sacar_producto, name='Sacar'),
    path('limpiar/',limpiar_carrito, name='Limpiar'),
     
]