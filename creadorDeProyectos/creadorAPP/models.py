from django.db import models
from django.contrib.auth.models import User

class AmbitoProyecto(models.Model):
    descripcion_ambito = models.TextField(help_text="Descripción del alcance y expectativas del proyecto.")
    caracteristicas_principales = models.TextField(help_text="Características principales del proyecto.")
    limitaciones = models.TextField(help_text="Limitaciones del proyecto.")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ámbito definido"
    


class ProjectPlan(models.Model):

    title = models.CharField(max_length=100)

    description = models.TextField()

    objetive = models.TextField()

    clientName = models.CharField(max_length=50)

    employeeName = models.CharField(max_length=50)

    employeeRole = models.CharField(max_length=50)
    
    startDate = models.DateField()

    endDate = models.DateField()



    def _str_(self):
        return f"Plan de proyecto almacenado exitosamente."
    

class Task(models.Model):
    project = models.ForeignKey(ProjectPlan, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=255)
    estimated_duration = models.PositiveIntegerField(help_text="Duración estimada en horas")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tarea almacenada exitosamente."