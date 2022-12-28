from django.contrib import admin

from appWeb.models import Prioridad,Tarea
# Register your models here.
class AdminPrioridad(admin.ModelAdmin):
    list_display=('nombre','created',)
    search_fields=('nombre',)
    list_filter = ('created',)
    date_hierarchy = "created"
    

admin.site.register(Prioridad,AdminPrioridad)


class AdminTarea(admin.ModelAdmin):
    list_display=('nombre',)
    search_fields=('nombre',)
    list_filter = ('created',)
    date_hierarchy = "created"
    

admin.site.register(Tarea,AdminTarea)