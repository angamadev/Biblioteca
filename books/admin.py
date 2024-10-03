from django.contrib import admin
from books.models import Editorial, Libro, Autor

# Register your models here.
class LibroInline(admin.StackedInline):
    model = Libro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = [
        "nombre",
        "apellido",
        "email",
        "telefono"
        ]
    ordering = ["nombre"]

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = [
        "nombre",
        "ciudad",
        "email",
        "telefono",
        "sitio_web",
        "fecha_fundacion",
    ]
    list_filter = [
        "fecha_fundacion"
    ]
    inlines = [LibroInline]


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = [
        "titulo",
        "isbn",
        "fecha_publicacion",
        "numero_paginas",
        "idioma",
        "editorial"
    ]
    list_filter = ["editorial","idioma"]
    search_fields = ["titulo", "autores__nombre"]
    filter_horizontal = ["autores"]



