from django.shortcuts import render,redirect
from productos import models
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import UploadImageForm, UploadCategorias

# Create your views here.
@login_required
def get_product(request):
    produto=models.Producto.objects.all()
    
    return render(request, 'productos/verProducto.html',{'productos':produto})

@login_required
def new_product(request):
    form = UploadImageForm()
    categoria=models.Categoria.objects.all()
    return render(request, 'productos/crearProducto.html',{'categorias':categoria,'form':form})

@login_required
def created_product(request):
    
    if request.method=="POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            imagen=form.cleaned_data.get('imagen')
            if imagen==None:
                imagen='false'
                
        
        nombre=request.POST.get('nombre')
        categorias=request.POST.getlist('categoria')
        precio=request.POST.get('precio')
        
        producto = models.Producto()
        producto.nombre=nombre
        producto.precio=precio
        producto.imagen=imagen
        producto.save()
        
        #agrego las categorias
        if len(categorias)>0:
            categoria=models.Categoria.objects.filter(pk__in=categorias)
            ultimoProducto=models.Producto.objects.last()
            ultimoProducto.categoria.set(categoria)
            
     
    
    
    return redirect('/producto/')
    
@login_required
def get_category(request):
    categoria = models.Categoria.objects.all()
    
    return render(request, 'productos/categoriasVer.html',{'categorias':categoria})
@login_required
def new_category(request):
    form = UploadCategorias()
    return render(request, 'productos/nuevaCategoria.html',{'form':form})

@login_required
def created_category(request):
    if request.method=="POST":
        form = UploadCategorias(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/producto/categoria')
        else:
            return redirect('/producto/categoria/nueva')
 
        
@login_required
def edit_product(request,id):
    
    form = UploadImageForm()
    
    producto=models.Producto.objects.get(pk=id)
    categoria=models.Categoria.objects.all()
    
    if request.method=="POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            imagen=form.cleaned_data.get('imagen')
            
            if imagen==None:
                imagen=producto.imagen
                
            producto.imagen=imagen
            producto.save()
        
            
        
        producto=models.Producto.objects.get(pk=id)
        nombre=request.POST.get('nombre')
        if nombre=='':
            nombre=producto.nombre
        categorias=request.POST.getlist('categoria')
        if categorias==[]:
            categorias=producto.categoria.all()
            
        precio=request.POST.get('precio')
        if precio=='':
            precio=producto.precio
        
        producto.nombre=nombre
        producto.categoria.set(categorias)
        producto.precio=precio
        producto.save()
        
        return redirect('/producto/')
        
    
    return render(request, 'productos/editarproducto.html',{'producto':producto,
                                                            'categorias':categoria,
                                                            'formulario':form,
                                                            })
def delete_product(request,id):
    models.Producto.objects.filter(pk=id).delete()
    return redirect('/producto/')


def edit_category(request,id):
    form= UploadCategorias()
    categoria=models.Categoria.objects.get(pk=id)
    if request.method=="POST":
        form= UploadCategorias(request.POST)
        if form.is_valid():
            nombre=form.cleaned_data.get('nombre')
            categoria.nombre=nombre
            categoria.save()
            return redirect('/producto/categoria')
         
    
    return render(request, 'productos/editarcategoria.html', {'form':form,'categoria':categoria})

def delete_category(request,id):
    models.Categoria.objects.filter(pk=id).delete()
    return redirect('/producto/categoria')

def view_product(request,id):
    categoria=models.Categoria.objects.all()
    producto= models.Producto.objects.get(pk=id)
    
    form = UploadImageForm()
    
    producto=models.Producto.objects.get(pk=id)
    categoria=models.Categoria.objects.all()
    
    if request.method=="POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            imagen=form.cleaned_data.get('imagen')
            
            if imagen==None:
                imagen=producto.imagen
                
            producto.imagen=imagen
            producto.save()
        
            
        
        producto=models.Producto.objects.get(pk=id)
        nombre=request.POST.get('nombre')
        if nombre=='':
            nombre=producto.nombre
        categorias=request.POST.getlist('categoria')
        if categorias==[]:
            categorias=producto.categoria.all()
            
        precio=request.POST.get('precio')
        if precio=='':
            precio=producto.precio
        
        producto.nombre=nombre
        producto.categoria.set(categorias)
        producto.precio=precio
        producto.save()
        
        return redirect('/producto/')
    
    return render(request, 'productos/productoindividual.html',{'producto':producto,'categorias':categoria,'formulario':form})