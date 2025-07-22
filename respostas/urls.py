from django.urls import path
from . import views

app_name = "respostas"

urlpatterns = [
    path('formulario/', views.exibir_formulario, name='exibir_formulario'),
]
