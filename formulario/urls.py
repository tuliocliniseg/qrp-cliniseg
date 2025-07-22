from django.urls import path
from .views import exibir_formulario

app_name = "formulario"  # Define namespace para o app formulário

urlpatterns = [
    path("", exibir_formulario, name="formulario_publico"),
]
