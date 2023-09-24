from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('lista/', views.PruebalistView.as_view()),
    path('lista-prueba/', views.Modelo_ListView.as_view()),
    path('add/', views.pruebacreateview.as_view(),name='prueba_add'),
    
    
]