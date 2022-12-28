from django.shortcuts import render
from django.contrib.auth.models import User

from appWeb import models
# Create your views here.
def get_history(request):
    userActive=User.objects.get(username=request.user)
    escolaborador = models.Colaborador.objects.filter(nombre=request.user)
    
    if escolaborador.count()>0:
        tareas=models.Tarea.objects.filter(colaborador__nombre=userActive.username).order_by('created')
    else:
        tareas=models.Tarea.objects.filter(usuario=userActive.id).order_by('created')
        
    return render(request, 'historial/historial.html',{'tareas':tareas})