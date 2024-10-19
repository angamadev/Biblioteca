from books.models.editorial_model import Editorial
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from books.decorators import is_user_created_editorial



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
        "nombre",
        "direccion",
        "ciudad",
        "estado",
        "pais",
        "codigo_postal",
        "telefono",
        "email",
        "sitio_web",
        "fecha_fundacion",
        ]
    template_name = 'editoriales/editorial_create.html'
    success_url = reverse_lazy('editorial:list')
    context_object_name = "editorales"
    
    def form_valid(self, form):
        form.instance.created_by= self.request.user
        return super().form_valid(form)
    
@method_decorator(is_user_created_editorial,name='dispatch')
class EditorialUpdateView(UpdateView):
    model = Editorial
    fields = [
        "nombre",
        "direccion",
        "ciudad",
        "estado",
        "pais",
        "codigo_postal",
        "telefono",
        "email",
        "sitio_web",
        "fecha_fundacion",
        "created_by",
        ]
    template_name = 'editoriales/editorial_update.html'
    success_url = reverse_lazy('editorial:list')
    context_object_name = "editoriales"
    
    
@method_decorator(is_user_created_editorial,name='dispatch')
class EditorialDeteteView(DeleteView):
        model = Editorial
        success_url = reverse_lazy('editorial:list')
        template_name = 'editoriales/editorial_delete.html'
        