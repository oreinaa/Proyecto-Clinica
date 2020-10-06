from django.contrib import admin
from appcore.models import (Sintoma,Diagnostico,Provincia,Ciudad,Titulo,Sangre, Ciudad, Provincia,
                           EstudioGabinete,Medicamento,Dosis,Frecuencia,Horario,Profesion,
                           Duracion,SignoVital,Antecedente, GrupoAntecedente,Doctor,Agenda,Paciente)

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha','hora','motivo','estado')
    ordering = ('fecha',)
    search_fields = ('paciente','fecha')
    list_filter = ('paciente__apellido','fecha')

class HorariosAdmin(admin.ModelAdmin):
    list_display = ('dia', 'desde','hasta','estado')
    ordering = ('dia',)

admin.site.register(Paciente)
admin.site.register(Sintoma)
admin.site.register(Diagnostico)
admin.site.register(SignoVital)
admin.site.register(EstudioGabinete)
admin.site.register(Medicamento)
admin.site.register(Dosis)
admin.site.register(Frecuencia)
admin.site.register(Duracion)
admin.site.register(Antecedente)
admin.site.register(GrupoAntecedente)
admin.site.register(Horario, HorariosAdmin)
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Sangre)
admin.site.register(Titulo)
admin.site.register(Profesion)
admin.site.register(Doctor)
admin.site.register(Provincia)
admin.site.register(Ciudad)
