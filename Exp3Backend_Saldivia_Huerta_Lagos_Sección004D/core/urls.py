from django.urls import path
from .views import inicio,cartelera,sobrenosotros

urlpatterns =[
    path('',inicio,name="Inicio"),
    path('cartelera',cartelera,name="Galeria"),
    path('sobre nosotros',sobrenosotros,name="QuienesSomos")
]