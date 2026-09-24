"""
Banco de dados SQLite — Assistente de Estudos — Mentoria 2.0
Gerencia avaliações, casos de teste, defeitos e progresso de atividades.
Desenvolvido por Adalton.
"""

import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "avaliacoes.db")


def get_connection():
    """Retorna uma conexão com o banco de dados."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Cria as tabelas necessárias se não existirem."""
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS avaliacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT NOT NULL,
            modulo TEXT NOT NULL,
            pergunta TEXT NOT NULL,
            resposta TEXT NOT NULL,
            avaliacao INTEGER NOT NULL,
            observacao TEXT
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS casos_teste (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT NOT NULL,
            ct_id TEXT NOT NULL,
            titulo TEXT NOT NULL,
            prioridade TEXT,
            pre_condicoes TEXT,
            dados TEXT,
            passos TEXT NOT NULL,
            resultado_esperado TEXT NOT NULL,
            pos_condicoes TEXT
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS defeitos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT NOT NULL,
            titulo TEXT NOT NULL,
            contexto TEXT,
            passos_reproducao TEXT NOT NULL,
            resultado_esperado TEXT NOT NULL,
            resultado_atual TEXT NOT NULL,
            evidencia TEXT,
            ambiente TEXT,
            versao TEXT,
            severidade TEXT,
            prioridade TEXT
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS progresso_atividades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT NOT NULL,
            atividade TEXT NOT NULL,
            acertou INTEGER NOT NULL,
            detalhes TEXT
        )
    """)

    conn.commit()
    conn.close()


# =====================================================================
# AVALIAÇÕES (Perguntas e Respostas)
# =====================================================================

def salvar_avaliacao(modulo, pergunta, resposta, avaliacao, observacao=""):
    """Salva uma avaliação de resposta no banco e retorna o ID gerado."""
    conn = get_connection()
    c = conn.cursor()
    c.execute(
        """INSERT INTO avaliacoes (data_hora, modulo, pergunta, resposta, avaliacao, observacao)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), modulo, pergunta, resposta, avaliacao, observacao),
    )
    last_id = c.lastrowid
    conn.commit()
    conn.close()
    return last_id


def listar_avaliacoes():
    """Retorna todas as avaliações ordenadas por data (mais recentes primeiro)."""
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM avaliacoes ORDER BY data_hora DESC")
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def buscar_avaliacao(registro_id):
    """Retorna uma avaliação pelo ID."""
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM avaliacoes WHERE id = ?", (registro_id,))
    row = c.fetchone()
    conn.close()
    return dict(row) if row else None


def excluir_avaliacao(registro_id):
    """Exclui uma avaliação pelo ID."""
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM avaliacoes WHERE id = ?", (registro_id,))
    conn.commit()
    conn.close()


# =====================================================================
# CASOS DE TESTE
# =====================================================================

def salvar_caso_teste(ct_id, titulo, prioridade, pre_condicoes, dados, passos, resultado_esperado, pos_condicoes):
    """Salva um caso de teste no banco e retorna o ID gerado."""
    conn = get_connection()
    c = conn.cursor()
    c.execute(
        """INSERT INTO casos_teste
           (data_hora, ct_id, titulo, prioridade, pre_condicoes, dados, passos, resultado_esperado, pos_condicoes)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ct_id, titulo, prioridade,
         pre_condicoes, dados, passos, resultado_esperado, pos_condicoes),
    )
    last_id = c.lastrowid
    conn.commit()
    conn.close()
    return last_id


def listar_casos_teste():
    """Retorna todos os casos de teste."""
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM casos_teste ORDER BY data_hora DESC")
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def buscar_caso_teste(registro_id):
    """Retorna um caso de teste pelo ID."""
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM casos_teste WHERE id = ?", (registro_id,))
    row = c.fetchone()
    conn.close()
    return dict(row) if row else None


def excluir_caso_teste(registro_id):
    """Exclui um caso de teste pelo ID."""
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM casos_teste WHERE id = ?", (registro_id,))
    conn.commit()
    conn.close()


# =====================================================================
# DEFEITOS
# =====================================================================

def salvar_defeito(titulo, contexto, passos_reproducao, resultado_esperado,
                   resultado_atual, evidencia, ambiente, versao, severidade, prioridade):
    """Salva um registro de defeito no banco e retorna o ID gerado."""
    conn = get_connection()
    c = conn.cursor()
    c.execute(
        """INSERT INTO defeitos
           (data_hora, titulo, contexto, passos_reproducao, resultado_esperado,
            resultado_atual, evidencia, ambiente, versao, severidade, prioridade)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), titulo, contexto,
         passos_reproducao, resultado_esperado, resultado_atual, evidencia,
         ambiente, versao, severidade, prioridade),
    )
    last_id = c.lastrowid
    conn.commit()
    conn.close()
    return last_id


def listar_defeitos():
    """Retorna todos os defeitos registrados."""
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM defeitos ORDER BY data_hora DESC")
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def buscar_defeito(registro_id):
    """Retorna um defeito pelo ID."""
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM defeitos WHERE id = ?", (registro_id,))
    row = c.fetchone()
    conn.close()
    return dict(row) if row else None


def excluir_defeito(registro_id):
    """Exclui um defeito pelo ID."""
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM defeitos WHERE id = ?", (registro_id,))
    conn.commit()
    conn.close()


# =====================================================================
# PROGRESSO DAS ATIVIDADES
# =====================================================================

def registrar_progresso(atividade, acertou, detalhes=""):
    """Registra o progresso de uma atividade."""
    conn = get_connection()
    c = conn.cursor()
    c.execute(
        """INSERT INTO progresso_atividades (data_hora, atividade, acertou, detalhes)
           VALUES (?, ?, ?, ?)""",
        (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), atividade,
         1 if acertou else 0, detalhes),
    )
    conn.commit()
    conn.close()


def listar_progresso():
    """Retorna todo o progresso de atividades."""
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM progresso_atividades ORDER BY data_hora DESC")
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def obter_estatisticas_progresso():
    """Retorna estatísticas agrupadas por atividade."""
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        SELECT atividade,
               COUNT(*) as total,
               SUM(acertou) as acertos
        FROM progresso_atividades
        GROUP BY atividade
        ORDER BY atividade
    """)
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def limpar_progresso():
    """Remove todo o progresso de atividades."""
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM progresso_atividades")
    conn.commit()
    conn.close()

