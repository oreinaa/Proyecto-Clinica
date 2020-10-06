from django.shortcuts import render, redirect
import json
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Paciente, Horario,SignoVital, Agenda
from django.views import View
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import *
from .forms import AgendaForm, SignoForm, PacienteForm, HorarioForm, DoctorForm



#Vista de Paciente
class ListadoPacienteView(ListView):
    model = Paciente
    template_name = "core/Paciente/listar_paciente.html"
    context_object_name = "pacientes"
    paginate_by = 3

    def get_queryset(self):
        nombre = self.request.GET.get(
        'nombre') if self.request.GET.get('nombre') else ''
        return self.model.objects.filter(nombre__icontains=nombre, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'nombre') if self.request.GET.get('nombre') else ''
        context['titulo'] = "Consulta de pacientes"
        return context


class CrearPacienteView(CreateView):
    model = Paciente
    template_name = "core/Paciente/crear_paciente.html"
    form_class = PacienteForm
    success_url = reverse_lazy('core:listar_paciente')


class EditarPacienteView(UpdateView):
    model = Paciente
    template_name = "core/Paciente/crear_paciente.html"
    form_class = PacienteForm
    success_url = reverse_lazy('core:listar_paciente')


class EliminarPacienteView(DeleteView):

    def post(self, request, *args, **kwargs):
        pk = request.POST.get("id")
        paciente = Paciente.objects.get(id=pk)
        paciente.delete()
        return redirect('core:listar_paciente')

#Vista de Citas
class CrearCitaView(CreateView):
    model = Agenda
    form_class = AgendaForm
    template_name = "core/Agenda/crear_cita.html"
    success_url = reverse_lazy('core:listar_cita')

class EditarCitaView(UpdateView):
    model = Agenda
    form_class = AgendaForm
    template_name = "core/Agenda/crear_cita.html"
    success_url = reverse_lazy('core:listar_cita')

class EliminarCitaView(DeleteView):

    def post(self, request, *args, **kwargs):
        pk = request.POST.get('id')
        agenda = Agenda.objects.get(id=pk)
        agenda.delete()
        return redirect('core:listar_cita')

class ListadoAgendaView(ListView):
    model = Agenda
    template_name = "core/Agenda/listar_cita.html"
    context_object_name = 'agendas'

    def get_queryset(self):
        fecha = self.request.GET.get(
        'fecha') if self.request.GET.get('fecha') else ''
        return self.model.objects.filter(fecha__icontains = fecha, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fecha'] = self.request.GET.get(
            'fecha') if self.request.GET.get('fecha') else ''
        context['titulo'] = "Consulta de pacientes"
        return context

#Vista de Signos
class CrearSignosView(CreateView):
    model = SignoVital
    form_class = SignoForm
    template_name = "core/signovital/crear_signo.html"
    success_url = reverse_lazy('core:listar_signo')

class EditarSignoView(UpdateView):
    model = SignoVital
    form_class = SignoForm
    template_name = "core/signovital/crear_signo.html"
    success_url = reverse_lazy('core:listar_signo')

class EliminarSignoView(DeleteView):

    def post(self, request, *args, **kwargs):
        pk = request.POST.get('id')
        signo = SignoVital.objects.get(id=pk)
        signo.delete()
        return redirect('core:listar_signo')

class ListadoSignosView(ListView):
    model = SignoVital
    template_name = "core/signovital/listar_signo.html"
    context_object_name = 'signos'

#Vista de Horarios xD
class CrearHorarioView(CreateView):
    model = Horario
    template_name = "core/horario/registrar_horario.html"
    form_class = HorarioForm
    success_url = reverse_lazy('core:listar_horario')


class EditarHorarioView(UpdateView):
    model = Horario
    template_name = "core/horario/registrar_horario.html"
    form_class = HorarioForm
    success_url = reverse_lazy('core:listar_horario')

class EliminarHorarioView(DeleteView):
    
    def post(self, request, *args, **kwargs):
        pk = request.POST.get('id')
        horario = Horario.objects.get(id=pk)
        horario.delete()
        return redirect('core:listar_horario')

class ListadoHorarioView(ListView):
    model = Horario
    template_name = "core/Horario/listar_horario.html"
    context_object_name = 'horarios'

#Vista de Doctor

class CrearDoctorView(CreateView):
    model = Doctor
    template_name = "core/Doctor/crear_doctor.html"
    form_class = DoctorForm
    success_url = reverse_lazy('core:listar_doctor')


class EditarDoctorView(UpdateView):
    model = Doctor
    template_name = "core/Doctor/crear_doctor.html"
    form_class = DoctorForm
    success_url = reverse_lazy('core:listar_doctor')

class EliminarDoctorView(DeleteView):
    
    def post(self, request, *args, **kwargs):
        pk = request.POST.get('id')
        doctor = Doctor.objects.get(id=pk)
        doctor.delete()
        return redirect('core:listar_doctor')

class ListadoDoctorView(ListView):
    model = Doctor
    template_name = "core/Doctor/listar_doctor.html"
    context_object_name = 'doctores'


