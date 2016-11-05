from django.shortcuts import render
from django.http import HttpResponse,Http404
from Alumnos.models import Alumno, Localizacion, Lugar, Archivo
from Alumnos.forms import Busqueda_legajo, LugarForm


def busqueda(request):
	if request.method == 'POST':
		form = Busqueda_legajo(request.POST)
		if form.is_valid():
			#dni = form.cleaned_data['dni']
			apellido = form.cleaned_data['apellido']
			#legajo = form.cleaned_data['legajo']
			legajos_encontrados = Alumno.buscar_legajo(apellido)
			return render(request, 'resultado.html',{'apellido': apellido, 'legajos_encontrados': legajos_encontrados})
	else:
		form = Busqueda_legajo()
	return render(request, 'busqueda.html',{'form':form})

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

def lugar_create(request):
	if request.method == 'POST':
		form = LugarForm(request.POST)
		if form.is_valid():
			form.save()
		return render(request, 'lugar_list.html',{'lugares':Lugar.objects.all()})
	else:
		form = LugarForm()

	return render(request, 'lugar_form.html',{'form':form})

def lugar_list(request):
	return render(request, 'lugar_list.html',{'lugares':Lugar.objects.all()})

def archivo_create(request):
	if request.method == 'POST':
		form = ArchivoForm(request.POST)
		if form.is_valid():
			form.save()
		return render(request, 'archivo_list.html',{'archivo':Archivo.objects.all()})
	else:
		form = ArchivoForm()

	return render(request, 'archivo_form.html',{'form':form})

def archivo_list(request):
	return render(request, 'archivo_list.html',{'archivos':Archivo.objects.all()})

# Create your views here.
