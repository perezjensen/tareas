from xml.dom.minidom import Document
from django.urls import path
from appWeb import views

from django.conf import settings # se utiliza para la carga de imagen 
from django.conf.urls.static import static # se utiliza para la carga de imagen

urlpatterns = [
    path('tareas/',views.get_task_admin, name="tareas"),
    path('anular/<int:id>/',views.cancel_task, name='anular_tarea'),
    path('activar/<int:id>/',views.active_task, name='activar_tarea'),
    path('actualizar/',views.update_task_all, name='actualizar_todas-tareas'),
    path('prioridad/actualizar/<int:id_task>/<int:id_priority>',views.change_priority, name='cambiar_prioridad'),
    path('abonar/',views.add_deposit, name='agregar-deposito'),
    path('finalizar/<int:id_task>',views.task_finish, name="hecho"),
    path('revertir/<int:id>/',views.task_revertir, name="revertir_tarea"),
    path('guardar/',views.task_save, name="guardar"),
    path('borrar/abono/<int:id>/',views.borrarAbono, name='borrarAbono'),
    
]
#añadimos a las url las url para buscar las imagenes 
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )