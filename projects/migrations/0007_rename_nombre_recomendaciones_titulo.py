# Generated by Django 4.2.3 on 2023-07-17 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_rename_description_adoptme_descripcion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recomendaciones',
            old_name='nombre',
            new_name='titulo',
        ),
    ]
