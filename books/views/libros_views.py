from django.shortcuts import render
from books.models.libro_model import Libro
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy


# Create your views here.
# @method_decorator(login_required,name='dispatch')
class LibrosListView(ListView):
    model = Libro
    template_name = 'libros/libro.html'
    context_object_name = "libros"

class LibrosDetailView(DetailView):
    model = Libro
    template_name = 'libros/libro_detail.html'
    context_object_name = "libros"
    
class LibroCreateView(CreateView):
    model = Libro
    fields = [
        "titulo",
        "isbn",
        "fecha_publicacion",
        "numero_paginas",
        "idioma",
        "editorial"

        ]
    template_name = 'libros/libro_create.html'
    success_url = reverse_lazy('books:libro_list')
    context_object_name = "libros"
    
class LibroUpdateView(UpdateView):
    model = Libro
    fields = [
        "titulo",
        "isbn",
        "fecha_publicacion",
        "numero_paginas",
        "idioma",
        "editorial"

        ]
    template_name = 'libros/libro_update.html'
    success_url = reverse_lazy('books:libro_list')
    context_object_name = "libros"
    
class LibroDeteteView(DeleteView):
        model = Libro
        success_url = reverse_lazy('books:libro_list')
        template_name = 'libros/libro_delete.html'
    
# def libros_view(request):
#     libros = Libro.objects.all()
#     context = {
#         'libros' : libros,
#     }
#     return render(request, 'libros/libro.html', context)

# def libro_detail(request, id):
#     libro = Libro.objects.get(pk=id)
    
#     context = {
#         'libro' : libro,
#     }
#     return render(request, 'libros/libro_detail.html', context)
