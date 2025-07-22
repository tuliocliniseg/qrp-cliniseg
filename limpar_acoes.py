# limpar_acoes.py

from painel.models import Acao

def limpar_acoes():
    print("Apagando todas as ações...")
    Acao.objects.all().delete()
    print("Todas as ações foram apagadas com sucesso.")

if __name__ == "__main__":
    limpar_acoes()
