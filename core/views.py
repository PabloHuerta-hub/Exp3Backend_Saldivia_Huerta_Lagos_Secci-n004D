from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'Inicio.html')

def cartelera(request):
    return render(request,'Cartelera.html')
    
def sobrenosotros(request):
    return render(request,'QuienesSomos.html')