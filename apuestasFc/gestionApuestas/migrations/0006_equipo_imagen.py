# Generated by Django 5.0.1 on 2024-12-03 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionApuestas', '0005_remove_juego_tiempo_finalizacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_equipos/'),
        ),
    ]
