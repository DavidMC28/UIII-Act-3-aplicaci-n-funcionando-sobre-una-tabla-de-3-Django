from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__' # Incluye todos los campos del modelo, incluyendo la foto
        # O si quieres especificar: fields = ['nombre', 'apellido', 'puesto', 'salario', 'fecha_contratacion', 'foto']