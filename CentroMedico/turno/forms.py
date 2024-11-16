from django import forms
from .models import Paciente, Turno

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = [
            'nombre', 'apellido', 'sexo',
            'dni', 'edad', 'h_clinica'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'sexo': forms.RadioSelect(),
            'dni': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'h_clinica': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        }
        
        
class TurnoForm(forms.ModelForm):

    class Meta:
        model = Turno
        fields = [
            'paciente', 'especialidad',
            'fecha', 'hora'
        ]
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'especialidad': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-sm'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-sm'}),
        }