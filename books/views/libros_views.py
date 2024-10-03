from django.shortcuts import render
from books.models.libro_model import Libro

# Create your views here.
def libros_view(request):
    libros = Libro.objects.all()
    context = {
        'libros' : libros,
    }
    return render(request, 'libros/libro.html', context)

def libro_detail(request, id):
    libro = Libro.objects.get(pk=id)
    
    context = {
        'libro' : libro,
    }
    return render(request, 'libros/libro_detail.html', context)