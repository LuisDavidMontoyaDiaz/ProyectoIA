# Generated by Django 2.2.3 on 2019-08-08 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('algoritmo', '0004_entrenamiento_rutaarchivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrenamiento',
            name='rutaArchivo',
        ),
        migrations.CreateModel(
            name='Ejecucion',
            fields=[
                ('idEjecucion', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('tituloEjecucion', models.CharField(max_length=80)),
                ('datoPrueba', models.FileField(upload_to='Archivos/Test')),
                ('tiempoEjecucion', models.DurationField()),
                ('foraneaAlgoritmo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='algoritmo.Entrenamiento')),
            ],
        ),
    ]