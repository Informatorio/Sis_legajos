from django import forms
from Alumnos.models import Alumno, Localizacion

class Busqueda_legajo(forms.Form):
	dni = forms.IntegerField(label='D.N.I', required=False)
	apellido = forms.CharField(label='Apellido',max_length=70)
	legajo = forms.CharField(label='Legajo',max_length=9, required=False)