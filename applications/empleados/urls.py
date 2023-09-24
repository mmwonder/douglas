from django.urls import path
from . import views

app_name="persona_app"
urlpatterns = [
     path('', views.InicioView.as_view(),name='inicio'),
    path('lista-empleados/', views.listAllempleados.as_view(),name='empleados_all'),
    path('lista-departamento/<name>', views.listadepa.as_view(), name='empleado_area'),
    path('buscar-empleado', views.listaempleadoinput.as_view()),
    path('lista-emp', views.listhabilidades.as_view()),
     path('detalle-empleado/<pk>', views.empleado_detalle.as_view(),name='empleado_detail'),
     path('add-empleado/', views.EmpleadoCreateView.as_view(),name='empleado_add'),
     path('success/', views.Success.as_view(),name='correcto'),
     path('update-empleado/<pk>/', views.EmpleadpUpdateView.as_view(),name='modificar_empleado'),
     path('eliminar-empleado/<pk>/', views.EmpleadoDeleteView.as_view(),name='eliminar_empleado'),
      path('lista-empleadoadmin/', views.ListaEmpleadosAdmin.as_view(),name='empleados_admin'),
    
    
    
]