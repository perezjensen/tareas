from django.shortcuts import render, redirect
from kanban import models
from appWeb import models
from datetime import datetime, date
from django.contrib.auth.models import User

# Create your views here.
def get_kanban(request):
    kanban=models.Kanban.objects.all()
    userActive=User.objects.get(username=request.user)
    #por hacer 
    kPorhacer=models.Kanban.objects.get(pk=3)
    porHacer = models.Tarea.objects.exclude(estado=False).filter(kanban=kPorhacer).filter(usuario=userActive.id)
    
    
    #en Proceso
    kProceso=models.Kanban.objects.get(pk=1)
    enProceso = models.Tarea.objects.exclude(estado=False).filter(kanban=kProceso).filter(usuario=userActive.id)
    
    
    #Hecho
    kHecho=models.Kanban.objects.get(pk=2)
    hecho = models.Tarea.objects.exclude(estado=False).filter(kanban=kHecho).filter(usuario=userActive.id).order_by('fechaHecho')
    
    return render(request, 'kanban/tablero.html',{'porHacer':porHacer,
                                                  'enProceso':enProceso,
                                                  'hecho':hecho[0:10],
                                                  'kanbans':kanban,
                                                  })

def change_kanban(request,id_task,id_kanban):
    
    tarea = models.Tarea.objects.get(pk=id_task)
    kanban =models.Kanban.objects.get(pk=id_kanban)
    tarea.kanban=kanban
    
    #si es igual a hecho 
    if id_kanban==2:
        tarea.culminado=False
        tarea.fechaHecho=date.today()
        
        
    tarea.save()
    
    return redirect('/tareas')


def change_tablero(request):
    if request.method=="POST":
        id_task= request.POST.get('id')
        id_kanban= request.POST.get('kanban')
        
        tarea = models.Tarea.objects.get(pk=id_task)
        kanban =models.Kanban.objects.get(pk=id_kanban)
        tarea.kanban=kanban
        
        if id_kanban==2:
            tarea.culminado=False
            tarea.fechaHecho=date.today()
            
        tarea.save()
        
        return redirect('/tablero/')