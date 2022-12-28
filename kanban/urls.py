
from django.urls import path
from kanban import views



urlpatterns = [
    path('tablero/',views.get_kanban, name="verTablero"),
    path('kanban/cambiar/<int:id_task>/<int:id_kanban>',views.change_kanban, name="cambiarEstado"),
    path('tablero/cambiar',views.change_tablero, name="cambiarTablero")
]
