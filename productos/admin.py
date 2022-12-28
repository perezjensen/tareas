from django.contrib import admin

# Register your models here.
from productos.models import Categoria, Producto
# Register your models here.

class AdminCategoria(admin.ModelAdmin):
    list_display=('nombre','created')
    search_fields=('nombre',)
    list_filter = ('created',)
    date_hierarchy = "created"

class AdminProducto(admin.ModelAdmin):
    list_display=('created','nombre','precio','get_categoria',)
    search_fields=('nombre','get_categoria',)
    list_filter = ('created','categoria',)
    date_hierarchy = "created"
    
    
admin.site.register(Categoria,AdminCategoria)
admin.site.register(Producto,AdminProducto)

