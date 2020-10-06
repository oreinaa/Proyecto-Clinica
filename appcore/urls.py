from django.urls import path
from appcore.views import (ListadoPacienteView,CrearPacienteView, EliminarPacienteView, EditarPacienteView , CrearCitaView, 
                           ListadoAgendaView, EditarCitaView,EliminarCitaView, CrearSignosView, CrearHorarioView, EditarHorarioView, 
                           EliminarHorarioView,ListadoHorarioView, EditarSignoView, EliminarSignoView, ListadoSignosView, CrearDoctorView,
                           EditarDoctorView,EliminarDoctorView,ListadoDoctorView)

app_name = 'core'
urlpatterns = [
    path('listar_paciente/', ListadoPacienteView.as_view(), name='listar_paciente'),
    path('crear_paciente/', CrearPacienteView.as_view(), name='crear_paciente'),
    path('editar_paciente/<int:pk>/',
         EditarPacienteView.as_view(), name='editar_paciente'),
    path('eliminar_paciente/<int:pk>/',
         EliminarPacienteView.as_view(), name='eliminar_paciente'),
    path('crear_cita/', CrearCitaView.as_view(), name='crear_cita'),
    path('listar_cita/', ListadoAgendaView.as_view(), name='listar_cita'),
    path('editar_cita/<int:pk>/',EditarCitaView.as_view(), name="editar_cita"),
    path('eliminar_cita/<int:pk>/',EliminarCitaView.as_view(), name="eliminar_cita"),
    path('crear_signo/', CrearSignosView.as_view(), name='crear_signo'),
    path('listar_signo/', ListadoSignosView.as_view(), name='listar_signo'),
    path('editar_signo/<int:pk>/',EditarSignoView.as_view(), name="editar_signo"),
    path('eliminar_signo/<int:pk>/',EliminarSignoView.as_view(), name="eliminar_signo"),
    path('crear_horario/', CrearHorarioView.as_view(), name='crear_horario'),
    path('listar_horario/', ListadoHorarioView.as_view(), name='listar_horario'),
    path('editar_horario/<int:pk>/',EditarHorarioView.as_view(), name="editar_horario"),
    path('eliminar_horario/<int:pk>/',EliminarHorarioView.as_view(), name="eliminar_horario"),
    path('crear_doctor/', CrearDoctorView.as_view(), name='crear_doctor'),
    path('listar_doctor/', ListadoDoctorView.as_view(), name='listar_doctor'),
    path('editar_doctor/<int:pk>/',EditarDoctorView.as_view(), name="editar_doctor"),
    path('eliminar_doctor/<int:pk>/',EliminarDoctorView.as_view(), name="eliminar_doctor"),
]