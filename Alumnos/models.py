from django.db import models

# Create your models here.

class Alumno(models.Model):
	dni      = models.IntegerField()
	nombre   = models.CharField(max_length=70,null=True)
	apellido = models.CharField(max_length=70)
	fecha_nacimiento = models.DateField(null=True)
	legajo   = models.CharField(max_length=9)

	def __str__(self):
		return self.apellido

	#@staticmethod
	#def buscar_legajo(dni, apellido, legajo):
		#if (apellido):
		#	queryset =Alumno.objects.filter(apellido__iexact='apellido')
		#return Alumno.objects.filter(apellido__iexact='apellido')
	@staticmethod
	def buscar_legajo_dni(dni):
		return Alumno.objects.filter(dni=dni)
	@staticmethod
	def buscar_legajo_apellido(apellido):
		return Alumno.objects.filter(apellido=apellido)
	@staticmethod
	def buscar_legajo_legajo(legajo):
		return Alumno.objects.filter(legajo=legajo)


class Lugar(models.Model):
	descripcion = models.CharField(max_length=30)

class Archivo(models.Model):
	numero = models.IntegerField()
	cajones = models.IntegerField()
	lugar = models.ForeignKey(Lugar,null=True)	

class Localizacion(models.Model):
	cajon    = models.IntegerField()
	lugar    = models.ForeignKey(Lugar,null = True)
	archivo  = models.ForeignKey(Archivo,null = True)
	alumno   = models.ForeignKey(Alumno,null = True)

	#def __str__(self):
	#	return self.lugar
	
	@staticmethod
	def localizacion(id):
		return Localizacion.objects.filter(alumno=id)

	#def archivo(localizacion):
	#	return Archivo.objects.get(pk=archivo)
