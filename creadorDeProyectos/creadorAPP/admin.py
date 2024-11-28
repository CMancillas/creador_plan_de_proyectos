from django.contrib import admin
from .models import ProjectPlan, Restriccion, Task, AmbitoProyecto, WorkTeamMember, Resource, ProjectRisks

# Register your models here.

# Registrando el modelo ProjectPlan a la base de datos
admin.site.register(ProjectPlan)

# Registrando el modelo Restriccion a la base de datos
admin.site.register(Restriccion)
admin.site.register(Task)
admin.site.register(AmbitoProyecto)
admin.site.register(WorkTeamMember)
admin.site.register(Resource)
admin.site.register(ProjectRisks)
