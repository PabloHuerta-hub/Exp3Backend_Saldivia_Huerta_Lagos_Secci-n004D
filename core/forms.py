from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Users,Usuarios,CategoriaCompra,Compras

class UsuariosForm(forms.ModelForm):
    class Meta:
        model= Usuarios
        fields= ['nombre','apellido','nomUsuario','direccion','correo','contraseña']
        labels = {'nombre': 'Nombre:', 
        'apellido':'Apellido:',
        'nomUsuario':'Nombre Usuario:',
        'direccion':'Direccion:',
        'correo':'Correo:',
        'contraseña':'Contraseña:',
        }
        widgets ={
            'nombre':forms.TextInput(
                attrs={
                    'class':'form_control',
                    'placeholder':'Ingrese nombre',
                    'id':'nombre'
                }
            ),
             'apellido':forms.TextInput(
                attrs={
                    'class':'form_control',
                    'placeholder':'Ingrese apellido',
                    'id':'apellido',
                }
            ),
             'nomUsuario':forms.TextInput(
                attrs={
                    'class':'form_control',
                    'placeholder':'Ingrese nombre de usuario',
                    'id':'nomUsuario'
                }
            ),
             'direccion':forms.TextInput(
                attrs={
                    'class':'form_control',
                    'placeholder':'Ingrese direccion',
                    'id':'direccion'
                }
            ),
             'correo':forms.TextInput(
                attrs={
                    'class':'form_control',
                    'placeholder':'Ingrese correo',
                    'id':'correo',
                }
            ),
             'contraseña':forms.TextInput(
                attrs={
                    'class':'form_control',
                    'placeholder':'Ingrese contraseña',
                    'id':'contraseña'
                }
            )
        }

class ComprasForm(forms.ModelForm):
    class Meta:
        model= Compras
        fields= ['pelicula','entradas','correocompra','telefono','nrotarjeta','anno','mes','nroverificador','nombrecompra','apellidocompra','direccioncompra','codigopostal']
        labels = {'pelicula':'Pelicula',
        'entradas':'Entradas',
        'correo': 'Correo',
        'telefono':'Telefono',
        'nrotarjeta':'NroTarjeta',
        'anno':'Año',
        'mes':'Mes',
        'nroverificador':'Numero Verificador',
        'nombrecompra':'Nombre',
        'apellidocompra':'Apellido',
        'direccioncompra':'Direccion',
        'codigopostalcompra':'Codigo postal',
        }
        
    
        widgets ={
            'pelicula':forms.Select(
            attrs={
              'class':'form_control',
              'id':'pelicula',

            }
            ),
            'entradas':forms.TextInput(
                attrs={
                    'class':'form_control',
                    'placeholder':'Ingrese numero entradas',
                    'id':'entradas'
                }
            ),
            'correo':forms.TextInput(
                attrs={
                    'class':'form_control',
                    'placeholder':'Ingrese correo',
                    'id':'correo',
                }
            ),
            'telefono':forms.TextInput(
                attrs={
                    'class':'form_control',
                    'placeholder':'Ingrese numero telefonico',
                    'id':'telefono'
                }
            ),
            'nrotarjeta':forms.TextInput(
                attrs={
                    'class':'form_control',
                    'placeholder':'Ingrese numero de tarjeta',
                    'id':'nrotarjeta'
                }
            ),
            'anno':forms.TextInput(
                attrs={
                    'class':'form_control',
                    'placeholder':'Ingrese año ',
                    'id':'anno'
                }
            ),
            'mes':forms.TextInput(
                attrs={
                    'class':'form_control',
                    'placeholder':'Ingrese mes',
                    'id':'mes'
                }
            ),
            'nroverificador':forms.TextInput(
                attrs={
                    'class':'form_control',
                    'placeholder':'Ingrese numero verificador',
                    'id':'nroverificador'
                }
            ),
            'nombre':forms.TextInput(
                attrs={
                    'class':'form_control',
                    'placeholder':'Ingrese nombre',
                    'id':'nombrecompra'
                }
            ),
             'apellido':forms.TextInput(
                attrs={
                    'class':'form_control',
                    'placeholder':'Ingrese apellido',
                    'id':'apellidocompra',
                }
            ),
             'direccion':forms.TextInput(
                attrs={
                    'class':'form_control',
                    'placeholder':'Ingrese direccion',
                    'id':'direccioncompra'
                }
            ),
             'codigopostal':forms.TextInput(
                attrs={
                    'class':'form_control',
                    'placeholder':'Ingrese codigo postal',
                    'id':'codpostal'
                }
            )
        }