
from django.urls import path
from productos import views



urlpatterns = [
    path('producto/',views.get_product, name="verProdutos"),
    path('producto/nuevo',views.new_product, name="nuevoProducto"),
    path('producto/categoria',views.get_category, name="verCategorias"),
    path('producto/categoria/nueva',views.new_category, name="nuevaCategoria"),
    path('producto/crear',views.created_product, name="crearProducto"),
    path('producto/categoria/crear',views.created_category, name="crearCategoria"),
    path('producto/editar/<int:id>',views.edit_product, name="editarProducto"),
    path('producto/eliminar/<int:id>',views.delete_product, name="eliminarProducto"),
    path('producto/categoria/editar/<int:id>',views.edit_category, name="editarCategoria"),
    path('producto/categoria/eliminar/<int:id>',views.delete_category, name="borrarCategoria"),
    path('producto/ver/<int:id>',views.view_product, name="verproducto"),

]
