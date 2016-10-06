from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Docente(models.Model):
	id_profesor = models.OneToOneField(User, on_delete=models.CASCADE) #user
	nombre = models.CharField('Nombre', max_length=100, blank=True, null=True)
	apellido = models.CharField('Apellido', max_length=100, blank=True, null=True)
	direccion = models.TextField('Direccion')
	telefono = models.CharField('Telefono', max_length=100, blank=True)
	codigo = models.CharField(max_length=200, blank=True, null=True)
	correo = models.CharField('Correo', max_length=200, blank=True, null=True)
	#imagen = models.ImageField('Imagen', upload_to='stores/', blank=True)
	observaciones = models.CharField('Nombre', max_length=100)
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def __str__(self):
		return self.user.get_full_name()


class Institucion(models.Model):
	id_institucion = models.OneToOneField(User, on_delete=models.CASCADE) #user
	nombre = models.CharField(max_length=200, blank=True, null=True)
	correo = models.CharField(max_length=200, blank=True, null=True)
	telefono = models.CharField(max_length=200, blank=True, null=True)
	observaciones = models.CharField('Nombre', max_length=100)
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def __str__(self):
		return self.user.get_full_name()

class Nota(models.Model):
	criterionota = models.ForeignKey('CriterioNota', on_delete=models.CASCADE)
	promedio_final = models.CharField(max_length=200, blank=True, null=True)
	observaciones = models.CharField('Nombre', max_length=100)
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.promedio_final


class Curso(models.Model):
	nota = models.ForeignKey('Nota', on_delete=models.CASCADE)
	nombre = models.CharField('Nombre', max_length=100)
	creditos = models.CharField('Creditos', max_length=100, blank=True)
	horario = models.CharField('Horario', max_length=100, blank=True)
	aula = models.CharField('Aula', max_length=100, blank=True)
	
	class Meta:
		verbose_name = 'Nota'
		verbose_name_plural = 'Nota'

	def __str__(self):
		return self.nombre

	def __iter__(self):
		return [ self.nombre,
				 self.creditos,
				 self.horario,
				 self.aula]


class Alumno(models.Model):
	id_alumno = models.OneToOneField(User, on_delete=models.CASCADE) #user
	curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
	nombre = models.CharField('Nombre', max_length=100, blank=True, null=True)
	apellido = models.CharField('Apellido', max_length=100, blank=True, null=True)
	direccion = models.TextField('Direccion')
	telefono = models.CharField('Telefono', max_length=100, blank=True)
	codigo = models.CharField(max_length=200, blank=True, null=True)
	correo = models.CharField('Correo', max_length=200, blank=True, null=True)
	#imagen = models.ImageField('Imagen', upload_to='stores/', blank=True)
	#observaciones = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def __str__(self):
		return self.user.get_full_name()


class CriterioNota(models.Model):
	peso1 = models.CharField('Nombre', max_length=100)
	peso2 = models.CharField('Nombre', max_length=100)
	peso3 = models.CharField('Nombre', max_length=100)
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.nota
