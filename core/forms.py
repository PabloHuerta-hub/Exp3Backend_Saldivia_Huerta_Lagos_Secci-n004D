from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Users,Usuarios

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