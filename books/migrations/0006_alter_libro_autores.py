# Generated by Django 5.1.1 on 2024-10-28 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_libro_descripcion_en_libro_descripcion_es_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autores',
            field=models.ManyToManyField(to='books.autor'),
        ),
    ]
