from django.contrib import admin
from django.urls import path
from . import views

app_name= "departamento_app"
urlpatterns = [
    path('new-departamento/', views.NewDepartamento.as_view(),name='nuevo-departamento'),
    path('departamento-lista/', views.Listadepartamento.as_view(),name='departamento-list')   
]