from django.utils import timezone
from django.db import models
from django.db.models import Q


class TurnoManager(models.Manager):
    
    def filtrar_turnos(self, esp='', desde=None, hasta=None):
        queryset = self.get_queryset()
        
        if esp != '':
            queryset = queryset.filter(especialidad__id = esp).order_by('especialidad__nombre')
        
        if desde:
            queryset = queryset.filter(fecha__gte = desde)
        
        if hasta:
            queryset = queryset.filter(fecha__lte = hasta)
            
        return queryset
    
    def ver_turnos(self, momento):
        queryset = self.get_queryset()
        
        hoy = timezone.now()
        
        if momento == 'anterior':
            queryset = queryset.filter(
                fecha__lte = hoy.date(),
                hora__lt= hoy.time()
            )
        if momento == 'proximo':
            queryset = queryset.filter(
                fecha__gte = hoy.date(),
                hora__gte = hoy.time()
            )
        return queryset
    
    

class PacienteManager(models.Manager):
    def filtrar_pacientes(self, name='', h_cli=''):
        queryset = self.get_queryset()
        
        if name != '':
            queryset = queryset.filter(
                Q(nombre__icontains = name) |
                Q(apellido__icontains = name)
            ).order_by('apellido')
        
        if h_cli != '':
            queryset = queryset.filter(
                h_clinica__icontains = h_cli
            ).order_by('-h_clinica')
        
        return queryset