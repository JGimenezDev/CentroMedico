from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from .models import Especialidad, Paciente, Turno
from .forms import PacienteForm, TurnoForm


class HomeTurno(TemplateView):
    template_name = "turno/home_turno.html"

# ------------------------ VISTAS PARA TURNOS --------------------------

class ListarTurnos(ListView):
    template_name = "turno/listar_turnos.html"
    context_object_name = 'turnos'
    paginate_by = 7
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['especialidades'] = Especialidad.objects.all().order_by('nombre')
        
        return context
    
    def get_queryset(self):
        esp = self.request.GET.get('esp', '')
        desde = self.request.GET.get('desde', '')
        hasta = self.request.GET.get('hasta', '')

        return Turno.objects.filtrar_turnos(esp, desde, hasta)
       

class DetalleTurno(DetailView):
    model = Turno
    template_name = "turno/detalle_turno.html"
    context_object_name = 'turno'


class NuevoTurno(CreateView):
    model = Turno
    template_name = "turno/nuevo_turno.html"
    form_class = TurnoForm
    
    def get_success_url(self):
        return reverse('turno:detalle_turno', kwargs={'pk': self.object.pk})


class EditarTurno(UpdateView):
    model = Turno
    template_name = "turno/editar_turno.html"
    form_class = TurnoForm
    
    def get_success_url(self):
        return reverse('turno:detalle_turno', kwargs={'pk': self.object.pk})


class EliminarTurno(DeleteView):
    model = Turno
    template_name = "turno/eliminar_turno.html"
    context_object_name = 'turno'
    success_url = reverse_lazy('turno:listar_turnos')




# ------------------------ VISTAS PARA PACIENTES --------------------------

class ListarPacientes(ListView):
    template_name = "turno/listar_pacientes.html"
    context_object_name = 'pacientes'
    paginate_by = 7
    
    def get_queryset(self):
        name = self.request.GET.get('nombre', '')
        h_clinica = self.request.GET.get('h_cli', '')
        
        return Paciente.objects.filtrar_pacientes(name, h_clinica)
    

class DetallePaciente(DetailView):
    model = Paciente
    template_name = "turno/detalle_paciente.html"
    context_object_name = 'paciente'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = timezone.now().date()
        turnos = self.request.GET.get('turnos', '')
        
        if turnos == 'prox':
            context['mostrar_turnos'] = self.get_object().turnos.filter(
                fecha__gte = hoy
            )[:5]
        elif turnos == 'venc':
            context['mostrar_turnos'] = self.get_object().turnos.filter(
                fecha__lt = hoy
            ).order_by('-fecha')[:5]
            
        return context    
    

class NuevoPaciente(CreateView):
    model = Paciente
    template_name = "turno/nuevo_paciente.html"
    form_class = PacienteForm
    
    def get_success_url(self):
        return reverse('turno:detalle_paciente', kwargs={'pk': self.object.pk})
    

class EditarPaciente(UpdateView):
    model = Paciente
    template_name = "turno/editar_paciente.html"
    form_class = PacienteForm
    
    def get_success_url(self):
        return reverse('turno:detalle_paciente', kwargs={'pk': self.object.pk})
    

class EliminarPaciente(DeleteView):
    model = Paciente
    template_name = "turno/eliminar_paciente.html"
    context_object_name = 'paciente'
    success_url = reverse_lazy('turno:listar_pacientes')