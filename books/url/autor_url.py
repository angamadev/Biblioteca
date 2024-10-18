
from django.urls import path

from books.views.autores_views import (
    AutoresListView,
    AutorDetailView,
    AutorCreateView,
    AutorUpdateView,
    AutorDeteteView,    
)   

app_name = "autor"

urlpatterns = [
    path("lista/", AutoresListView.as_view(), name='list'),
    path("detalle/<pk>/", AutorDetailView.as_view(), name="detail"),
    path("nuevo/", AutorCreateView.as_view(), name="create"),
    path("editar/<pk>", AutorUpdateView.as_view(), name="update"),
    path("eliminar/<pk>", AutorDeteteView.as_view(), name="delete"),
]
