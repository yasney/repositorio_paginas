from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def vista_about(request):
	
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
	return render(request,'about.html',locals())	

def vista_lista_producto(request):
	lista = Producto.objects.filter()
	return render (request, 'lista_producto.html',locals())

def vista_agregar_producto(request):
	if request.method == 'POST':
		formulario = agregar_producto_form(request.POST,request.FILES)
		if formulario.is_valid():
			prod=formulario.save(commit = False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect ('/lista_producto/')
	else:
		formulario = agregar_producto_form()
	return render(request,'agregar_producto.html',locals())

def vista_ver_producto(request,id_product):
	p = Producto.objects.get(id = id_product)
	return render(request,'ver_producto.html',locals())

def vista_editar_producto(request,id_product):
	prod = Producto.objects.get(id = id_product)
	if request.method == "POST":
		formulario = agregar_producto_form(request.POST, request.FILES,instance = prod)
		if formulario.is_valid():
			prod = formulario.save()
			return redirect('/lista_producto')
	else:	
		formulario = agregar_producto_form(instance = prod)
		return render(request,'agregar_producto.html',locals())

def vista_eliminar_producto(request, id_product):
	prod = Producto.objects.get(id = id_product)
	prod.delete()
	return redirect('/lista_producto')

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








 