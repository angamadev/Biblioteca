# Generated by Django 5.1.1 on 2024-10-10 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_autor_apellido_alter_autor_biografia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editorial',
            name='direccion',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
