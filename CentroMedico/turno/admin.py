from django.contrib import admin
from .models import Especialidad, Paciente, Turno

admin.site.register(Especialidad)

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['apellido', 'nombre', 'h_clinica']
    list_filter = ['sexo']
    search_fields = ['nombre', 'apellido']
    
@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'hora', 'paciente']
    list_filter = ['especialidad']