from django import forms
from .models import Producto, Categoria


class UploadImageForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['imagen']
        
        
        
class UploadCategorias(forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields = ['nombre']