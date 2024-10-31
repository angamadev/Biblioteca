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



# Definir accion personalizada
def set_out_of_stock(modeladmin, request, queryset):
    queryset.update(is_out_of_stock=True)
    modeladmin.message_user(request, "Los libros seleccionados han sido marcados como fuera de stock.")
    
# Personalizar el nombre de la accion    
set_out_of_stock.short_description = "Marcar como fuera de stock"


# Definir la acción personalizada para exportar a CSV
def export_books_to_csv(modeladmin, request, queryset):
    import csv
    from django.http import HttpResponse

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'
    writer = csv.writer(response)

    writer.writerow(['Título', 'ISBN', 'Fecha de publicación', 'Número de páginas', 'Idioma'])
    for book in queryset:
        writer.writerow([book.titulo, book.isbn, book.fecha_publicacion, book.numero_paginas, book.idioma])
    
    modeladmin.message_user(request, "Los libros seleccionados se han exportado en books.CSV.")
    return response


# Personalizar el nombre de la acción
export_books_to_csv.short_description = "Exportar libros seleccionados a CSV"



@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = [
        "titulo",
        "isbn",
        "fecha_publicacion",
        "is_out_of_stock",
        "numero_paginas",
        "idioma",
        "editorial"
    ]
    list_filter = ["editorial","idioma","is_out_of_stock"]
    search_fields = ["titulo", "autores__nombre"]
    filter_horizontal = ["autores"]
    actions = [set_out_of_stock,export_books_to_csv]


