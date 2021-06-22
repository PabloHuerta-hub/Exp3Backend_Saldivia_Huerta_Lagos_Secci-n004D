from django.shortcuts import render,redirect
from .models import Usuarios,Compras, pelicula
from .forms import UsuariosForm,ComprasForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
def inicio(request):
    return render(request,'Inicio.html')

def cartelera(request):
    return render(request,'Cartelera.html')
    
def sobrenosotros(request):
    return render(request,'QuienesSomos.html')

def formularioregistro(request):
    if request.method == 'POST':
        Usuarios_Form=UsuariosForm(request.POST)
        if Usuarios_Form.is_valid():
            Usuarios_Form.save()
            return redirect('Inicio')
    else:
        Usuarios_Form=UsuariosForm()
    return render(request,'core/FormularioRegistro.html',{'Usuarios_form':Usuarios_Form})
def formulario_compra(request):
    if request.method == 'POST':
        Compras_Form=ComprasForm(request.POST)
        if Compras_Form.is_valid():
            Compras_Form.save()
            return redirect('Inicio')
    else:
        Compras_Form=ComprasForm()
    return render(request,'core/Compra.html',{'Compras_form':Compras_Form})

class peliculaCreate(CreateView):
    model = pelicula
    fields = ['foto', 'nombre', 'sinopsis']
