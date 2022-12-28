from django.shortcuts import render, redirect
from django.http import HttpResponse
from appWeb import models
from django.contrib import messages
from django.db.models import Sum
from django.contrib.auth.models import User

#hace busquedas complejas con or en filter 
from django.db.models import Q

from django.db.models import F, Sum, FloatField
#importo los formularios 
from appWeb import forms

# Create your views here.
def get_task_admin(request):
    #cargo los formularios
    formularioActualizar = forms.FormularioTareaActualizar()
    
    #no muestro nada si no esta autenticado
    if request.user.is_authenticated:
        escolaborador = models.Colaborador.objects.filter(nombre=request.user)
        if escolaborador.count()>0:
            userActive=User.objects.get(username=request.user)
            kanban=models.Kanban.objects.get(pk=2)
            tarea=models.Tarea.objects.filter(colaborador__nombre=userActive.username).exclude(kanban=kanban).exclude(estado=False)
            kanban = models.Kanban.objects.all()
            return render(request, 'appWeb/index.html',{'tareas':tarea,
                                                        'colaborador':True,
                                                        'kanbans':kanban,

                                                        
                                                        })
           
        
        else:
        
            userActive=User.objects.get(username=request.user)
            kanban=models.Kanban.objects.get(pk=2)
            tarea=models.Tarea.objects.filter(usuario=userActive.id).exclude(kanban=kanban).exclude(estado=False).annotate(debePrecio=F('precio')-F('abono')).annotate(debeProducto=F('producto__precio')-F('abono'))
            prioridad=models.Prioridad.objects.all()
            kanban = models.Kanban.objects.all()
            producto = models.Producto.objects.all()
            colaborador= models.Colaborador.objects.filter(usuario=userActive.id)

            
        
        
            
            return render(request, 'appWeb/index.html',{'tareas':tarea,
                                                        'prioridades':prioridad,
                                                        'kanbans':kanban,
                                                        'productos':producto,
                                                        'colaboradores':colaborador,
                                                        'actualizarForm':formularioActualizar,
                                                        'colaborador':False,
                                                        })
    else:
        return redirect('/')
        
    

def cancel_task(request,id):
    models.Tarea.objects.filter(pk=id).update(estado=False)
    messages.success(request, "La Tarea ha sido Anulada")
    return redirect(f'/tareas?id={id}')

def active_task(request,id):
    models.Tarea.objects.filter(pk=id).update(estado=True)
    return redirect('/tareas')


def borrarAbono(request,id):
    models.Tarea.objects.filter(pk=id).update(abono=0)
    return redirect('/tareas')
    

def update_task_all(request):
    
    if request.method=="POST":
        
        #guardo el id de la tarea 
        idTask = request.POST['id']
        if idTask.isnumeric()==False:
            idTask=0
        
        #consulta en tabla productos many to many 
        productos = request.POST.getlist('productos')
        if productos=='':
            productos=[0,]
        producto=models.Producto.objects.filter(pk__in=productos)
        
        #Guardo el abono  
        abono = request.POST['abono']
        if abono=='' or abono.isnumeric()==False:
            #consulto lo que tengo guardado en abono para que no sobrescriba el valor 
            tareaAbono=models.Tarea.objects.get(pk=int(idTask))
            abono=int(tareaAbono.abono)
        else:
            #consulto lo que hay en abono para sumarlo al nuevo abono
            tareaAbono=models.Tarea.objects.get(pk=int(idTask))
            abono=int(abono)+int(tareaAbono.abono)
            
        #Guardo el nombre     
        nombre = request.POST['nombre']
        if nombre=='':
            #consulto lo que tengo guardado ennombre para que no sobrescriba el valor 
            tareanombre=models.Tarea.objects.get(pk=int(idTask))
            nombre=tareanombre.nombre


        #consulta en tabla prioridad
        prioridad  = request.POST['prioridad']
        if prioridad.isnumeric()==False:
            prioridad=2   
        prioridad_get=models.Prioridad.objects.get(pk=prioridad)
        
        #consulta en tabla colaboradores many to many
        colaboradores= request.POST.getlist('colaboradores')
        if colaboradores=='' :
                colaboradores=[0,]
        colaborador=models.Colaborador.objects.filter(pk__in=colaboradores)
        
        #busco si ya precio tienen un valor asignado y lo conservo 
        precio = request.POST['precio']
        if precio=='':
            tareaprecio=models.Tarea.objects.get(pk=int(idTask))
            precio=int(tareaprecio.precio)
    
        
        tarea=models.Tarea.objects.get(pk=int(idTask))
        
        tarea.producto.set(producto)
        
         
        tarea.abono=abono
        tarea.nombre = nombre
        tarea.prioridad=prioridad_get
        tarea.colaborador.set(colaboradores)
        tarea.precio=precio
        
        tarea.save()
        
        
           
    return redirect('/tareas')

