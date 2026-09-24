"""
Assistente de Estudos — Mentoria 2.0
Ponto de entrada do aplicativo desktop para Windows 11.
Desenvolvido por Adalton.
MENTORIA 2.0 — por Júlio de Lima.
"""

import sys
import os

# Adiciona o diretório atual ao sys.path para garantir imports relativos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import database
from ui import App


def main():
    # Inicializa as tabelas do banco de dados SQLite (avaliacoes.db)
    database.init_db()

    # Inicia a interface gráfica moderna
    app = App()
    app.run()


if __name__ == "__main__":
    main()

