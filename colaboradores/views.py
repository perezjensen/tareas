from django.shortcuts import render,redirect
from django.http import HttpResponse
from appWeb import models
from colaboradores import models
from appWeb import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages

from django.db.models import F, Sum, FloatField
# Create your views here.
def get_collaborators(request):
    if request.user.is_authenticated:
        
        userActive=User.objects.get(username=request.user)
        colaborador= models.Colaborador.objects.filter(usuario=userActive.id)
        
    
        
        return render(request,'colaboradores/verColaboradores.html',{'colaboradores':colaborador})
    else:
        return redirect('/')
    
def create_collaborator(request):
    
    #creo el form de registro  
    form= UserCreationForm()    
    #evaluo si hay un metodo post
    if request.method=="POST":
        #instacio los datos del formulario
        form= UserCreationForm(request.POST)
        if form.is_valid():
            Usuario = form.save()
            #a partir de aqui agrego los datos adicionales para que este usuario se vuelva colaborador 
            userActive=User.objects.get(username=request.user)
            colaborador = models.Colaborador()
            colaborador.usuario=userActive
            colaborador.nombre=form.cleaned_data.get('username')
            #colaborador.colaborador=True
            colaborador.save()
            return redirect('/colaboradores/')
        else:
            messages.error(request, "Datos Herrados, Por favor verfique que cumple con todos los pasos")
            return render(request,"colaboradores/crearColaborador.html",{'form':form})
    

    return render(request,'colaboradores/crearColaborador.html',{'form':form})
    

def change_collaborator(request,id_task,id_collaborator):
    colaboradores_exis = []
    tarea = models.Tarea.objects.get(pk=id_task)
    if tarea.colaborador.count() > 0:
        for i in tarea.colaborador.all():
            colaboradores_exis.append(i)
    
    collaborator =models.Colaborador.objects.get(pk=id_collaborator)
    colaboradores_exis.append(collaborator)
    
    
    tarea.colaborador.set(colaboradores_exis) 
    tarea.save()
    return redirect('/tareas')


def new_collaborator(request):
    if request.method=="POST":
        nombre=request.POST.get('nombre')
        correo=request.POST.get('correo')
        telefono=request.POST.get('telefono')
        contrasena=request.POST.get('contrasena')
        if nombre=='':
            return redirect('/colaboradores/nuevo')
        elif correo=='':
            return redirect('/colaboradores/nuevo')
        elif contrasena=='':
            return redirect('/colaboradores/nuevo')
        else:
            colaborador = models.Colaborador()
            colaborador.nombre=nombre
            colaborador.correo=correo
            colaborador.telefono=telefono
            colaborador.save()
           
            return redirect('/colaboradores/')
        
def delete_collaborator(request,id):
    models.Colaborador.objects.filter(pk=id).delete()
    return redirect('/colaboradores/')