from django.contrib import admin
from .models import AmbitoProyecto, ProjectPlan, Task

# Register your models here.
admin.site.register(AmbitoProyecto)
admin.site.register(ProjectPlan)
admin.site.register(Task)
