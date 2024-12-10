# Generated by Django 5.0.1 on 2024-12-02 23:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestionApuestas', '0003_remove_juego_equipo1_remove_juego_equipo2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo_finalizacion', models.DateTimeField()),
                ('equipo1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipo1', to='gestionApuestas.equipo')),
                ('equipo2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipo2', to='gestionApuestas.equipo')),
                ('ganador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ganador', to='gestionApuestas.equipo')),
            ],
        ),
    ]
