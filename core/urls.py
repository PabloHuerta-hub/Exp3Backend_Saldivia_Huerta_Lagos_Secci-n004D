from django.urls import path
from .views import inicio,cartelera,sobrenosotros,formularioregistro

urlpatterns =[
    path('',inicio,name="Inicio"),
    path('cartelera',cartelera,name="Galeria"),
    path('sobre nosotros',sobrenosotros,name="QuienesSomos"),
    path('formulario_registro',formularioregistro,name="Formulario_registro")
]