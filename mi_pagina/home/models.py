from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Raza(models.Model):
	nombre = models.CharField(max_length = 100)
	descripcion = models.TextField(max_length = 100)
	
	def __str__ (self):
		return self.nombre

class Cliente (models.Model):
	nombre = models.CharField(max_length = 100)
	apellido = models.CharField(max_length = 100)
	descripcion	= models.TextField(max_length =500)
	#perros = models.ManyToManyField(Perros, null = True,blank = True)

	def __str__ (self):
		return self.nombre

class Cuidador(models.Model):
	nombre = models.CharField(max_length = 100)
	apellido = models.CharField(max_length = 100)
	
	def __str__ (self):
		return self.nombre

class Veterinario(models.Model):
	nombre = models.CharField(max_length = 100)
	descripcion = models.TextField(max_length = 100)
	
	def __str__ (self):
		return self.nombre
		
class Perro(models.Model):
	nombre = models.CharField(max_length = 100)
	foto=models.ImageField(upload_to="fotos",null=True,blank=True)
	descripcion  = models.TextField(max_length  = 100)
	raza = models.ForeignKey(Raza, on_delete = models.PROTECT)
	cliente = models.ForeignKey(Cliente, on_delete = models.PROTECT)
	cuidador= models.ManyToManyField(Cuidador, null = True,blank = True)
	veterinario = models.ManyToManyField(Veterinario,null = True,blank=True)

	def __str__ (self):
	 	return self.nombre



class Perfil(models.Model):
	foto = models.ImageField(upload_to='perfiles', null=True, blank=True)
	identificacion = models.CharField(max_length = 100)
	edad = models.CharField(max_length =100)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	def __str__ (self):
		return self.identificacion


