from books.models.autor_model import Autor
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from books.decorators import is_user_created_autor
from django.contrib import messages
from django.utils.translation import gettext as _



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
        _("nombre"),
        _("apellido"),
        _("fecha_nacimiento"),
        _("nacionalidad"),
        _("biografia"),
        _("email"),
        _("telefono"),
        _("sitio_web"),
        _("premios"),
        ]
    template_name = 'autores/autor_create.html'
    context_object_name = "autores"
    
    def form_valid(self, form):
        form.instance.created_by= self.request.user
        messages.success(self.request, _('¡El autor ha sido Creado correctamente!'))
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('autor:list')

    
@method_decorator(is_user_created_autor,name='dispatch')
class AutorUpdateView(UpdateView):
    model = Autor
    fields = [
        _("nombre"),
        _("apellido"),
        _("fecha_nacimiento"),
        _("nacionalidad"),
        _("biografia"),
        _("email"),
        _("telefono"),
        _("sitio_web"),
        _("premios"),
        ]
    template_name = 'autores/autor_update.html'
    context_object_name = "autores"
    
    def form_valid(self, form):
        messages.info(self.request, _('¡El autor ha sido Modificado correctamente!'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('autor:list')

    
    
@method_decorator(is_user_created_autor,name='dispatch')
class AutorDeteteView(DeleteView):
    model = Autor
    template_name = 'autores/autor_delete.html'
    
    def form_valid(self, form):
        messages.warning(self.request, _('¡El autor se Elimino correctamente!'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('autor:list')

