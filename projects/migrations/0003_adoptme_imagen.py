# Generated by Django 4.2.3 on 2023-07-14 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_adoptme_datecompleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptme',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
