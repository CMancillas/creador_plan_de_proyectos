# Generated by Django 5.1.2 on 2024-11-11 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creadorAPP', '0006_remove_projectplan_employeename_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectrisks',
            name='mitigation_strategy_accept',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectrisks',
            name='mitigation_strategy_avoid',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectrisks',
            name='mitigation_strategy_control',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectrisks',
            name='mitigation_strategy_transfer',
            field=models.TextField(blank=True, null=True),
        ),
    ]