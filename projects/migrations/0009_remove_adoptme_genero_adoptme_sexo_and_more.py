# Generated by Django 4.2.3 on 2023-07-17 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_rename_descripcion_recomendaciones_mensaje_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adoptme',
            name='Genero',
        ),
        migrations.AddField(
            model_name='adoptme',
            name='sexo',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='adoptme',
            name='Imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
    ]
