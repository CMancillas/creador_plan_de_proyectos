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
#edit de hoy
class EventoCronograma(models.Model):
    titulo = models.CharField(max_length=100)  # Ej. "Inicio del proyecto"
    descripcion = models.TextField(blank=True, null=True)  # Descripción detallada
    fecha_inicio = models.DateField()  # Fecha en la que inicia el evento
    fecha_fin = models.DateField()  # Fecha de finalización, si aplica
    tipo_evento = models.CharField(
        max_length=50, 
        choices=[('trabajo', 'Día de trabajo'), ('entrega', 'Entrega'), ('reunión', 'Reunión')]
    )

    def __str__(self):
        return self.titulo
    
class EsfuerzoProyecto(models.Model):
    proyecto = models.ForeignKey(ProjectPlan, on_delete=models.CASCADE)  # Enlace al proyecto
    esfuerzo_estimado = models.DecimalField(max_digits=6, decimal_places=2)  # Esfuerzo estimado en horas
    esfuerzo_real = models.DecimalField(max_digits=6, decimal_places=2, default=0)  # Esfuerzo real en horas

    def diferencia_esfuerzo(self):
        return self.esfuerzo_estimado - self.esfuerzo_real  # Devuelve la diferencia entre estimado y real

    def __str__(self):
        return f"Esfuerzo del proyecto {self.proyecto.nombre}"
    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    costo = models.DecimalField(max_digits=10, decimal_places=2)  # Campo para el costo
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2)  # Campo para el presupuesto

    def __str__(self):
        return self.nombre