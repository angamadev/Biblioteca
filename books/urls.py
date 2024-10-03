
from django.urls import path
from .views import (
    editoriales_view,
    editorial_detail,
    libros_view,
    libro_detail,
    autores_view,
    autor_detail,
)

app_name = "books"

urlpatterns = [
    path("libros/", libros_view, name='libro_list'),
    path("libros/<int:id>/", libro_detail, name="libro_detail"),
    path("autores/", autores_view, name='autor_list'),
    path("autores/<int:id>/", autor_detail, name="autor_detail"),
    path("editoriales/", editoriales_view, name='editorial_list'),
    path("editoriales/<int:id>/", editorial_detail, name="editorial_detail"),
]
