from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

# Modelo para Autores
class Autor(models.Model):
    nombre = models.CharField(
        verbose_name = "Nombre",
        max_length=200
        )
    apellido = models.CharField(
        max_length=200,
        verbose_name = "Apellidos",
        )
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(
        max_length=100,
        verbose_name = "Nacionalidad",
        )
    biografia = models.TextField(
        verbose_name = "Biografia",
    )
    email = models.EmailField(
        verbose_name = "Email",
    )
    telefono = models.CharField(
        verbose_name = "Telefono",
        max_length=20, 
        blank=True, 
        null=True
        )
    sitio_web = models.URLField(
        verbose_name = "Pagina Web",
        blank=True, 
        null=True
        )
    premios = models.TextField(
        verbose_name = "Premios obtenidos",
        blank=True,
        null=True
        )

    def __str__(self):
        return self.nombre