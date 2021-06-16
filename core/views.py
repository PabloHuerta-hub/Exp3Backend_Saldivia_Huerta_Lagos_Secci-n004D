from django.shortcuts import render,redirect
from .models import Usuarios
from .forms import UsuariosForm
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