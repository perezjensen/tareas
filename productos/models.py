from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre= models.TextField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table='categorias'
        verbose_name='categoria'
        verbose_name_plural='categorias'
        ordering=['id']
        
class Producto(models.Model):
    nombre= models.TextField(max_length=50)
    precio= models.FloatField()
    categoria=models.ManyToManyField(Categoria)
    created=models.DateTimeField(auto_now_add=True)
    imagen=models.ImageField(upload_to='productos',null=True,blank=True)
    
    def get_categoria(self):
            return ",".join([str(p) for p in self.categoria.all()])
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table='productos'
        verbose_name='producto'
        verbose_name_plural='productos'
        ordering=['id']
    