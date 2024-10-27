# Generated by Django 5.1.2 on 2024-10-27 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creadorAPP', '0004_esfuerzoproyecto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('presupuesto', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
