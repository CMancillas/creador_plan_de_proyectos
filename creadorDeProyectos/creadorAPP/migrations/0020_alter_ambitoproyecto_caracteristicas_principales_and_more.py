# Generated by Django 5.1.2 on 2024-11-28 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creadorAPP', '0019_alter_projectplan_clientname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambitoproyecto',
            name='caracteristicas_principales',
            field=models.TextField(blank=True, default='', help_text='Características principales del proyecto.'),
        ),
        migrations.AlterField(
            model_name='ambitoproyecto',
            name='descripcion_ambito',
            field=models.TextField(blank=True, default='', help_text='Descripción del alcance y expectativas del proyecto.'),
        ),
        migrations.AlterField(
            model_name='ambitoproyecto',
            name='limitaciones',
            field=models.TextField(blank=True, default='', help_text='Limitaciones del proyecto.'),
        ),
        migrations.AlterField(
            model_name='projectrisks',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='projectrisks',
            name='risk_identifier',
            field=models.CharField(blank=True, default='', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='projectrisks',
            name='risk_type',
            field=models.CharField(blank=True, choices=[('Técnico', 'Técnico'), ('Organizativo', 'Organizativo'), ('Financiero', 'Financiero')], default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='resource',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Nombre del Recurso'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='resource_type',
            field=models.CharField(blank=True, choices=[('Recursos Humanos', 'Recursos Humanos'), ('Herramientas y Software', 'Herramientas y Software'), ('Infraestructura y Servicios', 'Infraestructura y Servicios'), ('Presupuesto', 'Presupuesto'), ('Documentación y Procedimientos', 'Documentación y Procedimientos')], default='', max_length=30, verbose_name='Tipo de Recurso'),
        ),
        migrations.AlterField(
            model_name='restriccion',
            name='descripcion',
            field=models.TextField(blank=True, default='', help_text='Descripción de la restricción.'),
        ),
        migrations.AlterField(
            model_name='task',
            name='estimated_duration',
            field=models.PositiveIntegerField(blank=True, default='', help_text='Duración estimada en horas'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='workteammember',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Nombre del miembro del equipo'),
        ),
        migrations.AlterField(
            model_name='workteammember',
            name='role',
            field=models.CharField(blank=True, choices=[('Gestor del proyecto', 'Gestor del proyecto'), ('Desarrollador', 'Desarrollador'), ('Analista', 'Analista'), ('QA Tester', 'QA Tester'), ('Otro', 'Otro')], default='', max_length=75, verbose_name='Rol del miembro del equipo'),
        ),
    ]