def change_priority(request,id_task,id_priority):
    
    tarea = models.Tarea.objects.get(pk=id_task)
    prioridad =models.Prioridad.objects.get(pk=id_priority)
    tarea.prioridad=prioridad
    tarea.save()
    
    return redirect('/tareas')

def add_deposit(request):
    if request.method == "POST":
        
        idTask = request.POST['id']
        if idTask.isnumeric()==False:
            idTask=0
            
        #Guardo el abono  
        abono = request.POST['abono']
        tareaAbono=models.Tarea.objects.get(pk=int(idTask))
        if abono=='' or abono.isnumeric()==False:
            #consulto lo que tengo guardado en abono para que no sobrescriba el valor 
            abono=int(tareaAbono.abono)
        else:
            #consulto lo que hay en abono para sumarlo al nuevo abono
            abono=int(abono)+int(tareaAbono.abono)
   
    tareaAbono.abono = abono
    tareaAbono.save()
    
    return redirect('/tareas')

def task_finish(request,id_task):
    
    tarea = models.Tarea.objects.get(pk=id_task)
    kanban =models.Kanban.objects.get(pk=2)
    tarea.kanban=kanban
    tarea.culminado=False
    tarea.save()
    
    messages.warning(request, "La Tarea ha sido Culminada")
    return redirect(f'/tareas?id={id_task}')

def task_revertir(request,id):
    tarea = models.Tarea.objects.get(pk=id)
    kanban =models.Kanban.objects.get(pk=1)
    tarea.kanban=kanban
    tarea.culminado=True
    tarea.save()
    return redirect('/tareas')

def task_save(request):
    if request.method=="POST":
        
        #No Guardo nada si la tarea esta vacia 
        mensaje = request.POST['mensaje']
        if mensaje=='':
            return redirect('/tareas')
        
        #recibo los datos 
        productos = request.POST.getlist('producto')
        prioridades = request.POST.get('prioridad')
        prioridad=models.Prioridad.objects.get(pk=prioridades)
        colaborador=request.POST.getlist('colaborador')
        abono=request.POST.get('abono')
        precio=request.POST.get('precio')
        
        #si abono viene vacio agrego un 0
        if abono=='':
            abono=0
            
        #si precio viene vacio agrego un 0
        if precio=='':
            precio=0
        
        #consulto la id del kanban de por hacer para guardarlo automatico
        kanban= models.Kanban.objects.get(pk=3)    
        
        #guardo solo el mensaje 
        tarea=models.Tarea() 
        tarea.nombre = mensaje
        tarea.prioridad=prioridad
        tarea.abono=abono
        tarea.precio=precio
        tarea.kanban=kanban
        tarea.save()
        
        #guardo el usuario
        userActive=User.objects.filter(username=request.user)
        ultimaTarea=models.Tarea.objects.last()
        ultimaTarea.usuario.set(userActive)
        
        #agrego los productos 
        if len(productos)>0:
            producto=models.Producto.objects.filter(pk__in=productos)
            ultimaTarea.producto.set(producto)
            
        #cagregar Colaborador        
        if len(colaborador)>0:
            colaboradores=models.Colaborador.objects.filter(pk__in=colaborador)
            ultimaTarea.colaborador.set(colaboradores)
  
           
  
    return redirect('/tareas')

