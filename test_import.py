import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qrp_cliniseg.settings')  # ajuste para o caminho correto do seu settings.py
django.setup()

try:
    from relatorios.services import gerar_pdf_fator_risco
    print("Importação bem-sucedida!")
except Exception as e:
    print("Erro na importação:", e)
