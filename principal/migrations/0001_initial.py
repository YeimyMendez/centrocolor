# Generated by Django 4.1.2 on 2022-10-18 20:15

from django.db import migrations, models
import principal.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emrpesa', models.CharField(max_length=75)),
                ('nombres', models.CharField(max_length=75)),
                ('apellidos', models.CharField(max_length=75)),
                ('documento', models.CharField(max_length=12)),
                ('rh', models.CharField(max_length=2)),
                ('telefono', models.CharField(max_length=12)),
                ('fecha_nacimiento', models.DateField()),
                ('imagen_empresa', models.ImageField(null=True, upload_to='foto')),
            ],
        ),
        migrations.CreateModel(
            name='Universal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
                ('apellido', models.CharField(max_length=75)),
                ('documento', models.CharField(max_length=12)),
                ('genero', models.CharField(blank=True, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino')], default='Masculino', max_length=12, null=True)),
                ('tipo_de_rh', models.CharField(choices=[('o  positivo (O+)', 'O positivo (O+)'), ('o negativo (O-)', 'O negativo (O-)'), ('ab positivo (AB+)', 'AB positivo (AB+)'), ('ab negativo (AB-)', 'AB negativo (AB-)'), ('a positivo (A+)', 'A positivo (A+)'), ('a negativo (A-)', 'A negativo (A-)'), ('b positivo (B+)', 'B positivo (B+)'), ('b negativo (B-)', 'B negativo (B-)')], default='O+', max_length=200)),
                ('empresa_universidad', models.CharField(max_length=75)),
                ('rol_de_usuario', models.CharField(choices=[('estudiante', 'Estudiante'), ('contratista', 'Contratista'), ('funcionario', 'Funcionario')], default='estudiante', max_length=200)),
                ('imagen_universi', models.ImageField(null=True, upload_to=principal.models.upload_location)),
            ],
        ),
    ]
