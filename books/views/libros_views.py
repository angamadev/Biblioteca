from books.models.libro_model import Libro
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from books.decorators import is_user_created_libro
from django.contrib import messages
from django.utils.translation import gettext as _


# Create your views here.
@method_decorator(login_required,name='dispatch')
class LibrosListView(ListView):
    model = Libro
    template_name = 'libros/libro.html'
    context_object_name = "libros"


@method_decorator(login_required,name='dispatch')
class LibrosDetailView(DetailView):
    model = Libro
    template_name = 'libros/libro_detail.html'
    context_object_name = "libros"
    

@method_decorator(login_required,name='dispatch')
class LibroCreateView(CreateView):
    model = Libro
    fields = [
        _("titulo"),
        _("isbn"),
        _("fecha_publicacion"),
        _("numero_paginas"),
        _("idioma"),
        _("editorial")

        ]
    template_name = 'libros/libro_create.html'
    context_object_name = "libros"
    
    def form_valid(self, form):
        form.instance.created_by= self.request.user
        messages.success(self.request, _('¡Libro Creado correctamente!'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('libro:list')
    

@method_decorator(is_user_created_libro,name='dispatch')
class LibroUpdateView(UpdateView):
    model = Libro
    fields = [
        _("titulo"),
        _("isbn"),
        _("fecha_publicacion"),
        _("numero_paginas"),
        _("idioma"),
        _("editorial"),
        ]
    
    template_name = 'libros/libro_update.html'
    context_object_name = "libros"
    
    def form_valid(self, form):
        messages.info(self.request, _('¡Libro Modificado correctamente!'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('libro:list')

    
@method_decorator(is_user_created_libro,name='dispatch')
class LibroDeteteView(DeleteView):
    model = Libro
    template_name = 'libros/libro_delete.html'
        
    def form_valid(self, form):
        messages.warning(self.request, _('¡Libro Borrado correctamente!'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('libro:list')


    
    