from django.shortcuts import render
from django.http import HttpResponse,Http404
from Alumnos.models import Alumno, Localizacion, Lugar, Archivo
from Alumnos.forms import Busqueda_legajo_dni, Busqueda_legajo_apellido, Busqueda_legajo_legajo

def index(request):
	return render(request, 'base.html')

def busqueda_apellido(request):
	if request.method == 'POST':
		form = Busqueda_legajo_apellido(request.POST)
		if form.is_valid():	
			apellido = form.cleaned_data['apellido']	
			legajos_encontrados = Alumno.buscar_legajo_apellido(apellido)
			return render(request, 'resultado.html', {'apellido': apellido, 'legajos_encontrados': legajos_encontrados})
	else:
		form = Busqueda_legajo_apellido()
	return render(request, 'busqueda_apellido.html',{'form':form})

def busqueda_dni(request):
	if request.method == 'POST':
		form = Busqueda_legajo_dni(request.POST)
		if form.is_valid():
			dni = form.cleaned_data['dni']
			legajos_encontrados = Alumno.buscar_legajo_dni(dni)
			return render(request, 'resultado.html', {'dni': dni, 'legajos_encontrados': legajos_encontrados})
	else:
		form = Busqueda_legajo_dni()
	return render(request, 'busqueda_dni.html',{'form':form})

def busqueda_legajo(request):
	if request.method == 'POST':
		form = Busqueda_legajo_legajo(request.POST)
		if form.is_valid():
			legajo = form.cleaned_data['legajo']
			legajos_encontrados = Alumno.buscar_legajo_legajo(legajo)
			return render(request, 'resultado.html', {'legajo': legajo, 'legajos_encontrados': legajos_encontrados})
	else:
		form = Busqueda_legajo_legajo()
	return render(request, 'busqueda_legajo.html',{'form':form})

	
def alumno(request, id):
	try:
		alumno = Alumno.objects.get(pk=id)
		keyalumno = alumno.id
		lugar = Localizacion.objects.get(pk=keyalumno).lugar.descripcion
		archivo = Localizacion.objects.get(pk=keyalumno).archivo.numero
		cajon = Localizacion.objects.get(pk=keyalumno).cajon
	except Alumno.DoesNotExist:
		raise Http404("No se encontró el legajo")
	return render(request, 'alumno.html',{'alumno': alumno, 'lugar': lugar, 'archivo': archivo, 'cajon': cajon})

# Create your views here.
