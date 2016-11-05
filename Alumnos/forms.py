from django import forms
from Alumnos.models import Alumno, Localizacion, Lugar, Archivo

class Busqueda_legajo(forms.Form):
	dni = forms.IntegerField(label='D.N.I', required=False)
	apellido = forms.CharField(label='Apellido',max_length=70)
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
