from books.models.editorial_model import Editorial
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from books.decorators import is_user_created_editorial
from django.contrib import messages
from django.utils.translation import gettext as _



# Create your views here.
@method_decorator(login_required,name='dispatch')
class EditorialListView(ListView):
    model = Editorial
    template_name = 'editoriales/editorial.html'
    context_object_name = "editoriales"
    
    
@method_decorator(login_required,name='dispatch')
class EditorialDetailView(DetailView):
    model = Editorial
    template_name = 'editoriales/editorial_detail.html'
    context_object_name = "editoriales"


@method_decorator(login_required,name='dispatch')
class EditorialCreateView(CreateView):
    model = Editorial
    fields = [
        _("nombre"),
        _("direccion"),
        _("ciudad"),
        _("estado"),
        _("pais"),
        _("codigo_postal"),
        _("telefono"),
        _("email"),
        _("sitio_web"),
        _("fecha_fundacion"),
        ]
    template_name = 'editoriales/editorial_create.html'
    context_object_name = "editorales"
    
    def form_valid(self, form):
        form.instance.created_by= self.request.user
        messages.success(self.request, '¡Editorial Creada correctamente!')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('editorial:list')

    
@method_decorator(is_user_created_editorial,name='dispatch')
class EditorialUpdateView(UpdateView):
    model = Editorial
    fields = [
        _("nombre"),
        _("direccion"),
        _("ciudad"),
        _("estado"),
        _("pais"),
        _("codigo_postal"),
        _("telefono"),
        _("email"),
        _("sitio_web"),
        _("fecha_fundacion"),
        _("created_by"),
        ]
    template_name = 'editoriales/editorial_update.html'
    context_object_name = "editoriales"
    
    def form_valid(self, form):
        messages.info(self.request, _('¡Editorial Modificada correctamente!'))
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('editorial:list')

    
    
@method_decorator(is_user_created_editorial,name='dispatch')
class EditorialDeteteView(DeleteView):
    model = Editorial
    template_name = 'editoriales/editorial_delete.html'
        
    def form_valid(self, form):
        messages.warning(self.request, _('¡Editorial Borrada correctamente!'))
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('editorial:list')
