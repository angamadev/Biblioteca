from books.models.autor_model import Autor
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(login_required,name='dispatch')

class AutoresListView(ListView):
    model = Autor
    template_name = 'autores/autor.html'
    context_object_name = "autores"


@method_decorator(login_required,name='dispatch')

class AutorDetailView(DetailView):
    model = Autor
    template_name = 'autores/autor_detail.html'
    context_object_name = "autores"


@method_decorator(login_required,name='dispatch')

class AutorCreateView(CreateView):
    model = Autor
    fields = [
        "nombre",
        "apellido",
        "fecha_nacimiento",
        "nacionalidad",
        "biografia",
        "email",
        "telefono",
        "sitio_web",
        "premios",
        ]
    template_name = 'autores/autor_create.html'
    success_url = reverse_lazy('autor:list')
    context_object_name = "autores"
    
    
@method_decorator(login_required,name='dispatch')

class AutorUpdateView(UpdateView):
    model = Autor
    fields = [
        "nombre",
        "apellido",
        "fecha_nacimiento",
        "nacionalidad",
        "biografia",
        "email",
        "telefono",
        "sitio_web",
        "premios",
        ]
    template_name = 'autores/autor_update.html'
    success_url = reverse_lazy('autor:list')
    context_object_name = "autores"
    
    
@method_decorator(login_required,name='dispatch')

class AutorDeteteView(DeleteView):
    model = Autor
    success_url = reverse_lazy('autor:list')
    template_name = 'autores/autor_delete.html'
    
    