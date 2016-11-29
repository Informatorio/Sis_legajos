from django import forms
from Alumnos.models import Alumno, Localizacion, Lugar, Archivo

# class Busqueda_legajo(forms.Form):
# 	dni = forms.IntegerField(label='D.N.I', required=False)
# 	apellido = forms.CharField(label='Apellido',max_length=70)
# 	legajo = forms.CharField(label='Legajo',max_length=9, required=False)

class Busqueda_legajo_dni(forms.Form):
	dni = forms.IntegerField(label='D.N.I')

class Busqueda_legajo_apellido(forms.Form):
	apellido = forms.CharField(label='Apellido',max_length=70)
"""
#<<<<<<< HEAD
	legajo = forms.CharField(label='Legajo',max_length=9, required=False)

class LugarForm(forms.ModelForm):
	class Meta:
		model = Lugar
		fields = ['descripcion',]
		labels = {'descripcion': 'Descripción',}

class ArchivoForm(forms.ModelForm):
	class Meta:
		model =  Archivo
		fields = ['numero','cajones','lugar',]
		lables = {'numero': 'Código', 'cajones': 'Número de cajón', 'lugar': 'Lugar'}
#=======
"""

class Busqueda_legajo_legajo(forms.Form):
	legajo = forms.CharField(label='Legajo',max_length=9)

#class Nuevo_alumno(forms.Form):
#	dni = forms.IntegerField(label="D.N.I:")
#	nombre = forms.CharField(label="Nombre:",max_length=70,required=True)
#	apellido = forms.CharField(label="Apellido:",max_length=70,required=True)
#	fecha_nacimiento = forms.DateField(label="Fecha de Nacimiento:")

class Nuevo_alumno(forms.ModelForm):# Nuevo_alumnoForm
	class Meta:
		model = Alumno
		fields = ('legajo', 'dni', 'nombre', 'apellido', 'fecha_nacimiento')

class AlmacenarForm(forms.ModelForm):
	class Meta:
		model = Localizacion
		fields = ('lugar', 'archivo', 'cajon')
