from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.



class Colaborador(models.Model):
    nombre= models.TextField(max_length=50,null=True,blank=True)
    apellido= models.TextField(max_length=50,null=True,blank=True)
    usuario=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    telefono=models.TextField(max_length=20,null=True,blank=True)
    correo = models.EmailField(max_length=254,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    #colaborador = models.BooleanField(default=True)
 
    
    
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table='colaborador'
        verbose_name='colaborador'
        verbose_name_plural='colaboradores'
        ordering=['id']
        