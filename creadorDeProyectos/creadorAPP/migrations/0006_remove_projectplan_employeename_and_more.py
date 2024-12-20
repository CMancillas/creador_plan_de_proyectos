# Generated by Django 5.1.3 on 2024-11-07 00:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creadorAPP', '0005_alter_restriccion_descripcion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectplan',
            name='employeeName',
        ),
        migrations.RemoveField(
            model_name='projectplan',
            name='employeeRole',
        ),
        migrations.AddField(
            model_name='ambitoproyecto',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ambiito', to='creadorAPP.projectplan'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='ProjectRisks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_identifier', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('risk_type', models.CharField(choices=[('technical', 'Técnico'), ('organizational', 'Organizativo'), ('financial', 'Financiero')], max_length=20)),
                ('identification_date', models.DateField(auto_now_add=True)),
                ('severity_level', models.CharField(choices=[('low', 'Bajo'), ('medium', 'Medio'), ('high', 'Alto')], max_length=10)),
                ('project_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risks', to='creadorAPP.projectplan')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_type', models.CharField(choices=[('human', 'Recursos Humanos'), ('tools', 'Herramientas y Software'), ('infrastructure', 'Infraestructura y Servicios'), ('budget', 'Presupuesto'), ('documentation', 'Documentación y Procedimientos')], max_length=15, verbose_name='Tipo de Recurso')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre del Recurso')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('quantity_estimated', models.PositiveIntegerField(blank=True, null=True, verbose_name='Cantidad Estimada')),
                ('cost_estimated', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Costo Estimado')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='creadorAPP.projectplan')),
            ],
        ),
        migrations.CreateModel(
            name='WorkTeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre del miembro del equipo')),
                ('role', models.CharField(choices=[('manager', 'Gestor del proyecto'), ('developer', 'Desarrollador'), ('analyst', 'Analista'), ('tester', 'QA Tester'), ('other', 'Otro')], max_length=75, verbose_name='Rol del miembro del equipo')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='creadorAPP.projectplan')),
            ],
        ),
    ]
