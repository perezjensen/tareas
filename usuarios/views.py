from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
#importo Usuarios
from django.contrib.auth.models import User
# Create your views here.
def login_user(request):
    
    if request.method=="POST":
        form =AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get('username')
            contrasena=form.cleaned_data.get('password')
            #valida si existe el usuario 
            usuario=authenticate(username=nombre_usuario,password=contrasena)
            if usuario is not None:
                login(request,usuario)
                return redirect('/tareas/')
            else:
                messages.error(request, "Datos No encontrados")
                return redirect('/')
        else:
            messages.error(request, "Informacion Incorrecta")
             
           
    form = AuthenticationForm()    
    return render(request, 'usuarios/login.html',{'form':form})

def register_user(request):
    
    #creo el form de registro  
    form= UserCreationForm()    
    #evaluo si hay un metodo post
    if request.method=="POST":
        #instacio los datos del formulario
        form= UserCreationForm(request.POST)
        if form.is_valid():
            Usuario = form.save()
            login(request, Usuario)
            return redirect('/tareas/')
        else:
            messages.error(request, "Datos Herrados, Por favor verfique que cumple con todos los pasos")
            return render(request,"usuarios/registro.html",{'form':form})
    
    return render(request, 'usuarios/registro.html',{'form':form})

def cerrar_sesion(request):
    logout(request)
    return redirect('/')