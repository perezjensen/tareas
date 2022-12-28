from django.db import models

from django.contrib.auth.models import User
from productos.models import Producto
from kanban.models import Kanban
from colaboradores.models import Colaborador

from django.db.models import F, Sum, FloatField
# Create your models here.


# Create your models here.
class Prioridad(models.Model):
    nombre= models.TextField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table='prioridad'
        verbose_name='prioridad'
        verbose_name_plural='prioridades'
        ordering=['id']

class Tarea(models.Model):
    nombre= models.TextField(max_length=50)
    usuario=models.ManyToManyField(User)
    colaborador=models.ManyToManyField(Colaborador,null=True,blank=True)
    prioridad=models.ForeignKey(Prioridad, on_delete=models.CASCADE,null=True,blank=True)
    producto = models.ManyToManyField(Producto,null=True,blank=True)
    kanban = models.ForeignKey(Kanban, on_delete=models.CASCADE, null=True,blank=True)
    abono = models.FloatField(default=0,null=True,blank=True)
    estado = models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    precio = models.FloatField(default=0,null=True,blank=True)
    retribucion=models.BooleanField(null=True,blank=True)
    #eliminar este campo despues 
    culminado=models.BooleanField(default=True)
    fechaHecho=models.DateTimeField(null=True,blank=True)
    fechaProceso=models.DateTimeField(null=True,blank=True)
    
    
    
    def __str__(self):
        return self.nombre
    

    
    class Meta:
        db_table='tarea'
        verbose_name='tarea'
        verbose_name_plural='tareas'
        ordering=['id']
        