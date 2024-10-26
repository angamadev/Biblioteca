from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _lazy


# Create your models here.

# Modelo para Autores
class Autor(models.Model):
    nombre = models.CharField(
        verbose_name = _lazy("Nombre"),
        max_length=200
        )
    apellido = models.CharField(
        max_length=200,
        verbose_name = _lazy("Apellidos"),
        )
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(
        max_length=100,
        verbose_name = _lazy("Nacionalidad"),
        )
    biografia = models.TextField(
        verbose_name = _lazy("Biografia"),
    )
    email = models.EmailField(
        verbose_name = _lazy("Email"),
    )
    telefono = models.CharField(
        verbose_name = _lazy("Telefono"),
        max_length=20, 
        blank=True, 
        null=True
        )
    sitio_web = models.URLField(
        verbose_name = _lazy("Pagina Web"),
        blank=True, 
        null=True
        )
    premios = models.TextField(
        verbose_name = _lazy("Premios obtenidos"),
        blank=True,
        null=True
        )
    created_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
        )

    def __str__(self):
        return self.nombre