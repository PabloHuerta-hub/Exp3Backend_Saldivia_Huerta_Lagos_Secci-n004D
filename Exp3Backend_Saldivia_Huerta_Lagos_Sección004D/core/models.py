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
    correo=models.CharField(primary_key=True,max_length=60,verbose_name='Correo')
    contraseña=models.CharField(max_length=50, verbose_name='Contraseña')
    def __str__(self):
        return self.correo