from django.db import models

# Create your models here.
class Users(models.Model):
    idUsuario= models.IntegerField(primary_key=True, verbose_name="Id de usuario")
    nombreCategoria= models.CharField(max_length=50, verbose_name="Nombre de categoria")

    def __str__(self):
        return self.nombreCategoria

        
class Usuarios(models.Model):
    nombre=models.CharField(max_length=50, verbose_name='Nombre')
    apellido=models.CharField(max_length=50, verbose_name='Apellido')
    nomUsuario=models.CharField(max_length=50, verbose_name='Nombre Usuario')
    direccion=models.CharField(max_length=50, verbose_name='Direccion')
    correo=models.EmailField(primary_key=True,max_length=60,verbose_name='Correo')
    contraseña=models.CharField(max_length=50, verbose_name='Contraseña')
    def __str__(self):
        return self.correo

class CategoriaCompra(models.Model):
    idpelicula= models.IntegerField(primary_key=True, verbose_name="Id de pelicula")
    nombre= models.CharField(max_length=50, verbose_name="Nombre de categoria")

    def __str__(self):
        return self.nombre
class pelicula(models.Model):
    foto=models.ImageField(upload_to="photos",verbose_name="foto")
    nombre=models.CharField(primary_key=True,max_length=50, verbose_name="nombre")
    sinopsis=models.TextField(verbose_name="sinopsis")
    def __str__(self):
        return self.nombre
class Compras(models.Model):
    pelicula=models.CharField(primary_key=True, max_length=100, verbose_name='Pelicula')
    entradas=models.IntegerField(verbose_name="Cant_entradas")
    correocompra=models.CharField(max_length=60,verbose_name='Correo')
    telefono=models.CharField(max_length=19, verbose_name="Telefono")
    nrotarjeta=models.IntegerField( verbose_name="Nrotarjeta")
    anno=models.IntegerField( verbose_name="anno")
    mes=models.IntegerField(verbose_name="mes")
    nroverificador=models.IntegerField( verbose_name="nroverificador")
    nombrecompra=models.CharField(max_length=50, verbose_name='Nombre')
    apellidocompra=models.CharField(max_length=50, verbose_name='Apellido')
    direccioncompra=models.CharField(max_length=100, verbose_name='Direccion')
    codigopostal=models.IntegerField( verbose_name='Codigopostal')
    def __str__(self):
        return self.pelicula