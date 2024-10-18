from django.contrib import admin
from .models import AmbitoProyecto
from .models import ProjectPlan

# Register your models here.

admin.site.register(AmbitoProyecto)
admin.site.register(ProjectPlan)