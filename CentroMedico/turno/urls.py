from django.urls import path
from . import views

app_name = 'turno'

urlpatterns = [
    path('', views.HomeTurno.as_view(), name='home_turno'),
    # ---------------------------------------- URLs de TURNOS ---------------------------
    path('listar-turnos', views.ListarTurnos.as_view(), name='listar_turnos'),    
    path('detalle-turno/<pk>/', views.DetalleTurno.as_view(), name='detalle_turno'),    
    path('nuevo-turno', views.NuevoTurno.as_view(), name='nuevo_turno'),
    path('editar-turno/<pk>/', views.EditarTurno.as_view(), name='editar_turno'),
    path('eliminar-turno/<pk>/', views.EliminarTurno.as_view(), name='eliminar_turno'),
    
    # ---------------------------------------- URLs de PACIENTES -------------------------
    path('listar-pacientes', views.ListarPacientes.as_view(), name='listar_pacientes'),
    path('detalle-paciente/<pk>/', views.DetallePaciente.as_view(), name='detalle_paciente'),   
    path('nuevo-paciente', views.NuevoPaciente.as_view(), name='nuevo_paciente'), 
    path('editar-paciente/<pk>/', views.EditarPaciente.as_view(), name='editar_paciente'),
    path('eliminar-paciente/<pk>/', views.EliminarPaciente.as_view(), name='eliminar_paciente'),
]