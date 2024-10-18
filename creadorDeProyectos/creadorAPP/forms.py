from django import forms
from django.contrib.auth.models import User
from .models import AmbitoProyecto

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