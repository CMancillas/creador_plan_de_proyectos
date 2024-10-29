from django.contrib import admin
from .models import ProjectPlan

# Register your models here.

# Registrando el modelo ProjectPlan a la base de datos
admin.site.register(ProjectPlan)