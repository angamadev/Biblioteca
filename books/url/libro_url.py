
from django.urls import path

from books.views.libros_views import (
    LibrosListView,
    LibrosDetailView,
    LibroCreateView,
    LibroUpdateView, 
    LibroDeteteView,
    
)   

app_name = "libro"

urlpatterns = [
    path("lista/",LibrosListView.as_view(), name='list'),
    path("detalle/<pk>/", LibrosDetailView.as_view(), name="detail"),
    path("nuevo/", LibroCreateView.as_view(), name="create"),
    path("editar/<pk>", LibroUpdateView.as_view(), name="update"),
    path("eliminar/<pk>", LibroDeteteView.as_view(), name="delete"),
]
