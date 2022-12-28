
from django.urls import path
from usuarios import views



urlpatterns = [
    path('',views.login_user, name="login"),
    path('registro/',views.register_user, name="register"),
    path('cerrar/',views.cerrar_sesion, name="cerrarSession"),

]
