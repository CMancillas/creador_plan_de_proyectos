from django.contrib import admin
from .models import ProjectPlan, Restriccion

# Register your models here.

# Registrando el modelo ProjectPlan a la base de datos
admin.site.register(ProjectPlan)

# Registrando el modelo Restriccion a la base de datos
admin.site.register(Restriccion)