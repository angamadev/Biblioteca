
from django.db import models
from .autor_model import Autor
from .editorial_model import Editorial
from django.contrib.auth.models import User


# Modelo para Libros
class Libro(models.Model):
    titulo = models.CharField(max_length=300)
    isbn = models.CharField(max_length=13, unique=True)
    fecha_publicacion = models.DateField()
    numero_paginas = models.IntegerField()

    LANGS_CHOICES = {
        "ES": "Español",
        "EN": "Inglés",
    }

    idioma = models.CharField(max_length=2, choices=LANGS_CHOICES, default="ES")
    descripcion = models.TextField(blank=True, null=True)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, blank=True, null=True)
    autores = models.ManyToManyField(Autor)
    genero = models.CharField(max_length=100, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_out_of_stock = models.BooleanField(verbose_name="Esta fuera de stock",default=False)

    def __str__(self):
        return self.titulo
