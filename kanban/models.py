from django.db import models



class Kanban(models.Model):
    estado= models.TextField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.estado
    
    class Meta:
        db_table='kanban'
        verbose_name='kanban'
        verbose_name_plural='kanbans'
        ordering=['id']


