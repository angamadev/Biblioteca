# Generated by Django 5.1.1 on 2024-09-11 22:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateField()),
                ('nacionalidad', models.CharField(max_length=100)),
                ('biografia', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('sitio_web', models.URLField(blank=True, null=True)),
                ('premios', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=300)),
                ('ciudad', models.CharField(blank=True, max_length=100, null=True)),
                ('estado', models.CharField(blank=True, max_length=100, null=True)),
                ('pais', models.CharField(blank=True, max_length=100, null=True)),
                ('codigo_postal', models.CharField(blank=True, max_length=20, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('sitio_web', models.URLField(blank=True, null=True)),
                ('fecha_fundacion', models.DateField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('fecha_publicacion', models.DateField()),
                ('numero_paginas', models.IntegerField()),
                ('idioma', models.CharField(choices=[('ES', 'Español'), ('EN', 'Inglés')], default='ES', max_length=2)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('genero', models.CharField(blank=True, max_length=100, null=True)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('autores', models.ManyToManyField(blank=True, null=True, to='books.autor')),
                ('editorial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.editorial')),
            ],
        ),
    ]
