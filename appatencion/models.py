from django.db import models
from django.utils.timezone import now
from appcore.models import (Paciente,Sintoma,Diagnostico,
                            EstudioGabinete,Medicamento,Dosis,Frecuencia,
                            Duracion,SignoVital,Antecedente, GrupoAntecedente)


class Receta(models.Model):
   paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
   fecha = models.DateField('Fecha de Atencion', blank=True, null=True, default=now().date())
   hora = models.TimeField('Hora', default=now().time())
   motivo = models.CharField('Motivo de consulta', max_length=100)
   sintoma = models.ForeignKey(Sintoma, on_delete=models.PROTECT, null=True)
   exploracion = models.TextField('Exploracion Fisica')
   diagnostico = models.ManyToManyField(Diagnostico)
   gabinete = models.ManyToManyField(EstudioGabinete)
   instrucciones = models.TextField('Instrucciones Medicas')
   estado = models.BooleanField(default=True)

   class Meta:
       verbose_name='Receta Medica'
       verbose_name_plural = 'Recetas Medicas'
   
   def __str__(self):
       return '{}'.format(self.fecha)

class DetalleReceta(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.PROTECT)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.PROTECT)
    dosis = models.ForeignKey(Dosis, on_delete=models.PROTECT)
    frecuencia = models.ForeignKey(Frecuencia, on_delete=models.PROTECT)
    duracion = models.ForeignKey(Duracion, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'DetalleReceta'
        verbose_name_plural = 'DetalleRecetas'
    

    def __str__(self):
        return '{}'.format(self.id)


class TomarSignoVital(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.PROTECT)
    signovital = models.ForeignKey(SignoVital, on_delete=models.PROTECT, blank=True, null=True)
    valor = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Tomar Signo Vital'
        verbose_name_plural = 'Tomar Signos Vitales'
    
    def __str__(self):
        return '{}'.format(self.id)

class Historia(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    fecha = models.DateField('Fecha de Historia', blank=True, null=True, default=now().date())
    hora = models.TimeField('Hora', default=now().time())
    historiaNo = models.CharField('Numero de Historia', max_length=50)
    notas = models.TextField('Notas Internas')
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Historia'
        verbose_name_plural = 'Historias'
    
    def __str__(self):
        return '{}'.format(self.fecha)

class DetalleHistoria(models.Model):
    historia = models.ForeignKey(Historia, on_delete=models.PROTECT)
    GrupoAntecedente = models.ForeignKey(GrupoAntecedente, on_delete=models.PROTECT)
    antecedente = models.ForeignKey(Antecedente, on_delete=models.PROTECT)
    descripcion = models.CharField('Antecedentes', max_length=300)

    class Meta:
        verbose_name = 'Detalle Historia Clinica'
        verbose_name_plural = 'Detalle Historias Clinicas'
    
    def __str__(self):
        return '{}'.format(self.descripcion)
