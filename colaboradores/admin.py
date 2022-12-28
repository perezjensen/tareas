from django.contrib import admin

# Register your models here.

from colaboradores.models import Colaborador
# Register your models here.
class AdminColaborador(admin.ModelAdmin):
    list_display=('nombre','apellido','usuario','telefono','correo')
    search_fields=('nombre',)
    list_filter = ('created',)
    date_hierarchy = "created"
    

admin.site.register(Colaborador,AdminColaborador)


