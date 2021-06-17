from django.urls import path
from .views import inicio,cartelera,sobrenosotros,formularioregistro,formulario_compra

urlpatterns =[
    path('',inicio,name="Inicio"),
    path('cartelera',cartelera,name="Galeria"),
    path('sobre nosotros',sobrenosotros,name="QuienesSomos"),
    path('formulario_registro',formularioregistro,name="Formulario_registro"),
    path('formulario_compra',formulario_compra,name="Formulario_compra") 
]