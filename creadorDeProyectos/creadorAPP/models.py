from django.db import models
from django.contrib.auth.models import User

class ProjectPlan(models.Model):
     # se guarda el usuario que crea el proyecto
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100,blank=True, default='')

    description = models.TextField(blank=True, default='')

    objetive = models.TextField(blank=True, default='')

    clientName = models.CharField(max_length=50,blank=True, default='')

    startDate = models.DateField(blank=True, default='')

    endDate = models.DateField(blank=True, default='')

    # Campo para el presupuesto total
    presupuestoTotal = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        null=True,
        blank=True,
        help_text="Presupuesto total del proyecto en USD."
        )

    def _str_(self):
        return f"Proyecto: {self.title}"
    

    
class Task(models.Model):
    project = models.ForeignKey(ProjectPlan, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=255,blank=True, default='',verbose_name='Nombre')
    description = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        verbose_name='Descripción' 
    )
    estimated_duration = models.PositiveIntegerField(blank=True, default='',verbose_name='Duración Estimada')
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(null=True, blank=True,verbose_name='Fecha de inicio')  # Campo para la fecha de inicio
    end_date = models.DateField(null=True, blank=True,verbose_name='Fecha de fin')    # Campo para la fecha de fin

    def __str__(self):
        return f"Tarea: {self.name}"
  
class Restriccion(models.Model):
    RISK_TYPES = [
       ('Técnico', 'Técnico'),
        ('Organizativo', 'Organizativo'),
        ('Financiero', 'Financiero'),
    ]

    proyecto = models.ForeignKey(ProjectPlan, on_delete=models.CASCADE, related_name='restricciones')
    descripcion = models.TextField(help_text="Descripción de la restricción.",blank=True, default='')
    tipo_riesgo = models.CharField(
        max_length=30, 
        choices=RISK_TYPES, 
        verbose_name="Tipo de Riesgo",
        null=True, 
        blank=True,
        help_text="Tipo de riesgo asociado con esta restricción."
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Restricción para el proyecto {self.proyecto.title}"


class AmbitoProyecto(models.Model):
    project = models.ForeignKey(ProjectPlan, on_delete=models.CASCADE, related_name='ambiito')
    descripcion_ambito = models.TextField(help_text="Descripción del alcance y expectativas del proyecto.",blank=True, default='')
    caracteristicas_principales = models.TextField(help_text="Características principales del proyecto.",blank=True, default='')
    limitaciones = models.TextField(help_text="Limitaciones del proyecto.",blank=True, default='')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Alcance del Proyecto: {self.project.title}"
    

class WorkTeamMember(models.Model):
    ROLE_CHOICES = [
         ('Gestor del proyecto', 'Gestor del proyecto'),
        ('Desarrollador', 'Desarrollador'),
        ('Analista', 'Analista'),
        ('QA Tester', 'QA Tester'),
        ('Otro', 'Otro'),
    ]

    project = models.ForeignKey(ProjectPlan, on_delete=models.CASCADE, related_name = 'team_members')
    name = models.CharField(max_length=200, verbose_name="Nombre del miembro del equipo",blank=True, default='')
    role = models.CharField(max_length=75, choices=ROLE_CHOICES, verbose_name="Rol del miembro del equipo",blank=True, default='')

    def __str__(self):
        return f"{self.name} - {self.get_role_display()}"


class Resource(models.Model):
    RESOURCE_TYPE_CHOICES = [
    ('Recursos Humanos', 'Recursos Humanos'),
    ('Herramientas y Software', 'Herramientas y Software'),
    ('Infraestructura y Servicios', 'Infraestructura y Servicios'),
    ('Presupuesto', 'Presupuesto'),
    ('Documentación y Procedimientos', 'Documentación y Procedimientos'),
    ]

    project = models.ForeignKey(ProjectPlan, on_delete=models.CASCADE, related_name='resources')
    resource_type = models.CharField(max_length=30, choices=RESOURCE_TYPE_CHOICES, verbose_name="Tipo de Recurso",blank=True, default='')
    name = models.CharField(max_length=255, verbose_name="Nombre del Recurso",blank=True, default='')
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    quantity_estimated = models.PositiveIntegerField(blank=True, null=True, verbose_name="Cantidad Estimada")
    cost_estimated = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Costo Estimado")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_resource_type_display()} - {self.name}"


class ProjectRisks(models.Model):
    RISK_TYPES = [
        ('Técnico', 'Técnico'),
        ('Organizativo', 'Organizativo'),
        ('Financiero', 'Financiero'),
    ]
    MITIGATION_STRATEGIES = [
        ('Evitar', 'Evitar'),
        ('Aceptar', 'Aceptar'),
        ('Transferir', 'Transferir'),
        ('Controlar', 'Controlar'),
    ]
    project_plan = models.ForeignKey(ProjectPlan, on_delete=models.CASCADE, related_name='risks')
    risk_identifier = models.CharField(max_length=50, unique=True,blank=True, default='')
    description = models.TextField(blank=True, default='')
    risk_type = models.CharField(max_length=30, choices=RISK_TYPES,blank=True, default='')
    identification_date = models.DateField(auto_now_add=True)
    probability = models.CharField(max_length=30, choices=[
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
    ])
    severity_level = models.CharField(max_length=30, choices=[
        ('Bajo', 'Bajo'),
        ('Medio', 'Medio'),
        ('Alto', 'Alto'),
    ])
    mitigation_strategy = models.CharField(max_length=30, choices=MITIGATION_STRATEGIES)
    def __str__(self):
        return f"{self.risk_identifier}: {self.description}"
