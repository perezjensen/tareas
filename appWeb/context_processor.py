from django.contrib.auth.models import User
from appWeb import models
from datetime import date




def totalTareas(request):
    
    if request.user.is_authenticated:
        escolaborador = models.Colaborador.objects.filter(nombre=request.user)
        if escolaborador.count()>0:
            colaborador=True
        else:
            colaborador=False
            
        userActive=User.objects.get(username=request.user)
        kanban=models.Kanban.objects.get(pk=2)
        
        if colaborador==False:
            tarea=models.Tarea.objects.filter(usuario=userActive.id).exclude(kanban=kanban).exclude(estado=False)
        else:
            tarea=models.Tarea.objects.filter(colaborador__nombre=userActive.username).exclude(kanban=kanban).exclude(estado=False)
            
        #valido si el usuario tiene tareas 
        if tarea.count()==0:
            return {
            'totaltareas':0,
            'tareasHechas':0,
            'porcentaje':0,
            'colaborador':colaborador,}
            
        else:
            #tareas hechas durante el dia 
            if colaborador==False:
                hechosHoy=models.Tarea.objects.filter(usuario=userActive.id,fechaHecho=date.today())
            else:
                hechosHoy=models.Tarea.objects.filter(colaborador__nombre=userActive.username,fechaHecho=date.today())

            procentaje=int(hechosHoy.count())*100
            poprcentajeTotal=procentaje/int(tarea.count())
            return {
                'totaltareas':tarea.count,
                'tareasHechas':hechosHoy.count,
                'porcentaje':int(poprcentajeTotal),
                'colaborador':colaborador,}
    else:
        return {
            'totaltareas':0,
            'tareasHechas':0,
            'porcentaje':0,
            'colaborador':False,}  