
from django.urls import path

from books.views.editoriales_views import (
    EditorialListView,
    EditorialDetailView,
    EditorialCreateView,
    EditorialUpdateView,
    EditorialDeteteView,    
)   

app_name = "editorial"

urlpatterns = [
    path("lista/", EditorialListView.as_view(), name='list'),
    path("detalle/<pk>/", EditorialDetailView.as_view(), name="detail"),
    path("nuevo/", EditorialCreateView.as_view(), name="create"),
    path("editar/<pk>", EditorialUpdateView.as_view(), name="update"),
    path("eliminar/<pk>", EditorialDeteteView.as_view(), name="delete"),
]
