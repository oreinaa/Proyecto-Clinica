from .models import Horario, Agenda, SignoVital, Paciente, Doctor
from django import forms

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nacimiento': forms.DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'civil': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'profesion': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'titulo': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'provincia': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ciudad': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sangre': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'hijos': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ('paciente','fecha','hora','motivo','estado')
        label = {
            'paciente': 'Paciente',
            'fecha': 'Fecha',
            'hora': 'Hora',
            'motivo': 'Motivo de Consulta',
            'estado': 'Estado'
        }
        widgets = {
            'paciente': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del paciente'
                }
            ),
            'fecha': forms.DateInput(
               format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}
            ),
            'hora': forms.TimeInput(
                attrs= {'class': 'form-control',
                       'placeholder': 'hh:mm'
                }
            ),
            'motivo': forms.TextInput(
                attrs= {'class': 'form-control',
                       'placeholder': 'Motivo de Consulta'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs= {'class': 'form-control',
                }      
            ),

        }


class SignoForm(forms.ModelForm):
    class Meta:
        model = SignoVital
        fields =  ('descripcion','rango1','rango2','medida','imagen','estado')
        label = {
            'descripcion': 'Signo Vital',
            'rango1': 'Rango 1',
            'rango2': 'Rango 2',
            'medida': 'Medida',
            'imagen': 'Imagen',
            'estado': 'Estado'
        }
        widgets = {
            'descripcion': forms.TextInput (
                attrs= {
                    'class': 'form-control'
                }
            ),
            'rango1': forms.NumberInput (
                attrs= {
                    'class': 'form-control'
                }
            ),
            'rango2': forms.NumberInput (
                attrs= {
                    'class': 'form-control'
                }
            ),
            'medida': forms.TextInput (
                attrs= {
                    'class': 'form-control'
                }
            ),
             'imagen': forms.FileInput (
                attrs= {
                    'class': 'form-control'
                }
            ),
             'estado': forms.CheckboxInput (
                attrs= {
                    'class': 'form-control'
                }
            ),
        }

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ('dia','desde','hasta','estado')
        label = {
            'dia': 'Dia',
            'desde': 'Desde',
            'hasta': 'Hasta',
            'estado': 'Estado'
        }
        widgets = {
            'dia': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Dia'
                }
            ),
            'desde': forms.TimeInput(
               attrs={'class':'form-control', 
                       'placeholder':'hh:mm'}
            ),
            'hasta': forms.TimeInput(
                attrs= {'class': 'form-control',
                       'placeholder': 'hh:mm'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs= {'class': 'form-control',
                }      
            ),

        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nacimiento': forms.DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'civil': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'profesion': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'titulo': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'provincia': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ciudad': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'consultorio': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'lugar': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'horario': forms.SelectMultiple (
                 attrs={
                    'class': 'form-control'
                }
            ),
            'duracion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'logo': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'registro': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }