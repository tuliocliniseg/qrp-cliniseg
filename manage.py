#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    
    # 🧠 Esta linha define qual módulo de configuração será usado
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qrp_cliniseg.settings')

    try:
        # ✅ Aqui o Django carrega os comandos administrativos
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # ⚠️ Erro caso o Django não esteja instalado corretamente
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # 🚀 Executa o comando fornecido (como runserver, migrate, etc.)
    execute_from_command_line(sys.argv)

# ✅ Garante que isso será executado apenas se for o script principal
if __name__ == '__main__':
    main()
