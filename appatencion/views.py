import json
from django.db.models.expressions import Random
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views import View
from .models import *
from appcore.models import *
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class InicioView(ListView):
    model = Agenda
    template_name = 'index.html'
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


class HistoriaView(View):
    template_name = 'Atencion/Hclinica/historia.html'

    def get(self, request, *args, **kwargs):
        data = {}
        action = request.GET.get("action")
        if action:
            if action == "data_antecedente":
                id_grupo_antecedente = request.GET.get("id_grupo_antecedente")
                grupo_antecedente = GrupoAntecedente.objects.get(
                    pk=int(id_grupo_antecedente))
                lt_antecedentes = Antecedente.objects.filter(
                    grupoAntecedente_id=grupo_antecedente.id)
                data["lt_antecedentes"] = [{"id": x.id, "descripcion": x.descripcion}
                                           for x in lt_antecedentes]
                data["result"] = "ok"
                return JsonResponse(data, safe=False)
        else:
            id_paciente = request.GET.get("id_paciente", "")
            historia = None
            try:
                historia = Historia.objects.get(pk=int(id_paciente))
            except Exception as ex:
                pass
            if historia:
                data['historia'] = historia
                data['list_historia_detalle'] = DetalleHistoria.objects.filter(
                    historia_id=historia.id)
                data['signo_vitales'] = TomarSignoVital.objects.filter(
                    receta__paciente_id=int(id_paciente))
                print(data['signo_vitales'])
            else:
                historia = Historia.objects.create(
                    paciente_id=int(id_paciente),
                    historiaNo='0'+id_paciente,
                    notas=""
                )
                data['historia'] = historia
            data['title'] = 'Historia Clinica'
            data['lt_grupo_antecedentes'] = GrupoAntecedente.objects.filter(
                estado=True)
            return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'update':
                historia = Historia.objects.get(
                    pk=int(request.POST['id_paciente']))
                historia.notas= request.POST['notas_internas']
                historia.save()
                DetalleHistoria.objects.filter(
                    historia_id=historia.id).delete()
                lt_historia = json.loads(request.POST['lt_historia'])
                for detalle_historia in lt_historia:
                    print(detalle_historia["id_antecedente"])
                    DetalleHistoria.objects.create(
                        historia_id=historia.id,
                        GrupoAntecedente_id=int(
                            detalle_historia["id_grupo_antecedente"]),
                        antecedente_id=int(
                            detalle_historia["id_antecedente"]),
                        descripcion=detalle_historia["descripcion"],
                    )
                data["result"] = "ok"

        except Exception as ex:
            data["error"] = str(ex)
        return JsonResponse(data, safe=False)

class RecetaView(View):
    template_name = 'Atencion/Receta/receta.html'

    def get(self, request, *args, **kwargs):
        data = {}
        id_paciente = request.GET.get("id_paciente", "")
        receta = None
        try:
            receta = Receta.objects.get(pk=int(id_paciente))
        except Exception as ex:
            pass
        if receta:
            data['receta'] = receta
            data['list_receta_detalle'] = DetalleReceta.objects.filter(
                receta_id=receta.id)
        else:
            receta = Receta.objects.create(
                paciente_id=int(id_paciente),
                motivo="",
                exploracion="",
                instrucciones=""
            )
            data['receta'] = receta
            data['title'] = 'Consulta Medica'
            data['lt_grupo_medicamentos'] = Medicamento.objects.filter(
            estado=True)
            data['lt_grupo_dosis'] = Dosis.objects.filter(
            estado=True)
            data['lt_grupo_frecuencias'] = Frecuencia.objects.filter(
            estado=True)
            data['lt_grupo_duraciones'] = Duracion.objects.filter(
            estado=True)
            data['lt_grupo_sintomas'] = Sintoma.objects.filter(
            estado=True)

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'submit':
                receta = Receta.objects.get(
                    pk=int(request.POST['id_paciente']))
                receta.motivo = request.POST['motivo']
                receta.exploracion = request.POST['exploracion']
                receta.instrucciones = request.POST['instrucciones']
                receta.save()
                # DetalleHistoria.objects.filter(
                #     historia_id=historia.id).delete()
                lt_receta = json.loads(request.POST['lt_receta'])
                for detalle_receta in lt_receta:
                    print(detalle_receta["id_grupo_dosis"])
                    print(detalle_receta["id_grupo_frecuencia"])
                    print(detalle_receta["id_grupo_duracion"])
                    DetalleReceta.objects.create(
                        receta_id=receta.id,
                        medicamento_id=int(
                            detalle_receta["id_grupo_medicamento"]),
                        dosis_id=int(
                            detalle_receta["id_grupo_dosis"]),
                        frecuencia_id=int(
                            detalle_receta["id_grupo_frecuencia"]),
                        duracion_id=int(
                            detalle_receta["id_grupo_duracion"]),
                    )
                data["result"] = "ok"

        except Exception as ex:
            data["error"] = str(ex)
        return JsonResponse(data, safe=False)

    

           

    