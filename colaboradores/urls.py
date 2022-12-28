
from django.urls import path
from colaboradores import views



urlpatterns = [
    path('colaboradores/',views.get_collaborators, name="verColaborador"),
    path('colaboradores/nuevo',views.create_collaborator, name="nuevoColaborador"),
    path('colaboradores/cambiar/<int:id_task>/<int:id_collaborator>',views.change_collaborator, name="cambiarColaborador"),
    path('colaboradores/crear',views.new_collaborator, name="crearColaborador"),
    path('colaboradores/eliminar/<int:id>',views.delete_collaborator, name="borrarColaborador"),
]
