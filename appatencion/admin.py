from django.contrib import admin
from appatencion.models import TomarSignoVital, Historia, Receta, DetalleReceta, DetalleHistoria


admin.site.register(TomarSignoVital)
admin.site.register(Historia)
admin.site.register(Receta)
admin.site.register(DetalleReceta)
admin.site.register(DetalleHistoria)