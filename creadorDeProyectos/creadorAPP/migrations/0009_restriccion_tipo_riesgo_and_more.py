# Generated by Django 5.1.2 on 2024-11-13 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("creadorAPP", "0008_projectplan_created_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="restriccion",
            name="tipo_riesgo",
            field=models.CharField(
                blank=True,
                choices=[
                    ("technical", "Técnico"),
                    ("organizational", "Organizativo"),
                    ("financial", "Financiero"),
                ],
                help_text="Tipo de riesgo asociado con esta restricción.",
                max_length=20,
                null=True,
                verbose_name="Tipo de Riesgo",
            ),
        ),
        migrations.AlterField(
            model_name="restriccion",
            name="descripcion",
            field=models.TextField(help_text="Descripción de la restricción."),
        ),
    ]