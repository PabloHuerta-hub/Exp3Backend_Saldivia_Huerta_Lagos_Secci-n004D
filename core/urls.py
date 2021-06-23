from django.urls import path, include
from .views import inicio,cartelera,sobrenosotros,formularioregistro,formulario_compra, pelicula_form
from . import views

from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
urlpatterns =[
    path('',inicio,name="Inicio"),
    path('cartelera',cartelera,name="Galeria"),
    path('sobre nosotros',sobrenosotros,name="QuienesSomos"),
    path('formulario_registro',formularioregistro,name="Formulario_registro"),
    path('formulario_compra',formulario_compra,name="Formulario_compra"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('pelicula_form', pelicula_form, name='pelicula_form')
]
