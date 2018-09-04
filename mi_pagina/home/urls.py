from django.urls import path
from .views import *


urlpatterns = [
	path('mi_pagina/',vista_perros),
	path('agregar_raza/', vista_agregar_raza, name = 'vista_agregar_raza'),
	path('agregar_perro/', vista_agregar_perro, name = 'vista_agregar_perro'),
	path('lista_perros/',vista_lista_perros, name = 'vista_lista_perros'),
	path('ver_perros/<int:id_product>/', vista_ver_perros, name = 'vista_ver_perros'),
	path('editar_perros/<int:id_product>/',vista_editar_perros, name = 'vista_editar_perros'),
	path('eliminar_perros/<int:id_product>/', vista_eliminar_perros, name = 'eliminar_ver_perros'),	
	path('login/',vista_login, name= 'vista_login'),
	path('logout/',vista_logout, name='vista_logout'),
	path('',vista_inicio),
	path('register/',vista_register,name='vista_register'),
	path('crear_perfil/',vista_crear_perfil,name='crear_perfil'),
	#path('register/',vista_register, name='vista_register'),

]
