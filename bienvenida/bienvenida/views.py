from django.shortcuts import render
from . models import Producto

def lista_producto(request):
    productos = producto.objects.all()
    return render(request, 'productos_listas.html', {'productos': productos})