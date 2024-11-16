from django.db import models
from .managers import TurnoManager, PacienteManager


class Especialidad(models.Model):
    nombre = models.CharField(max_length=30)
    
    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'
    
    def __str__(self):
        return self.nombre
    
    
class Paciente(models.Model):
    
    SEXO = {
        'H': 'Hombre',
        'M': 'Mujer',
    }
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1, choices=SEXO, default='H')
    dni = models.CharField(max_length=10, unique=True)
    edad = models.IntegerField()
    h_clinica = models.CharField('Historia Clínica', max_length=20, unique=True)
    
    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['apellido', 'nombre']
    
    objects = PacienteManager()
    
    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
    
    
class Turno(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='turnos')
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    
    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'
        ordering = ['fecha', 'hora']
        constraints = [
            models.UniqueConstraint(
                fields=['fecha', 'hora', 'especialidad'],
                name='unique_fecha_hora_especialidad'
            )
        ]
        
    objects = TurnoManager()
        
    def __str__(self):
        return f'{self.fecha} - {self.hora}'