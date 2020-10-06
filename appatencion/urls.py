from django.contrib import admin
from django.urls import path
from appatencion.views import HistoriaView, RecetaView
from django.conf import settings

app_name = "atencion"
urlpatterns = [
    path('historia/', HistoriaView.as_view(),name='historia'),
    path('receta/', RecetaView.as_view(),name='receta'),
]