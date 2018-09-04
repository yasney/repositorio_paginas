from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User



# Create your views here.
def vista_perros(request):
	info_enviado=False
	email =""
	title =""
	text =""
	if request.method =="POST":
		formulario = contacto_form(request.POST)
		if formulario.is_valid():
			info_enviado = True 
			email = formulario.cleaned_data['correo']
			title = formulario.cleaned_data['titulo']
			text = formulario.cleaned_data['texto']
	else:
		formulario = contacto_form()
	return render(request,'perros.html',locals())	

def vista_lista_perros(request):
	lista = Perro.objects.all()
	return render (request, 'lista_perros.html',locals())

def vista_agregar_raza(request):
	if request.method == 'POST':
		formulario = agregar_raza_form(request.POST, request.FILES)
		if formulario.is_valid():
			prod=formulario.save(commit = False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect ('/lista_perros/')
	else:
		formulario = agregar_raza_form()
	return render(request,'agregar_raza.html',locals())

def vista_agregar_perro(request):
	if request.method == 'POST':
		formulario = agregar_perro_form(request.POST,request.FILES)
		if formulario.is_valid():
			prod = formulario.save(commit = False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect ('/lista_perros/')
	else:
		formulario = agregar_perro_form()
	return render(request,'agregar_perro.html',locals())	

def vista_ver_perros(request,id_product):
	p = Perro.objects.get(id = id_product)
	return render(request, 'ver_perros.html',locals())

def vista_editar_perros(request,id_product):
	prod = Perro.objects.get(id = id_product)
	if request.method == "POST":
		formulario = agregar_raza_form(request.POST,request.FILES,instance = prod)
		if formulario.is_valid():
			pro = formulario.save()
			return redirect('/lista_perros')
	else:
		formulario = agregar_raza_form(instance = prod)
	return render(request,'agregar_raza.html',locals())

def vista_eliminar_perros(request,id_product):
	pro = Perro.objects.get(id = id_product)
	pro.delete()
	return redirect('/lista_perros/')

def vista_login (request):
	usu =""
	cla =""
	if request.method == "POST":
		formulario = login_form(request.POST)
		if formulario.is_valid():
			usu = formulario.cleaned_data['usuario']
			cla = formulario.cleaned_data['clave']
			usuario = authenticate(username=usu, password=cla)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/')
			else:
				msj = "usuario o clave incorrectos"
	formulario = login_form()
	return render(request, 'login.html', locals())

def vista_logout (request):
	logout(request)
	return redirect('/logout/')

def vista_inicio(request):
	return render(request,'inicio.html',locals())

def vista_register (request):
	formulario = register_form()
	if request.method == 'POST':
		formulario = register_form(request.POST)
		if formulario.is_valid():
			usuario = formulario.cleaned_data['username']
			correo = formulario.cleaned_data['email']
			password_1 = formulario.cleaned_data['password_1']
			password_2 = formulario.cleaned_data['password_2']
			u = User.objects.create_user(username=usuario, email=correo, password=password_1)
			u.save()
			return render(request, 'bienvenido.html',locals())
		else:
			return render(request, 'register.html',locals())			
	return render(request, 'register.html',locals())
	
def vista_crear_perfil(request):
	formulario_1 = register_form()
	formulario_2 = perfil_form()
	if request.method == 'POST':
		formulario_1 = register_form(request.POST)
		formulario_2 = perfil_form(request.POST, request.FILES)
		if formulario_1.is_valid() and formulario_2.is_valid():
			usuario    = formulario_1.cleaned_data['username']
			correo 	   = formulario_1.cleaned_data['email']
			password_1 = formulario_1.cleaned_data['password_1']
			password_2 = formulario_1.cleaned_data['password_2']
			u = User.objects.create_user(username=usuario, email=correo, password=password_1)
			u.save()
			
			y = formulario_2.save(commit=False)
			y.user=u
			y.save()
			msg = "gracias por registrarse..."

	return render(request, 'crear_perfil.html',locals())				






		



						

