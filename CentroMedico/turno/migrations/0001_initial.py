# Generated by Django 5.1.3 on 2024-11-16 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Especialidad',
                'verbose_name_plural': 'Especialidades',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=30)),
                ('sexo', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer')], default='H', max_length=1)),
                ('dni', models.CharField(max_length=10, unique=True)),
                ('edad', models.IntegerField()),
                ('h_clinica', models.CharField(max_length=20, unique=True, verbose_name='Historia Clínica')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'ordering': ['apellido', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turno.especialidad')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turnos', to='turno.paciente')),
            ],
            options={
                'verbose_name': 'Turno',
                'verbose_name_plural': 'Turnos',
                'ordering': ['fecha', 'hora'],
                'constraints': [models.UniqueConstraint(fields=('fecha', 'hora', 'especialidad'), name='unique_fecha_hora_especialidad')],
            },
        ),
    ]
