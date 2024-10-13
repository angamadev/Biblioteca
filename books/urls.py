
from django.urls import path

from books.models.editorial_model import Editorial

from .views import (
    EditorialListView,
    EditorialDetailView,
    EditorialCreateView,
    EditorialUpdateView,
    EditorialDeteteView,
    AutoresListView,
    AutorDetailView,
    AutorCreateView,
    AutorUpdateView,
    AutorDeteteView,
    LibrosListView,
    LibrosDetailView,
    LibroCreateView,
    LibroUpdateView, 
    LibroDeteteView,
    
)   

app_name = "books"

urlpatterns = [
    path("libros/",LibrosListView.as_view(), name='libro_list'),
    path("libros/<pk>/", LibrosDetailView.as_view(), name="libro_detail"),
    path("libro/nuevo/", LibroCreateView.as_view(), name="libro_create"),
    path("libros/editar/<pk>", LibroUpdateView.as_view(), name="libro_update"),
    path("libros/eliminar/<pk>", LibroDeteteView.as_view(), name="libro_delete"),
    path("autores/", AutoresListView.as_view(), name='autor_list'),
    path("autores/<pk>/", AutorDetailView.as_view(), name="autor_detail"),
    path("autor/nuevo/", AutorCreateView.as_view(), name="autor_create"),
    path("autores/editar/<pk>", AutorUpdateView.as_view(), name="autor_update"),
    path("autores/eliminar/<pk>", AutorDeteteView.as_view(), name="autor_delete"),
    path("editoriales/", EditorialListView.as_view(), name='editorial_list'),
    path("editoriales/<pk>/", EditorialDetailView.as_view(), name="editorial_detail"),
    path("editorial/nuevo/", EditorialCreateView.as_view(), name="editorial_create"),
    path("editoriales/editar/<pk>", EditorialUpdateView.as_view(), name="editorial_update"),
    path("editoriales/eliminar/<pk>", EditorialDeteteView.as_view(), name="editorial_delete"),
]
