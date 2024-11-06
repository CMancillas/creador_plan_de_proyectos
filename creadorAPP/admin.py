from django.contrib import admin
from .models import AmbitoProyecto, ProjectPlan, Task, Resource, ProjectRisks

# Register your models here.
admin.site.register(AmbitoProyecto)
admin.site.register(ProjectPlan)
admin.site.register(Task)
admin.site.register(Resource)
admin.site.register(ProjectRisks)