from django.shortcuts import render
from django.http import HttpResponse,Http404
from Alumnos.models import Alumno, Localizacion
from Alumnos.forms import Busqueda_legajo


def busqueda(request):
	if request.method == 'POST':
		form = Busqueda_legajo(request.POST)
		if form.is_valid():
			#dni = form.cleaned_data['dni']
			apellido = form.cleaned_data['apellido']
			#legajo = form.cleaned_data['legajo']

			#legajos_encontrados = Alumno.buscar_legajo(dni, apellido, legajo)
			legajos_encontrados = Alumno.buscar_legajo(apellido)
			#return render(request, 'resultado.html', {'dni': dni, 'apellido': apellido, 'legajo': legajo, 'legajos_encontrados': legajos_encontrados})
			return render(request, 'resultado.html', {'apellido': apellido, 'legajos_encontrados': legajos_encontrados})
	else:
		form = Busqueda_legajo()
	return render(request, 'busqueda.html',{'form':form})

def alumno(request, id):
	try:
		alumno = Alumno.objects.get(pk=id) 
	except Alumno.DoesNotExist:
		raise Http404("No se encontró el legajo")
	return render(request, 'alumno.html',{'alumno': alumno})

# Create your views here.
