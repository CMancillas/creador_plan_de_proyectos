from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#Definimos objeto Project y Task
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField() #Campo de texto largo
    created_at = models.DateTimeField(auto_now_add=True) #fecha de creacion
    # Aquí asumimos que el proyecto está relacionado con el usuario administrador que lo crea
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=255)
    estimated_duration = models.PositiveIntegerField(help_text="Duración estimada en horas")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name