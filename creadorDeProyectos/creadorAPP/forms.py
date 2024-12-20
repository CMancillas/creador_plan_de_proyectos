from django import forms
from django.contrib.auth.models import User
from .models import AmbitoProyecto
from .models import ProjectPlan
from .models import Task
from .models import Restriccion
from .models import Resource
from .models import ProjectRisks
from .models import WorkTeamMember


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields  = ['username', 'password', 'password_confirm']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        # Check if the passwords match
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data
    
class AmbitoProyectoForm(forms.ModelForm):
    class Meta:
        model = AmbitoProyecto
        fields = ['descripcion_ambito', 'caracteristicas_principales', 'limitaciones']
        widgets = {
            'descripcion_ambito': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Describa el alcance del proyecto...'}),
            'caracteristicas_principales': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Características principales...'}),
            'limitaciones': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Limitaciones del proyecto...'}),
        }
        labels = {
            'descripcion_ambito': 'Descripción del Ámbito del Proyecto',
            'caracteristicas_principales': 'Características Principales',
            'limitaciones': 'Limitaciones',
        }
    
    def clean(self):
        cleaned_data = super().clean()
        descripcion_ambito = cleaned_data.get('descripcion_ambito')
        caracteristicas_principales = cleaned_data.get('caracteristicas_principales')
        limitaciones = cleaned_data.get('limitaciones')

        if not descripcion_ambito:
            self.add_error('descripcion_ambito', "Este campo es obligatorio.")
        
        if not caracteristicas_principales:
            self.add_error('caracteristicas_principales', "Este campo es obligatorio.")
        
        if not limitaciones:
            self.add_error('limitaciones', "Este campo es obligatorio.")



class ProjectPlanForm(forms.ModelForm):
    class Meta:
        model = ProjectPlan
        fields = ['title', 'description', 'objetive', 'clientName','startDate', 'endDate', 'presupuestoTotal']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descripción del proyecto...'}),
            'objetive': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Objetivo del proyecto...'}),
            'startDate': forms.DateInput(attrs={'type': 'date'}),
            'endDate': forms.DateInput(attrs={'type': 'date'}),
            'presupuestoTotal': forms.NumberInput(attrs={'placeholder': 'Presupuesto en USD'}),
        }
        labels = {
            'title': 'Título del Proyecto',
            'description': 'Descripción',
            'objetive': 'Objetivo',
            'clientName': 'Nombre del Cliente',
            'startDate': 'Fecha de Inicio',
            'endDate': 'Fecha de Fin',
            'presupuestoTotal': 'Prespuesto Total (USD)',
        }
    
    def clean(self):
        cleaned_data = super().clean()
        startDate = cleaned_data.get('startDate')
        endDate = cleaned_data.get('endDate')
        presupuestoTotal = cleaned_data.get('presupuestoTotal')
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')
        objetive = cleaned_data.get('objetive')
        clientName = cleaned_data.get('clientName')

        if not title:
            self.add_error('title', "Este campo es obligatorio.")

        if not description:
            self.add_error('description', "Este campo es obligatorio.")

        if not objetive:
            self.add_error('objetive', "Este campo es obligatorio.")

        if not clientName:
            self.add_error('clientName', "Este campo es obligatorio.")        

        if startDate and endDate and startDate > endDate:
            self.add_error('endDate', "La fecha de fin no puede ser anterior a la fecha de inicio.")

        # Validacion de presupuesto positivo
        if presupuestoTotal is not None and presupuestoTotal < 0:
            self.add_error('presupuestoTotal', "El presupuesto debe de ser un valor positivo.")
        
        return cleaned_data
    
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description','estimated_duration', 'start_date', 'end_date']
        widgets = {
            'description': forms.TextInput(attrs={'maxlength': 255}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
    def clean (self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        estimated_duration = cleaned_data.get('estimated_duration')
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if not name:
            self.add_error('name', "Este campo es obligatorio.")
        
        if not description:
            self.add_error('description', "Este campo es obligatorio.")
        
        if not estimated_duration:
            self.add_error('estimated_duration', "Este campo es obligatorio.")
        
        if start_date and end_date and start_date > end_date:
            self.add_error('end_date', "La fecha de fin no puede ser anterior a la fecha de inicio.")
        
        return cleaned_data   

class RestriccionForm(forms.ModelForm):
    class Meta: 
        model = Restriccion
        fields = ['descripcion', 'tipo_riesgo']#, 'riesgo_identificado']
        labels = {
            'descripcion': 'Descripción de la Restricción',
            'tipo_riesgo': 'Tipo de Riesgo',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe la restricción...'}),
            'tipo_riesgo': forms.Select()
        }

           
class DeleteTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'estimated_duration', 'project']              


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['resource_type', 'name', 'description', 'quantity_estimated', 'cost_estimated']
        labels = {
            'resource_type': 'Tipo de Recurso',
            'name': 'Nombre del Recurso',
            'description': 'Descripción',
            'quantity_estimated': 'Cantidad Estimada',
            'cost_estimated': 'Costo Estimado',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }


class ProjectRisksForm(forms.ModelForm):
    class Meta:
        model = ProjectRisks
        fields = ['risk_identifier', 'description', 'risk_type', 'probability', 'severity_level','mitigation_strategy']
        labels = {
            'risk_identifier': 'Identificador del Riesgo',
            'description': 'Descripción',
            'risk_type': 'Tipo de Riesgo',
            'probability': 'Probabilidad de ocurrencia',
            'severity_level': 'Impacto en el Proyecto',
            'mitigation_strategy': 'Estrategia de Mitigación',
            
        }

class WorkTeamMemberForm(forms.ModelForm):
    class Meta:
        model = WorkTeamMember
        fields = ['name', 'role']
        labels = {
            'name': 'Nombre del miembro del equipo',
            'role': 'Rol del miembro del equipo',
        }


