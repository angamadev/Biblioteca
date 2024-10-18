from books.forms.editorial_form import EditorialCreate,EditorialCreateModelforms
from books.models.editorial_model import Editorial
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy


# Create your views here.
class EditorialListView(ListView):
    model = Editorial
    template_name = 'editoriales/editorial.html'
    context_object_name = "editoriales"
    
    
class EditorialDetailView(DetailView):
    model = Editorial
    template_name = 'editoriales/editorial_detail.html'
    context_object_name = "editoriales"


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
        "created_by",
        ]
    template_name = 'editoriales/editorial_create.html'
    success_url = reverse_lazy('editorial:list')
    context_object_name = "editorales"
    
    
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
    
    
class EditorialDeteteView(DeleteView):
        model = Editorial
        success_url = reverse_lazy('editorial:list')
        template_name = 'editoriales/editorial_delete.html'
        