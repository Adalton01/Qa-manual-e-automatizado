"""
Interface principal — Assistente de Estudos — Mentoria 2.0
Aplicativo desktop com 6 telas para estudos de Testes de Software.
Desenvolvido por Adalton.
MENTORIA 2.0 — por Júlio de Lima.
"""

import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
try:
    from ttkbootstrap.scrolled import ScrolledFrame
except ImportError:
    from ttkbootstrap import ScrolledFrame

import database
import knowledge_base
import activities


# =====================================================================
# CONSTANTES DE ESTILO
# =====================================================================

FONT_TITLE = ("Segoe UI", 22, "bold")
FONT_SUBTITLE = ("Segoe UI", 16, "bold")
FONT_SECTION = ("Segoe UI", 14, "bold")
FONT_BODY = ("Segoe UI", 12)
FONT_BODY_BOLD = ("Segoe UI", 12, "bold")
FONT_SMALL = ("Segoe UI", 10)
FONT_STAR = ("Segoe UI", 28)
FONT_WATERMARK = ("Segoe UI", 11, "italic")
FONT_MENU = ("Segoe UI", 13)

PAD_X = 18
PAD_Y = 10
CARD_PAD = 15

STAR_EMPTY = "☆"
STAR_FULL = "★"


# =====================================================================
# CLASSE PRINCIPAL DO APLICATIVO
# =====================================================================

class App:
    """Aplicativo Assistente de Estudos — Mentoria 2.0."""

    def __init__(self):
        # Janela principal
        self.window = ttkb.Window(
            title="Assistente de Estudos — Mentoria 2.0",
            themename="cosmo",
            size=(1150, 780),
            minsize=(950, 650),
        )
        self.window.place_window_center()

        # Variáveis de estado
        self.current_screen = None
        self.star_rating = 0
        self.star_labels = []
        self.current_response = ""
        self.current_module = ""
        self.activity_sub_frame = None

        # Criar layout principal
        self._create_layout()

        # Mostrar tela inicial
        self.show_screen("inicio")

    # -----------------------------------------------------------------
    # LAYOUT PRINCIPAL
    # -----------------------------------------------------------------

    def _create_layout(self):
        """Cria o layout com menu lateral e área de conteúdo."""
        # Container principal
        main_frame = ttkb.Frame(self.window)
        main_frame.pack(fill=BOTH, expand=True)

        # --- Menu lateral ---
        self.sidebar = ttkb.Frame(main_frame, width=220, bootstyle="light")
        self.sidebar.pack(side=LEFT, fill=Y)
        self.sidebar.pack_propagate(False)

        # Logo no menu
        ttkb.Label(
            self.sidebar, text="MENTORIA 2.0", font=FONT_TITLE,
            bootstyle="primary", anchor="center",
        ).pack(fill=X, pady=(20, 2), padx=10)
        ttkb.Label(
            self.sidebar, text="Assistente de Estudos", font=FONT_BODY,
            anchor="center",
        ).pack(fill=X, pady=(0, 20), padx=10)
        ttkb.Separator(self.sidebar).pack(fill=X, padx=10, pady=5)

        # Botões do menu
        menu_items = [
            ("🏠  Início", "inicio"),
            ("📚  Perguntas e Respostas", "perguntas"),
            ("📝  Atividades de Testes", "atividades"),
            ("📋  Histórico", "historico"),
            ("📊  Progresso", "progresso"),
            ("ℹ️  Sobre", "sobre"),
        ]

        self.menu_buttons = {}
        for label, screen_id in menu_items:
            btn = ttkb.Button(
                self.sidebar, text=label, bootstyle="light",
                command=lambda s=screen_id: self.show_screen(s),
                width=22,
            )
            btn.pack(fill=X, padx=10, pady=3)
            self.menu_buttons[screen_id] = btn

        # Rodapé do menu
        ttkb.Label(
            self.sidebar, text="Desenvolvido por Adalton",
            font=FONT_SMALL, anchor="center", foreground="#888",
        ).pack(side=BOTTOM, fill=X, pady=(0, 10), padx=10)

        # --- Área de conteúdo ---
        self.content_area = ttkb.Frame(main_frame)
        self.content_area.pack(side=LEFT, fill=BOTH, expand=True)

        # Criar todas as telas
        self.screens = {}
        self._create_screen_inicio()
        self._create_screen_perguntas()
        self._create_screen_atividades()
        self._create_screen_historico()
        self._create_screen_progresso()
        self._create_screen_sobre()

    def show_screen(self, screen_id):
        """Mostra uma tela e esconde as outras."""
        for sid, frame in self.screens.items():
            frame.pack_forget()

        if screen_id in self.screens:
            self.screens[screen_id].pack(fill=BOTH, expand=True)
            self.current_screen = screen_id

        # Atualizar visual dos botões do menu
        for sid, btn in self.menu_buttons.items():
            if sid == screen_id:
                btn.configure(bootstyle="primary")
            else:
                btn.configure(bootstyle="light")

        # Atualizar dados dinâmicos
        if screen_id == "historico":
            self._refresh_historico()
        elif screen_id == "progresso":
            self._refresh_progresso()

    # -----------------------------------------------------------------
    # HELPERS
    # -----------------------------------------------------------------

    def _create_card(self, parent, title=None, **pack_kwargs):
        """Cria um frame estilo cartão com borda e padding."""
        card = ttkb.Labelframe(parent, text=title or "", padding=CARD_PAD,
                               bootstyle="default")
        card.pack(fill=X, padx=PAD_X, pady=PAD_Y, **pack_kwargs)
        return card

    def _add_watermark(self, parent):
        """Adiciona marca d'água discreta."""
        ttkb.Label(
            parent, text="MENTORIA 2.0 — por Júlio de Lima",
            font=FONT_WATERMARK, foreground="#c0c0c0", anchor="center",
        ).pack(side=BOTTOM, fill=X, pady=(10, 5))

    def _add_footer(self, parent):
        """Adiciona rodapé."""
        ttkb.Label(
            parent, text="Desenvolvido por Adalton",
            font=FONT_SMALL, foreground="#999", anchor="center",
        ).pack(side=BOTTOM, fill=X, pady=(0, 5))

    # =================================================================
    # TELA INÍCIO
    # =================================================================

    def _create_screen_inicio(self):
        """Cria a tela de início."""
        frame = ScrolledFrame(self.content_area, autohide=True)
        self.screens["inicio"] = frame

        inner = frame

        # Cabeçalho
        ttkb.Label(
            inner, text="MENTORIA 2.0", font=FONT_TITLE,
            bootstyle="primary", anchor="center",
        ).pack(fill=X, pady=(30, 5), padx=PAD_X)
        ttkb.Label(
            inner, text="Assistente de Estudos — Testes de Software",
            font=FONT_SUBTITLE, anchor="center",
        ).pack(fill=X, pady=(0, 20), padx=PAD_X)

        # Descrição
        desc_card = self._create_card(inner, title="Bem-vindo!")
        ttkb.Label(
            desc_card,
            text=(
                "Este aplicativo foi criado para apoiar seus estudos de Testes de Software.\n"
                "Consulte os conteúdos dos Módulos 1 e 2, pratique exercícios e acompanhe\n"
                "seu progresso. As respostas são baseadas nos materiais da Mentoria."
            ),
            font=FONT_BODY, wraplength=750, justify="left",
        ).pack(fill=X, pady=5)

        # Cartões de funcionalidades
        features = [
            ("📚 Perguntas e Respostas",
             "Pesquise perguntas e receba respostas baseadas nos Módulos 1 e 2."),
            ("📝 Atividades de Testes",
             "Pratique com 10 exercícios de técnicas de teste aprendidas na Mentoria."),
            ("📋 Histórico",
             "Consulte suas perguntas, avaliações, casos de teste e defeitos."),
            ("📊 Progresso",
             "Acompanhe seu desempenho nas atividades práticas."),
        ]

        for title, desc in features:
            card = self._create_card(inner, title=title)
            ttkb.Label(card, text=desc, font=FONT_BODY, wraplength=700,
                       justify="left").pack(fill=X)

        self._add_watermark(inner)

    # =================================================================
    # TELA PERGUNTAS E RESPOSTAS
    # =================================================================

    def _create_screen_perguntas(self):
        """Cria a tela de perguntas e respostas."""
        frame = ScrolledFrame(self.content_area, autohide=True)
        self.screens["perguntas"] = frame
        inner = frame

        ttkb.Label(inner, text="📚 Perguntas e Respostas", font=FONT_TITLE,
                   anchor="w").pack(fill=X, padx=PAD_X, pady=(20, 10))

        # Seleção de módulo
        mod_card = self._create_card(inner, title="Escolha o módulo")
        self.module_var = tk.StringVar(value="Todos os módulos")
        module_combo = ttkb.Combobox(
            mod_card, textvariable=self.module_var, font=FONT_BODY,
            values=[
                "Módulo 1 — Fundamentos e Mentalidade",
                "Módulo 2 — Modelagem, Documentação e Execução",
                "Todos os módulos",
            ],
            state="readonly", width=50,
        )
        module_combo.pack(fill=X, pady=5)

        # Campo de pergunta
        q_card = self._create_card(inner, title="Digite sua pergunta")
        ttkb.Label(
            q_card,
            text="Exemplos: O que é teste exploratório? | Qual a diferença entre severidade e prioridade?",
            font=FONT_SMALL, foreground="#777",
        ).pack(fill=X, pady=(0, 5))
        self.question_text = ttkb.Text(q_card, height=3, font=FONT_BODY, wrap="word")
        self.question_text.pack(fill=X, pady=5)

        ttkb.Button(
            q_card, text="🔎  Pesquisar resposta", bootstyle="primary",
            command=self._search_answer, padding=(20, 10),
        ).pack(pady=10)

        # Área de resposta
        r_card = self._create_card(inner, title="Resposta")
        self.answer_text = ttkb.Text(
            r_card, height=10, font=FONT_BODY, wrap="word", state="disabled",
        )
        self.answer_text.pack(fill=BOTH, pady=5)
        self.source_label = ttkb.Label(r_card, text="", font=FONT_SMALL,
                                       foreground="#0066cc")
        self.source_label.pack(fill=X, pady=(0, 5))

        # Avaliação
        eval_card = self._create_card(inner, title="Avalie o nível desta resposta")
        star_frame = ttkb.Frame(eval_card)
        star_frame.pack(pady=10)

        self.star_labels = []
        self.star_rating = 0
        for i in range(5):
            lbl = ttkb.Label(
                star_frame, text=STAR_EMPTY, font=FONT_STAR,
                foreground="#ffc107", cursor="hand2",
            )
            lbl.pack(side=LEFT, padx=4)
            lbl.bind("<Button-1>", lambda e, idx=i: self._set_rating(idx + 1))
            self.star_labels.append(lbl)

        ttkb.Label(eval_card, text="Observação (opcional):", font=FONT_BODY,
                   ).pack(fill=X, pady=(10, 2))
        self.obs_text = ttkb.Text(eval_card, height=2, font=FONT_BODY, wrap="word")
        self.obs_text.pack(fill=X, pady=5)

        ttkb.Button(
            eval_card, text="💾  Salvar avaliação", bootstyle="success",
            command=self._save_evaluation, padding=(20, 10),
        ).pack(pady=10)

        self._add_watermark(inner)

    def _search_answer(self):
        """Pesquisa resposta na base de conhecimento."""
        pergunta = self.question_text.get("1.0", "end").strip()
        if not pergunta:
            messagebox.showwarning("Atenção", "Digite uma pergunta para pesquisar.")
            return

        # Determinar módulo
        mod = self.module_var.get()
        if "Módulo 1" in mod:
            modulo = "modulo1"
        elif "Módulo 2" in mod:
            modulo = "modulo2"
        else:
            modulo = "todos"

        self.current_module = mod

        # Pesquisar
        resultados = knowledge_base.pesquisar(pergunta, modulo)
        resposta, fonte = knowledge_base.formatar_resposta(resultados)

        self.current_response = resposta

        # Exibir resposta
        self.answer_text.configure(state="normal")
        self.answer_text.delete("1.0", "end")
        self.answer_text.insert("1.0", resposta)
        self.answer_text.configure(state="disabled")

        # Exibir fonte
        if fonte:
            self.source_label.configure(text=f"📎 Fonte: {fonte}")
        else:
            self.source_label.configure(text="")

        # Resetar avaliação
        self._set_rating(0)
        self._evaluation_saved = False

    def _set_rating(self, rating):
        """Define a avaliação em estrelas."""
        self.star_rating = rating
        for i, lbl in enumerate(self.star_labels):
            lbl.configure(text=STAR_FULL if i < rating else STAR_EMPTY)

    def _save_evaluation(self):
        """Salva a avaliação no banco de dados."""
        if getattr(self, "_evaluation_saved", False):
            messagebox.showinfo("Aviso", "Esta avaliação já foi salva. Para avaliar novamente, faça uma nova pesquisa.")
            return

        pergunta = self.question_text.get("1.0", "end").strip()
        if not pergunta:
            messagebox.showwarning("Atenção", "Faça uma pergunta antes de avaliar.")
            return
        if self.star_rating == 0:
            messagebox.showwarning("Atenção", "Selecione uma avaliação de 1 a 5 estrelas.")
            return
        if not self.current_response:
            messagebox.showwarning("Atenção", "Pesquise uma resposta antes de avaliar.")
            return

        obs = self.obs_text.get("1.0", "end").strip()
        database.salvar_avaliacao(
            self.current_module, pergunta, self.current_response,
            self.star_rating, obs,
        )
        self._evaluation_saved = True
        # Resetar campos para evitar duplicados por cliques sucessivos
        self._set_rating(0)
        self.obs_text.delete("1.0", "end")
        self.current_response = ""
        messagebox.showinfo("Sucesso", "Avaliação salva com sucesso! ✅")



    # =================================================================
    # TELA ATIVIDADES DE TESTES
    # =================================================================

    def _create_screen_atividades(self):
        """Cria a tela principal de atividades."""
        frame = ttkb.Frame(self.content_area)
        self.screens["atividades"] = frame

        # Container para lista e conteúdo da atividade
        self.act_list_frame = ScrolledFrame(frame, autohide=True)
        self.act_list_frame.pack(fill=BOTH, expand=True)

        self.act_detail_frame = ScrolledFrame(frame, autohide=True)

        self._build_activity_list()

    def _build_activity_list(self):
        """Constrói a lista de atividades como cartões."""
        inner = self.act_list_frame

        ttkb.Label(inner, text="📝 Atividades de Testes", font=FONT_TITLE,
                   anchor="w").pack(fill=X, padx=PAD_X, pady=(20, 5))
        ttkb.Label(
            inner,
            text="Pratique as técnicas de testes aprendidas nos Módulos 1 e 2.",
            font=FONT_BODY, foreground="#555",
        ).pack(fill=X, padx=PAD_X, pady=(0, 15))

        for num, nome in activities.NOMES_ATIVIDADES.items():
            card = ttkb.Frame(inner, padding=12)
            card.pack(fill=X, padx=PAD_X, pady=4)

            row = ttkb.Frame(card)
            row.pack(fill=X)

            ttkb.Label(
                row, text=f"Atividade {num}", font=FONT_BODY_BOLD,
                bootstyle="primary", width=14,
            ).pack(side=LEFT)
            ttkb.Label(row, text=nome, font=FONT_BODY).pack(side=LEFT, padx=10)
            ttkb.Button(
                row, text="Iniciar ▶", bootstyle="outline-primary",
                command=lambda n=num: self._show_activity(n),
                padding=(15, 5),
            ).pack(side=RIGHT)

        self._add_watermark(inner)

    def _show_activity(self, num):
        """Mostra a tela de uma atividade específica."""
        self.act_list_frame.pack_forget()

        # Limpar e recriar o frame de detalhes
        self.act_detail_frame.destroy()
        self.act_detail_frame = ScrolledFrame(self.screens["atividades"], autohide=True)
        self.act_detail_frame.pack(fill=BOTH, expand=True)

        inner = self.act_detail_frame

        # Botão voltar
        ttkb.Button(
            inner, text="← Voltar às atividades", bootstyle="outline-secondary",
            command=self._back_to_activity_list, padding=(15, 8),
        ).pack(anchor="w", padx=PAD_X, pady=(15, 10))

        nome = activities.NOMES_ATIVIDADES.get(num, "")
        ttkb.Label(inner, text=f"Atividade {num}: {nome}", font=FONT_TITLE,
                   anchor="w", wraplength=800).pack(fill=X, padx=PAD_X, pady=(5, 15))

        # Chamar o construtor da atividade
        builders = {
            1: self._build_act_valor_limite,
            2: self._build_act_particao,
            3: self._build_act_tabela_decisao,
            4: self._build_act_checking_testing,
            5: self._build_act_adhoc_exploratorio,
            6: self._build_act_charter,
            7: self._build_act_severidade_prioridade,
            8: self._build_act_caso_teste,
            9: self._build_act_gherkin,
            10: self._build_act_defeito,
        }
        builder = builders.get(num)
        if builder:
            builder(inner)

        self._add_watermark(inner)

    def _back_to_activity_list(self):
        """Volta para a lista de atividades."""
        self.act_detail_frame.pack_forget()
        self.act_list_frame.pack(fill=BOTH, expand=True)

    # -----------------------------------------------------------------
    # ATIVIDADE 1: VALOR LIMITE
    # -----------------------------------------------------------------

    def _build_act_valor_limite(self, parent):
        """Constrói a atividade de Valor Limite."""
        card = self._create_card(parent, title="Enunciado")
        ttkb.Label(
            card, text=f"Regra: {activities.VALOR_LIMITE_REGRA}", font=FONT_BODY_BOLD,
        ).pack(fill=X, pady=5)
        ttkb.Label(
            card,
            text=(
                "Para cada valor abaixo, identifique se está:\n"
                "• Abaixo do limite\n• No limite\n• Acima do limite"
            ),
            font=FONT_BODY, wraplength=700, justify="left",
        ).pack(fill=X, pady=5)

        # Campos para resposta
        resp_card = self._create_card(parent, title="Sua resposta")
        self._vl_combos = []
        for cenario in activities.VALOR_LIMITE_CENARIOS:
            row = ttkb.Frame(resp_card)
            row.pack(fill=X, pady=5)
            ttkb.Label(row, text=f"  {cenario['label']}  →  ",
                       font=FONT_BODY_BOLD, width=16).pack(side=LEFT)
            var = tk.StringVar(value="Selecione...")
            combo = ttkb.Combobox(
                row, textvariable=var, font=FONT_BODY, width=22,
                values=activities.VALOR_LIMITE_OPCOES, state="readonly",
            )
            combo.pack(side=LEFT, padx=5)
            self._vl_combos.append((cenario, var))

        btn_frame = ttkb.Frame(resp_card)
        btn_frame.pack(fill=X, pady=10)
        ttkb.Button(
            btn_frame, text="✔ Verificar resposta", bootstyle="success",
            command=lambda: self._check_valor_limite(result_card),
            padding=(20, 10),
        ).pack(side=LEFT, padx=5)
        ttkb.Button(
            btn_frame, text="🔄 Tentar novamente", bootstyle="outline-warning",
            command=self._reset_valor_limite, padding=(20, 10),
        ).pack(side=LEFT, padx=5)

        # Resultado
        result_card = self._create_card(parent, title="Resultado")
        self._vl_result_label = ttkb.Label(
            result_card, text="Responda às questões acima e clique em Verificar.",
            font=FONT_BODY, wraplength=700, justify="left",
        )
        self._vl_result_label.pack(fill=X, pady=5)

    def _check_valor_limite(self, result_card):
        """Verifica as respostas do valor limite."""
        acertos = 0
        total = len(self._vl_combos)
        detalhes = []

        for cenario, var in self._vl_combos:
            resposta = var.get()
            if resposta == "Selecione...":
                messagebox.showwarning("Atenção", "Selecione uma opção para cada valor.")
                return
            correto = resposta == cenario["resposta_correta"]
            if correto:
                acertos += 1
            status = "✅ Correto" if correto else f"❌ Incorreto (correto: {cenario['resposta_correta']})"
            detalhes.append(f"{cenario['label']}: {status}\n{cenario['explicacao']}")

        texto = "\n\n".join(detalhes)
        texto += f"\n\n{'─' * 40}\n"
        texto += f"Resultado: {acertos}/{total} acertos\n\n"
        texto += activities.VALOR_LIMITE_EXPLICACAO_GERAL

        self._vl_result_label.configure(text=texto)

        # Registrar progresso
        database.registrar_progresso(
            activities.NOMES_ATIVIDADES[1],
            acertos == total,
            f"{acertos}/{total} acertos",
        )

    def _reset_valor_limite(self):
        """Reseta os campos da atividade de valor limite."""
        for _, var in self._vl_combos:
            var.set("Selecione...")
        self._vl_result_label.configure(
            text="Responda às questões acima e clique em Verificar.")

    # -----------------------------------------------------------------
    # ATIVIDADE 2: PARTICIONAMENTO DE EQUIVALÊNCIA
    # -----------------------------------------------------------------

    def _build_act_particao(self, parent):
        """Constrói a atividade de Particionamento de Equivalência."""
        card = self._create_card(parent, title="Enunciado")
        ttkb.Label(
            card, text=f"Regra: {activities.PARTICAO_REGRA}",
            font=FONT_BODY_BOLD,
        ).pack(fill=X, pady=5)
        ttkb.Label(
            card,
            text=(
                "Identifique as duas classes de equivalência e forneça\n"
                "um valor de exemplo para cada uma."
            ),
            font=FONT_BODY, wraplength=700, justify="left",
        ).pack(fill=X, pady=5)

        resp_card = self._create_card(parent, title="Sua resposta")

        # Classe Inválida
        ttkb.Label(resp_card, text="Classe INVÁLIDA — Informe um valor de exemplo:",
                   font=FONT_BODY_BOLD).pack(fill=X, pady=(5, 2))
        ttkb.Label(resp_card, text="(Valores que NÃO devem ser aceitos pela regra)",
                   font=FONT_SMALL, foreground="#777").pack(fill=X)
        self._part_inv = ttkb.Entry(resp_card, font=FONT_BODY)
        self._part_inv.pack(fill=X, pady=5)

        # Classe Válida
        ttkb.Label(resp_card, text="Classe VÁLIDA — Informe um valor de exemplo:",
                   font=FONT_BODY_BOLD).pack(fill=X, pady=(10, 2))
        ttkb.Label(resp_card, text="(Valores que DEVEM ser aceitos pela regra)",
                   font=FONT_SMALL, foreground="#777").pack(fill=X)
        self._part_val = ttkb.Entry(resp_card, font=FONT_BODY)
        self._part_val.pack(fill=X, pady=5)

        btn_frame = ttkb.Frame(resp_card)
        btn_frame.pack(fill=X, pady=10)
        ttkb.Button(
            btn_frame, text="✔ Verificar resposta", bootstyle="success",
            command=self._check_particao, padding=(20, 10),
        ).pack(side=LEFT, padx=5)
        ttkb.Button(
            btn_frame, text="🔄 Tentar novamente", bootstyle="outline-warning",
            command=self._reset_particao, padding=(20, 10),
        ).pack(side=LEFT, padx=5)

        result_card = self._create_card(parent, title="Resultado")
        self._part_result = ttkb.Label(
            result_card, text="Informe os valores e clique em Verificar.",
            font=FONT_BODY, wraplength=700, justify="left",
        )
        self._part_result.pack(fill=X, pady=5)

    def _check_particao(self):
        """Verifica as respostas do particionamento."""
        inv_text = self._part_inv.get().strip()
        val_text = self._part_val.get().strip()

        if not inv_text or not val_text:
            messagebox.showwarning("Atenção", "Preencha os dois campos.")
            return

        classe_inv, msg_inv = activities.verificar_particao(inv_text)
        classe_val, msg_val = activities.verificar_particao(val_text)

        if classe_inv is None:
            self._part_result.configure(text=f"Classe Inválida: {msg_inv}")
            return
        if classe_val is None:
            self._part_result.configure(text=f"Classe Válida: {msg_val}")
            return

        acertou_inv = classe_inv == "invalida"
        acertou_val = classe_val == "valida"
        acertos = int(acertou_inv) + int(acertou_val)

        texto = f"{'✅' if acertou_inv else '❌'} Classe Inválida: {msg_inv}\n\n"
        texto += f"{'✅' if acertou_val else '❌'} Classe Válida: {msg_val}\n\n"
        texto += f"{'─' * 40}\n"
        texto += f"Resultado: {acertos}/2 acertos\n\n"
        texto += activities.PARTICAO_EXPLICACAO

        self._part_result.configure(text=texto)
        database.registrar_progresso(
            activities.NOMES_ATIVIDADES[2], acertos == 2,
            f"{acertos}/2 acertos",
        )

    def _reset_particao(self):
        """Reseta campos."""
        self._part_inv.delete(0, "end")
        self._part_val.delete(0, "end")
        self._part_result.configure(text="Informe os valores e clique em Verificar.")

    # -----------------------------------------------------------------
    # ATIVIDADE 3: TABELA DE DECISÃO
    # -----------------------------------------------------------------

    def _build_act_tabela_decisao(self, parent):
        """Constrói a atividade de Tabela de Decisão."""
        card = self._create_card(parent, title="Enunciado")
        ttkb.Label(
            card,
            text=(
                "Considere as seguintes condições para uma transferência bancária:\n\n"
                "• Condição 1: Valor (menor que R$ 5.000 OU maior/igual a R$ 5.000)\n"
                "• Condição 2: Token (Válido, Inválido ou Não informado)\n\n"
                "Monte as combinações possíveis e selecione o resultado esperado."
            ),
            font=FONT_BODY, wraplength=700, justify="left",
        ).pack(fill=X, pady=5)

        resp_card = self._create_card(parent, title="Monte as combinações")
        self._td_combos = []
        for i, comb in enumerate(activities.TABELA_DECISAO_COMBINACOES):
            row = ttkb.Frame(resp_card)
            row.pack(fill=X, pady=4)
            ttkb.Label(
                row,
                text=f"Cenário {i+1}: Valor {comb['valor']} + Token {comb['token']}  →",
                font=FONT_BODY, width=55, anchor="w",
            ).pack(side=LEFT)
            var = tk.StringVar(value="Selecione...")
            combo = ttkb.Combobox(
                row, textvariable=var, font=FONT_BODY, width=35,
                values=activities.TABELA_DECISAO_OPCOES,
                state="readonly",
            )
            combo.pack(side=LEFT, padx=5)
            self._td_combos.append((comb, var))

        btn_frame = ttkb.Frame(resp_card)
        btn_frame.pack(fill=X, pady=10)
        ttkb.Button(
            btn_frame, text="✔ Verificar resposta", bootstyle="success",
            command=self._check_tabela_decisao, padding=(20, 10),
        ).pack(side=LEFT, padx=5)
        ttkb.Button(
            btn_frame, text="🔄 Tentar novamente", bootstyle="outline-warning",
            command=self._reset_tabela_decisao, padding=(20, 10),
        ).pack(side=LEFT, padx=5)

        result_card = self._create_card(parent, title="Resultado")
        self._td_result = ttkb.Label(
            result_card, text="Selecione os resultados e clique em Verificar.",
            font=FONT_BODY, wraplength=700, justify="left",
        )
        self._td_result.pack(fill=X, pady=5)

    def _check_tabela_decisao(self):
        """Verifica respostas da tabela de decisão."""
        acertos = 0
        total = len(self._td_combos)
        detalhes = []

        for comb, var in self._td_combos:
            resp = var.get()
            if resp == "Selecione...":
                messagebox.showwarning("Atenção", "Selecione um resultado para cada cenário.")
                return

            correto, opcao_esperada, esperado = activities.validar_cenario_tabela_decisao(comb, resp)

            if correto:
                acertos += 1
            status = "✅" if correto else "❌"
            detalhes.append(
                f"{status} Valor {comb['valor']} + Token {comb['token']}:\n"
                f"   Sua resposta: {resp}\n"
                f"   Esperado: {opcao_esperada}"
            )

        texto = "\n\n".join(detalhes)
        texto += f"\n\n{'─' * 40}\n"
        texto += f"Resultado: {acertos}/{total} acertos\n\n"
        texto += activities.TABELA_DECISAO_EXPLICACAO

        self._td_result.configure(text=texto)
        database.registrar_progresso(
            activities.NOMES_ATIVIDADES[3], acertos == total,
            f"{acertos}/{total} acertos",
        )

    def _reset_tabela_decisao(self):
        for _, var in self._td_combos:
            var.set("Selecione...")
        self._td_result.configure(
            text="Selecione os resultados e clique em Verificar.")

    # -----------------------------------------------------------------
    # ATIVIDADE 4: CHECKING × TESTING
    # -----------------------------------------------------------------

    def _build_act_checking_testing(self, parent):
        """Constrói a atividade Checking × Testing."""
        card = self._create_card(parent, title="Enunciado")
        ttkb.Label(
            card,
            text=(
                "Para cada situação abaixo, identifique se representa\n"
                "CHECKING (verificação de resultado conhecido) ou\n"
                "TESTING (investigação exploratória)."
            ),
            font=FONT_BODY, wraplength=700, justify="left",
        ).pack(fill=X, pady=5)

        resp_card = self._create_card(parent, title="Sua resposta")
        self._ct_combos = []
        for i, cenario in enumerate(activities.CENARIOS_CHECKING_TESTING):
            frame = ttkb.Frame(resp_card)
            frame.pack(fill=X, pady=8)
            ttkb.Label(
                frame, text=f"Situação {i+1}:",
                font=FONT_BODY_BOLD, bootstyle="primary",
            ).pack(fill=X)
            ttkb.Label(
                frame, text=cenario["descricao"],
                font=FONT_BODY, wraplength=680, justify="left",
            ).pack(fill=X, pady=(2, 5))
            var = tk.StringVar(value="Selecione...")
            combo = ttkb.Combobox(
                frame, textvariable=var, font=FONT_BODY, width=20,
                values=["Checking", "Testing"], state="readonly",
            )
            combo.pack(anchor="w")
            self._ct_combos.append((cenario, var))
            if i < len(activities.CENARIOS_CHECKING_TESTING) - 1:
                ttkb.Separator(resp_card).pack(fill=X, pady=5)

        btn_frame = ttkb.Frame(resp_card)
        btn_frame.pack(fill=X, pady=10)
        ttkb.Button(
            btn_frame, text="✔ Verificar resposta", bootstyle="success",
            command=self._check_ct, padding=(20, 10),
        ).pack(side=LEFT, padx=5)
        ttkb.Button(
            btn_frame, text="🔄 Tentar novamente", bootstyle="outline-warning",
            command=self._reset_ct, padding=(20, 10),
        ).pack(side=LEFT, padx=5)

        result_card = self._create_card(parent, title="Resultado")
        self._ct_result = ttkb.Label(
            result_card, text="Selecione as respostas e clique em Verificar.",
            font=FONT_BODY, wraplength=700, justify="left",
        )
        self._ct_result.pack(fill=X, pady=5)

    def _check_ct(self):
        acertos = 0
        total = len(self._ct_combos)
        detalhes = []
        for i, (cenario, var) in enumerate(self._ct_combos):
            resp = var.get()
            if resp == "Selecione...":
                messagebox.showwarning("Atenção", "Selecione uma opção para cada situação.")
                return
            correto = resp == cenario["resposta_correta"]
            if correto:
                acertos += 1
            status = "✅ Correto!" if correto else f"❌ Incorreto (correto: {cenario['resposta_correta']})"
            detalhes.append(f"Situação {i+1}: {status}\n{cenario['justificativa']}")

        texto = "\n\n".join(detalhes)
        texto += f"\n\n{'─' * 40}\nResultado: {acertos}/{total} acertos"
        texto += (
            "\n\nChecking verifica uma expectativa conhecida. "
            "Testing investiga com perguntas e hipóteses.\n"
            "Fonte: Módulo 2, itens 2 e 3."
        )
        self._ct_result.configure(text=texto)
        database.registrar_progresso(
            activities.NOMES_ATIVIDADES[4], acertos == total,
            f"{acertos}/{total} acertos",
        )

    def _reset_ct(self):
        for _, var in self._ct_combos:
            var.set("Selecione...")
        self._ct_result.configure(text="Selecione as respostas e clique em Verificar.")

    # -----------------------------------------------------------------
    # ATIVIDADE 5: AD HOC × EXPLORATÓRIO
    # -----------------------------------------------------------------

    def _build_act_adhoc_exploratorio(self, parent):
        """Constrói a atividade Ad hoc × Exploratório."""
        card = self._create_card(parent, title="Enunciado")
        ttkb.Label(
            card,
            text=(
                "Para cada cenário, identifique se representa:\n"
                "• Teste AD HOC (sem roteiro, exploração rápida)\n"
                "• Teste EXPLORATÓRIO (aprendizagem + desenho + execução)\n"
                "• SBTM (sessão estruturada com charter)"
            ),
            font=FONT_BODY, wraplength=700, justify="left",
        ).pack(fill=X, pady=5)

        resp_card = self._create_card(parent, title="Sua resposta")
        self._ae_combos = []
        for i, cenario in enumerate(activities.CENARIOS_ADHOC_EXPLORATORIO):
            frame = ttkb.Frame(resp_card)
            frame.pack(fill=X, pady=8)
            ttkb.Label(frame, text=f"Cenário {i+1}:", font=FONT_BODY_BOLD,
                       bootstyle="primary").pack(fill=X)
            ttkb.Label(frame, text=cenario["descricao"], font=FONT_BODY,
                       wraplength=680, justify="left").pack(fill=X, pady=(2, 5))
            var = tk.StringVar(value="Selecione...")
            combo = ttkb.Combobox(
                frame, textvariable=var, font=FONT_BODY, width=22,
                values=["Ad hoc", "Exploratório", "SBTM"], state="readonly",
            )
            combo.pack(anchor="w")
            self._ae_combos.append((cenario, var))
            if i < len(activities.CENARIOS_ADHOC_EXPLORATORIO) - 1:
                ttkb.Separator(resp_card).pack(fill=X, pady=5)

        btn_frame = ttkb.Frame(resp_card)
        btn_frame.pack(fill=X, pady=10)
        ttkb.Button(btn_frame, text="✔ Verificar resposta", bootstyle="success",
                    command=self._check_ae, padding=(20, 10)).pack(side=LEFT, padx=5)
        ttkb.Button(btn_frame, text="🔄 Tentar novamente", bootstyle="outline-warning",
                    command=self._reset_ae, padding=(20, 10)).pack(side=LEFT, padx=5)

        result_card = self._create_card(parent, title="Resultado")
        self._ae_result = ttkb.Label(
            result_card, text="Selecione as respostas e clique em Verificar.",
            font=FONT_BODY, wraplength=700, justify="left",
        )
        self._ae_result.pack(fill=X, pady=5)

    def _check_ae(self):
        acertos = 0
        total = len(self._ae_combos)
        detalhes = []
        for i, (cenario, var) in enumerate(self._ae_combos):
            resp = var.get()
            if resp == "Selecione...":
                messagebox.showwarning("Atenção", "Selecione uma opção para cada cenário.")
                return
            correto = resp == cenario["resposta_correta"]
            if correto:
                acertos += 1
            status = "✅ Correto!" if correto else f"❌ Incorreto (correto: {cenario['resposta_correta']})"
            detalhes.append(f"Cenário {i+1}: {status}\n{cenario['justificativa']}")

        texto = "\n\n".join(detalhes)
        texto += f"\n\n{'─' * 40}\nResultado: {acertos}/{total} acertos"
        texto += "\n\nFonte: Módulo 2, itens 4 a 7."
        self._ae_result.configure(text=texto)
        database.registrar_progresso(
            activities.NOMES_ATIVIDADES[5], acertos == total,
            f"{acertos}/{total} acertos",
        )

    def _reset_ae(self):
        for _, var in self._ae_combos:
            var.set("Selecione...")
        self._ae_result.configure(text="Selecione as respostas e clique em Verificar.")

    # -----------------------------------------------------------------
    # ATIVIDADE 6: TEST CHARTER / SBTM
    # -----------------------------------------------------------------

    def _build_act_charter(self, parent):
        """Constrói a atividade de Test Charter."""
        card = self._create_card(parent, title="Enunciado")
        ttkb.Label(
            card,
            text=(
                "Monte um Test Charter seguindo o modelo:\n\n"
                f'"{activities.CHARTER_MODELO}"\n\n'
                "Preencha os três elementos essenciais."
            ),
            font=FONT_BODY, wraplength=700, justify="left",
        ).pack(fill=X, pady=5)

        resp_card = self._create_card(parent, title="Sua resposta")

        ttkb.Label(resp_card, text="ALVO — O que será explorado:",
                   font=FONT_BODY_BOLD).pack(fill=X, pady=(5, 2))
        ttkb.Label(resp_card, text='Ex: "o módulo de pagamento"',
                   font=FONT_SMALL, foreground="#777").pack(fill=X)
        self._charter_alvo = ttkb.Entry(resp_card, font=FONT_BODY)
        self._charter_alvo.pack(fill=X, pady=5)

        ttkb.Label(resp_card, text="RECURSOS/TÉCNICAS — Como será explorado:",
                   font=FONT_BODY_BOLD).pack(fill=X, pady=(10, 2))
        ttkb.Label(resp_card, text='Ex: "dados inválidos e valores extremos"',
                   font=FONT_SMALL, foreground="#777").pack(fill=X)
        self._charter_recursos = ttkb.Entry(resp_card, font=FONT_BODY)
        self._charter_recursos.pack(fill=X, pady=5)

        ttkb.Label(resp_card, text="INFORMAÇÃO — O que deseja descobrir:",
                   font=FONT_BODY_BOLD).pack(fill=X, pady=(10, 2))
        ttkb.Label(resp_card, text='Ex: "como o sistema trata erros de validação"',
                   font=FONT_SMALL, foreground="#777").pack(fill=X)
        self._charter_info = ttkb.Entry(resp_card, font=FONT_BODY)
        self._charter_info.pack(fill=X, pady=5)

        btn_frame = ttkb.Frame(resp_card)
        btn_frame.pack(fill=X, pady=10)
        ttkb.Button(btn_frame, text="✔ Verificar resposta", bootstyle="success",
                    command=self._check_charter, padding=(20, 10)).pack(side=LEFT, padx=5)
        ttkb.Button(btn_frame, text="🔄 Tentar novamente", bootstyle="outline-warning",
                    command=self._reset_charter, padding=(20, 10)).pack(side=LEFT, padx=5)

        result_card = self._create_card(parent, title="Resultado")
        self._charter_result = ttkb.Label(
            result_card, text="Preencha os campos e clique em Verificar.",
            font=FONT_BODY, wraplength=700, justify="left",
        )
        self._charter_result.pack(fill=X, pady=5)

    def _check_charter(self):
        alvo = self._charter_alvo.get()
        recursos = self._charter_recursos.get()
        info = self._charter_info.get()

        valido, msg, charter = activities.validar_test_charter(alvo, recursos, info)

        texto = msg
        if charter:
            texto += f'\n\n📋 Seu Test Charter:\n"{charter}"'
        texto += f"\n\n{'─' * 40}\n{activities.CHARTER_EXPLICACAO}"

        self._charter_result.configure(text=texto)
        database.registrar_progresso(
            activities.NOMES_ATIVIDADES[6], valido,
            "Charter válido" if valido else "Charter incompleto",
        )

    def _reset_charter(self):
        self._charter_alvo.delete(0, "end")
        self._charter_recursos.delete(0, "end")
        self._charter_info.delete(0, "end")
        self._charter_result.configure(text="Preencha os campos e clique em Verificar.")

    # -----------------------------------------------------------------
    # ATIVIDADE 7: SEVERIDADE × PRIORIDADE
    # -----------------------------------------------------------------

    def _build_act_severidade_prioridade(self, parent):
        """Constrói a atividade Severidade × Prioridade."""
        card = self._create_card(parent, title="Enunciado")
        ttkb.Label(
            card,
            text=(
                "Para cada situação de defeito, identifique a Severidade e a Prioridade.\n\n"
                "Severidade = impacto do problema\n"
                "Prioridade = urgência de tratamento"
            ),
            font=FONT_BODY, wraplength=700, justify="left",
        ).pack(fill=X, pady=5)

        resp_card = self._create_card(parent, title="Sua resposta")
        self._sp_combos = []
        for i, cenario in enumerate(activities.CENARIOS_SEVERIDADE_PRIORIDADE):
            frame = ttkb.Frame(resp_card)
            frame.pack(fill=X, pady=8)
            ttkb.Label(frame, text=f"Defeito {i+1}:", font=FONT_BODY_BOLD,
                       bootstyle="primary").pack(fill=X)
            ttkb.Label(frame, text=cenario["descricao"], font=FONT_BODY,
                       wraplength=680, justify="left").pack(fill=X, pady=(2, 5))

            sel_row = ttkb.Frame(frame)
            sel_row.pack(fill=X, pady=2)
            ttkb.Label(sel_row, text="Severidade:", font=FONT_BODY).pack(side=LEFT)
            sev_var = tk.StringVar(value="Selecione...")
            ttkb.Combobox(
                sel_row, textvariable=sev_var, font=FONT_BODY, width=12,
                values=activities.SEVERIDADE_OPCOES, state="readonly",
            ).pack(side=LEFT, padx=(5, 20))
            ttkb.Label(sel_row, text="Prioridade:", font=FONT_BODY).pack(side=LEFT)
            pri_var = tk.StringVar(value="Selecione...")
            ttkb.Combobox(
                sel_row, textvariable=pri_var, font=FONT_BODY, width=12,
                values=activities.PRIORIDADE_OPCOES, state="readonly",
            ).pack(side=LEFT, padx=5)
            self._sp_combos.append((cenario, sev_var, pri_var))
            if i < len(activities.CENARIOS_SEVERIDADE_PRIORIDADE) - 1:
                ttkb.Separator(resp_card).pack(fill=X, pady=5)

        btn_frame = ttkb.Frame(resp_card)
        btn_frame.pack(fill=X, pady=10)
        ttkb.Button(btn_frame, text="✔ Verificar resposta", bootstyle="success",
                    command=self._check_sp, padding=(20, 10)).pack(side=LEFT, padx=5)
        ttkb.Button(btn_frame, text="🔄 Tentar novamente", bootstyle="outline-warning",
                    command=self._reset_sp, padding=(20, 10)).pack(side=LEFT, padx=5)

        result_card = self._create_card(parent, title="Resultado")
        self._sp_result = ttkb.Label(
            result_card, text="Selecione as respostas e clique em Verificar.",
            font=FONT_BODY, wraplength=700, justify="left",
        )
        self._sp_result.pack(fill=X, pady=5)

    def _check_sp(self):
        detalhes = []
        acertos = 0
        total = len(self._sp_combos)
        for i, (cenario, sev_var, pri_var) in enumerate(self._sp_combos):
            sev = sev_var.get()
            pri = pri_var.get()
            if sev == "Selecione..." or pri == "Selecione...":
                messagebox.showwarning("Atenção", "Selecione severidade e prioridade para cada defeito.")
                return

            sev_ok, pri_ok, sev_status, pri_status, exp = activities.validar_severidade_prioridade(
                cenario, sev, pri
            )
            if sev_ok and pri_ok:
                acertos += 1

            detalhes.append(
                f"Defeito {i+1}:\n"
                f"  Severidade informada: {sev} → {sev_status}\n"
                f"  Prioridade informada: {pri} → {pri_status}\n"
                f"  💡 {exp}"
            )

        texto = "\n\n".join(detalhes)
        texto += f"\n\n{'─' * 40}\nResultado: {acertos}/{total} acertos\n\n"
        texto += activities.SEVERIDADE_PRIORIDADE_EXPLICACAO
        self._sp_result.configure(text=texto)
        database.registrar_progresso(
            activities.NOMES_ATIVIDADES[7], acertos == total,
            f"{acertos}/{total} acertos",
        )

    def _reset_sp(self):
        for _, sev, pri in self._sp_combos:
            sev.set("Selecione...")
            pri.set("Selecione...")
        self._sp_result.configure(text="Selecione as respostas e clique em Verificar.")

    # -----------------------------------------------------------------
    # ATIVIDADE 8: CASO DE TESTE
    # -----------------------------------------------------------------

    def _build_act_caso_teste(self, parent):
        """Constrói a atividade Caso de Teste."""
        card = self._create_card(parent, title="Enunciado")
        ttkb.Label(
            card,
            text=(
                "Crie um caso de teste completo. Preencha os campos abaixo.\n"
                "Os campos marcados com * são obrigatórios."
            ),
            font=FONT_BODY, wraplength=700, justify="left",
        ).pack(fill=X, pady=5)

        resp_card = self._create_card(parent, title="Formulário do Caso de Teste")
        self._ct_fields = {}

        for campo_id, nome, obrigatorio in activities.CASO_TESTE_CAMPOS:
            obr = " *" if obrigatorio else ""
            ttkb.Label(resp_card, text=f"{nome}{obr}:", font=FONT_BODY_BOLD,
                       ).pack(fill=X, pady=(8, 2))
            if campo_id in ("passos", "resultado_esperado", "pre_condicoes"):
                widget = ttkb.Text(resp_card, height=3, font=FONT_BODY, wrap="word")
            else:
                widget = ttkb.Entry(resp_card, font=FONT_BODY)
            widget.pack(fill=X, pady=2)
            self._ct_fields[campo_id] = widget

        btn_frame = ttkb.Frame(resp_card)
        btn_frame.pack(fill=X, pady=15)
        ttkb.Button(btn_frame, text="✔ Verificar e Salvar", bootstyle="success",
                    command=self._check_caso_teste, padding=(20, 10)).pack(side=LEFT, padx=5)
        ttkb.Button(btn_frame, text="🔄 Limpar campos", bootstyle="outline-warning",
                    command=self._reset_caso_teste, padding=(20, 10)).pack(side=LEFT, padx=5)

        result_card = self._create_card(parent, title="Resultado")
        self._caso_result = ttkb.Label(
            result_card, text="Preencha o formulário e clique em Verificar.",
            font=FONT_BODY, wraplength=700, justify="left",
        )
        self._caso_result.pack(fill=X, pady=5)

        # Explicação
        exp_card = self._create_card(parent, title="Sobre Casos de Teste")
        ttkb.Label(exp_card, text=activities.CASO_TESTE_EXPLICACAO, font=FONT_BODY,
                   wraplength=700, justify="left").pack(fill=X, pady=5)

    def _get_ct_value(self, campo_id):
        """Obtém o valor de um campo do caso de teste."""
        widget = self._ct_fields[campo_id]
        if isinstance(widget, ttkb.Text) or isinstance(widget, tk.Text):
            return widget.get("1.0", "end").strip()
        return widget.get().strip()

    def _check_caso_teste(self):
        campos = {}
        for campo_id in self._ct_fields:
            campos[campo_id] = self._get_ct_value(campo_id)

        # Se todos os campos estiverem vazios (ex: clique consecutivo logo após salvar)
        if not any(campos.values()):
            self._caso_result.configure(
                text="Preencha os campos obrigatórios para cadastrar um novo caso de teste."
            )
            return

        # Verificar se é idêntico ao último caso de teste já salvo com sucesso
        campos_tupla = tuple(sorted((k, v) for k, v in campos.items() if v))
        if hasattr(self, "_last_ct_saved") and self._last_ct_saved == campos_tupla:
            self._caso_result.configure(
                text="ℹ️ Este caso de teste já foi salvo com sucesso no banco de dados."
            )
            return

        valido, msg = activities.validar_caso_teste(campos)

        if valido:
            database.salvar_caso_teste(
                campos.get("ct_id", ""), campos.get("titulo", ""),
                campos.get("prioridade", ""), campos.get("pre_condicoes", ""),
                campos.get("dados", ""), campos.get("passos", ""),
                campos.get("resultado_esperado", ""), campos.get("pos_condicoes", ""),
            )
            self._last_ct_saved = campos_tupla
            # Limpar campos para evitar cliques sucessivos que criem duplicados
            for widget in self._ct_fields.values():
                if isinstance(widget, (ttkb.Text, tk.Text)):
                    widget.delete("1.0", "end")
                else:
                    widget.delete(0, "end")

        self._caso_result.configure(text=msg)
        database.registrar_progresso(
            activities.NOMES_ATIVIDADES[8], valido,
            "Caso salvo" if valido else "Campos incompletos",
        )

    def _reset_caso_teste(self):
        self._last_ct_saved = None
        for widget in self._ct_fields.values():
            if isinstance(widget, (ttkb.Text, tk.Text)):
                widget.delete("1.0", "end")
            else:
                widget.delete(0, "end")
        self._caso_result.configure(text="Preencha o formulário e clique em Verificar.")

    # -----------------------------------------------------------------
    # ATIVIDADE 9: GHERKIN
    # -----------------------------------------------------------------

    def _build_act_gherkin(self, parent):
        """Constrói a atividade de Gherkin."""
        card = self._create_card(parent, title="Enunciado")
        ttkb.Label(
            card,
            text=(
                "Escreva um cenário utilizando a sintaxe Gherkin.\n"
                "Os campos Dado, Quando e Então são obrigatórios.\n"
                "Os campos E são opcionais.\n\n"
                f"{activities.GHERKIN_EXEMPLO}"
            ),
            font=FONT_BODY, wraplength=700, justify="left",
        ).pack(fill=X, pady=5)

        resp_card = self._create_card(parent, title="Seu cenário Gherkin")
        labels = ["Dado", "E (contexto adicional)", "Quando", "E (ação adicional)", "Então"]
        hints = [
            "que o usuário está na página de login",
            "possui credenciais válidas (opcional)",
            "informa e-mail e senha",
            "clica em entrar (opcional)",
            "o sistema exibe a página inicial",
        ]
        self._gherkin_fields = []
        for label, hint in zip(labels, hints):
            obr = " *" if label in ("Dado", "Quando", "Então") else ""
            ttkb.Label(resp_card, text=f"{label}{obr}:", font=FONT_BODY_BOLD,
                       ).pack(fill=X, pady=(8, 2))
            entry = ttkb.Entry(resp_card, font=FONT_BODY)
            entry.pack(fill=X, pady=2)
            entry.insert(0, "")
            # Placeholder visual
            ttkb.Label(resp_card, text=f"Ex: {hint}", font=FONT_SMALL,
                       foreground="#999").pack(fill=X)
            self._gherkin_fields.append(entry)

        btn_frame = ttkb.Frame(resp_card)
        btn_frame.pack(fill=X, pady=15)
        ttkb.Button(btn_frame, text="✔ Verificar resposta", bootstyle="success",
                    command=self._check_gherkin, padding=(20, 10)).pack(side=LEFT, padx=5)
        ttkb.Button(btn_frame, text="🔄 Tentar novamente", bootstyle="outline-warning",
                    command=self._reset_gherkin, padding=(20, 10)).pack(side=LEFT, padx=5)

        result_card = self._create_card(parent, title="Resultado")
        self._gherkin_result = ttkb.Label(
            result_card, text="Preencha os campos e clique em Verificar.",
            font=FONT_BODY, wraplength=700, justify="left",
        )
        self._gherkin_result.pack(fill=X, pady=5)

    def _check_gherkin(self):
        dado = self._gherkin_fields[0].get()
        e1 = self._gherkin_fields[1].get()
        quando = self._gherkin_fields[2].get()
        e2 = self._gherkin_fields[3].get()
        entao = self._gherkin_fields[4].get()

        valido, msg, cenario = activities.validar_gherkin(dado, e1, quando, e2, entao)

        texto = msg
        if cenario:
            texto += f"\n\n📋 Seu cenário Gherkin:\n\n{cenario}"
        texto += f"\n\n{'─' * 40}\n{activities.GHERKIN_EXPLICACAO}"

        self._gherkin_result.configure(text=texto)
        database.registrar_progresso(
            activities.NOMES_ATIVIDADES[9], valido,
            "Cenário válido" if valido else "Cenário incompleto",
        )

    def _reset_gherkin(self):
        for field in self._gherkin_fields:
            field.delete(0, "end")
        self._gherkin_result.configure(text="Preencha os campos e clique em Verificar.")

    # -----------------------------------------------------------------
    # ATIVIDADE 10: REGISTRO DE DEFEITO
    # -----------------------------------------------------------------

    def _build_act_defeito(self, parent):
        """Constrói a atividade de Registro de Defeito."""
        card = self._create_card(parent, title="Enunciado")
        ttkb.Label(
            card,
            text=(
                "Registre um defeito completo. Preencha os campos abaixo.\n"
                "Os campos marcados com * são obrigatórios."
            ),
            font=FONT_BODY, wraplength=700, justify="left",
        ).pack(fill=X, pady=5)

        resp_card = self._create_card(parent, title="Formulário de Registro de Defeito")
        self._def_fields = {}

        for campo_id, nome, obrigatorio in activities.DEFEITO_CAMPOS:
            obr = " *" if obrigatorio else ""
            ttkb.Label(resp_card, text=f"{nome}{obr}:", font=FONT_BODY_BOLD,
                       ).pack(fill=X, pady=(8, 2))

            if campo_id in ("severidade",):
                var = tk.StringVar(value="")
                widget = ttkb.Combobox(
                    resp_card, textvariable=var, font=FONT_BODY, width=15,
                    values=activities.SEVERIDADE_OPCOES, state="readonly",
                )
                widget.pack(fill=X, pady=2)
                widget._var = var  # store reference
            elif campo_id in ("prioridade",):
                var = tk.StringVar(value="")
                widget = ttkb.Combobox(
                    resp_card, textvariable=var, font=FONT_BODY, width=15,
                    values=activities.PRIORIDADE_OPCOES, state="readonly",
                )
                widget.pack(fill=X, pady=2)
                widget._var = var
            elif campo_id in ("passos_reproducao", "contexto"):
                widget = ttkb.Text(resp_card, height=3, font=FONT_BODY, wrap="word")
                widget.pack(fill=X, pady=2)
            else:
                widget = ttkb.Entry(resp_card, font=FONT_BODY)
                widget.pack(fill=X, pady=2)
            self._def_fields[campo_id] = widget

        btn_frame = ttkb.Frame(resp_card)
        btn_frame.pack(fill=X, pady=15)
        ttkb.Button(btn_frame, text="✔ Verificar e Salvar", bootstyle="success",
                    command=self._check_defeito, padding=(20, 10)).pack(side=LEFT, padx=5)
        ttkb.Button(btn_frame, text="🔄 Limpar campos", bootstyle="outline-warning",
                    command=self._reset_defeito, padding=(20, 10)).pack(side=LEFT, padx=5)

        result_card = self._create_card(parent, title="Resultado")
        self._def_result = ttkb.Label(
            result_card, text="Preencha o formulário e clique em Verificar.",
            font=FONT_BODY, wraplength=700, justify="left",
        )
        self._def_result.pack(fill=X, pady=5)

        exp_card = self._create_card(parent, title="Sobre Registro de Defeitos")
        ttkb.Label(exp_card, text=activities.DEFEITO_EXPLICACAO, font=FONT_BODY,
                   wraplength=700, justify="left").pack(fill=X, pady=5)

    def _get_def_value(self, campo_id):
        widget = self._def_fields[campo_id]
        if isinstance(widget, ttkb.Combobox):
            return widget.get().strip()
        if isinstance(widget, (ttkb.Text, tk.Text)):
            return widget.get("1.0", "end").strip()
        return widget.get().strip()

    def _check_defeito(self):
        campos = {}
        for campo_id in self._def_fields:
            campos[campo_id] = self._get_def_value(campo_id)

        # Se todos os campos estiverem vazios (ex: clique consecutivo logo após salvar)
        if not any(campos.values()):
            self._def_result.configure(
                text="Preencha os campos obrigatórios para cadastrar um novo defeito."
            )
            return

        # Verificar se é idêntico ao último defeito já salvo com sucesso
        campos_tupla = tuple(sorted((k, v) for k, v in campos.items() if v))
        if hasattr(self, "_last_def_saved") and self._last_def_saved == campos_tupla:
            self._def_result.configure(
                text="ℹ️ Este registro de defeito já foi salvo com sucesso no banco de dados."
            )
            return

        valido, msg = activities.validar_registro_defeito(campos)

        if valido:
            database.salvar_defeito(
                campos.get("titulo", ""), campos.get("contexto", ""),
                campos.get("passos_reproducao", ""), campos.get("resultado_esperado", ""),
                campos.get("resultado_atual", ""), campos.get("evidencia", ""),
                campos.get("ambiente", ""), campos.get("versao", ""),
                campos.get("severidade", ""), campos.get("prioridade", ""),
            )
            self._last_def_saved = campos_tupla
            # Limpar campos para evitar cliques sucessivos que criem duplicados
            for campo_id, widget in self._def_fields.items():
                if isinstance(widget, ttkb.Combobox):
                    widget.set("")
                elif isinstance(widget, (ttkb.Text, tk.Text)):
                    widget.delete("1.0", "end")
                else:
                    widget.delete(0, "end")

        self._def_result.configure(text=msg)
        database.registrar_progresso(
            activities.NOMES_ATIVIDADES[10], valido,
            "Defeito salvo" if valido else "Campos incompletos",
        )

    def _reset_defeito(self):
        self._last_def_saved = None
        for campo_id, widget in self._def_fields.items():
            if isinstance(widget, ttkb.Combobox):
                widget.set("")
            elif isinstance(widget, (ttkb.Text, tk.Text)):
                widget.delete("1.0", "end")
            else:
                widget.delete(0, "end")
        self._def_result.configure(text="Preencha o formulário e clique em Verificar.")

    # =================================================================
    # TELA HISTÓRICO
    # =================================================================

    def _create_screen_historico(self):
        """Cria a tela de histórico com abas."""
        frame = ttkb.Frame(self.content_area)
        self.screens["historico"] = frame

        ttkb.Label(frame, text="📋 Histórico", font=FONT_TITLE,
                   anchor="w").pack(fill=X, padx=PAD_X, pady=(20, 10))

        # Notebook com abas
        self.hist_notebook = ttkb.Notebook(frame, bootstyle="primary")
        self.hist_notebook.pack(fill=BOTH, expand=True, padx=PAD_X, pady=(0, 10))

        # Aba Avaliações
        self.hist_aval_frame = ttkb.Frame(self.hist_notebook)
        self.hist_notebook.add(self.hist_aval_frame, text="  ⭐ Avaliações  ")
        self._build_hist_avaliacoes()

        # Aba Casos de Teste
        self.hist_ct_frame = ttkb.Frame(self.hist_notebook)
        self.hist_notebook.add(self.hist_ct_frame, text="  📄 Casos de Teste  ")
        self._build_hist_casos()

        # Aba Defeitos
        self.hist_def_frame = ttkb.Frame(self.hist_notebook)
        self.hist_notebook.add(self.hist_def_frame, text="  🐛 Defeitos  ")
        self._build_hist_defeitos()

        # Rodapé
        self._add_footer(frame)

    def _build_hist_avaliacoes(self):
        """Constrói a aba de avaliações."""
        frame = self.hist_aval_frame

        # Botões
        btn_frame = ttkb.Frame(frame)
        btn_frame.pack(fill=X, padx=10, pady=10)
        ttkb.Button(btn_frame, text="🔄 Atualizar", bootstyle="info",
                    command=self._refresh_hist_aval, padding=(15, 8),
                    ).pack(side=LEFT, padx=5)
        ttkb.Button(btn_frame, text="👁️ Visualizar Detalhes", bootstyle="secondary",
                    command=lambda: self._show_aval_detail(None), padding=(15, 8),
                    ).pack(side=LEFT, padx=5)
        ttkb.Button(btn_frame, text="🗑️ Excluir selecionado", bootstyle="danger",
                    command=self._delete_hist_aval, padding=(15, 8),
                    ).pack(side=LEFT, padx=5)

        # Tabela
        cols = ("id", "data", "modulo", "pergunta", "avaliacao", "observacao")
        self.hist_aval_tree = ttkb.Treeview(
            frame, columns=cols, show="headings", height=12,
        )
        for col, heading, width in [
            ("id", "ID", 40), ("data", "Data", 130),
            ("modulo", "Módulo", 150), ("pergunta", "Pergunta", 300),
            ("avaliacao", "⭐", 50), ("observacao", "Observação", 200),
        ]:
            self.hist_aval_tree.heading(col, text=heading)
            self.hist_aval_tree.column(col, width=width, minwidth=40)

        scroll = ttkb.Scrollbar(frame, orient="vertical",
                                command=self.hist_aval_tree.yview)
        self.hist_aval_tree.configure(yscrollcommand=scroll.set)
        self.hist_aval_tree.pack(side=LEFT, fill=BOTH, expand=True, padx=(10, 0), pady=(0, 10))
        scroll.pack(side=LEFT, fill=Y, padx=(0, 10), pady=(0, 10))

        # Detalhes com duplo clique
        self.hist_aval_tree.bind("<Double-1>", self._show_aval_detail)

    def _refresh_hist_aval(self):
        """Atualiza a tabela de avaliações."""
        for item in self.hist_aval_tree.get_children():
            self.hist_aval_tree.delete(item)
        for row in database.listar_avaliacoes():
            pergunta_short = row["pergunta"][:60] + "..." if len(row["pergunta"]) > 60 else row["pergunta"]
            obs_short = (row["observacao"] or "")[:40]
            self.hist_aval_tree.insert("", "end", values=(
                row["id"], row["data_hora"], row["modulo"],
                pergunta_short, "★" * row["avaliacao"], obs_short,
            ))

    def _show_aval_detail(self, event=None):
        """Mostra detalhes da avaliação selecionada."""
        sel = self.hist_aval_tree.selection()
        if not sel:
            if event is None:
                messagebox.showwarning("Atenção", "Selecione um registro para visualizar.")
            return
        item = self.hist_aval_tree.item(sel[0])
        aval_id = item["values"][0]
        registro = database.buscar_avaliacao(aval_id)
        if not registro:
            return

        # Mostrar em pop-up
        detail_text = (
            f"📅 Data: {registro['data_hora']}\n"
            f"📚 Módulo: {registro['modulo']}\n"
            f"❓ Pergunta: {registro['pergunta']}\n\n"
            f"💬 Resposta:\n{registro['resposta']}\n\n"
            f"⭐ Avaliação: {'★' * registro['avaliacao']}\n"
            f"📝 Observação: {registro['observacao'] or '(nenhuma)'}"
        )
        self._show_detail_popup("Detalhes da Avaliação", detail_text)

    def _delete_hist_aval(self):
        """Exclui a avaliação selecionada."""
        sel = self.hist_aval_tree.selection()
        if not sel:
            messagebox.showwarning("Atenção", "Selecione um registro para excluir.")
            return
        item = self.hist_aval_tree.item(sel[0])
        aval_id = item["values"][0]
        if messagebox.askyesno("Confirmar exclusão",
                               f"Deseja realmente excluir o registro #{aval_id}?"):
            database.excluir_avaliacao(aval_id)
            self._refresh_hist_aval()
            messagebox.showinfo("Sucesso", "Registro excluído com sucesso.")

    def _build_hist_casos(self):
        """Constrói a aba de casos de teste."""
        frame = self.hist_ct_frame
        btn_frame = ttkb.Frame(frame)
        btn_frame.pack(fill=X, padx=10, pady=10)
        ttkb.Button(btn_frame, text="🔄 Atualizar", bootstyle="info",
                    command=self._refresh_hist_casos, padding=(15, 8)).pack(side=LEFT, padx=5)
        ttkb.Button(btn_frame, text="👁️ Visualizar Detalhes", bootstyle="secondary",
                    command=lambda: self._show_caso_detail(None), padding=(15, 8)).pack(side=LEFT, padx=5)
        ttkb.Button(btn_frame, text="🗑️ Excluir selecionado", bootstyle="danger",
                    command=self._delete_hist_caso, padding=(15, 8)).pack(side=LEFT, padx=5)

        cols = ("id", "data", "ct_id", "titulo", "prioridade")
        self.hist_ct_tree = ttkb.Treeview(frame, columns=cols, show="headings", height=12)
        for col, heading, width in [
            ("id", "ID", 40), ("data", "Data", 130), ("ct_id", "CT ID", 80),
            ("titulo", "Título", 350), ("prioridade", "Prioridade", 100),
        ]:
            self.hist_ct_tree.heading(col, text=heading)
            self.hist_ct_tree.column(col, width=width, minwidth=40)

        scroll = ttkb.Scrollbar(frame, orient="vertical",
                                command=self.hist_ct_tree.yview)
        self.hist_ct_tree.configure(yscrollcommand=scroll.set)
        self.hist_ct_tree.pack(side=LEFT, fill=BOTH, expand=True, padx=(10, 0), pady=(0, 10))
        scroll.pack(side=LEFT, fill=Y, padx=(0, 10), pady=(0, 10))
        self.hist_ct_tree.bind("<Double-1>", self._show_caso_detail)

    def _refresh_hist_casos(self):
        for item in self.hist_ct_tree.get_children():
            self.hist_ct_tree.delete(item)
        for row in database.listar_casos_teste():
            self.hist_ct_tree.insert("", "end", values=(
                row["id"], row["data_hora"], row["ct_id"],
                row["titulo"][:60], row["prioridade"] or "",
            ))

    def _show_caso_detail(self, event=None):
        sel = self.hist_ct_tree.selection()
        if not sel:
            if event is None:
                messagebox.showwarning("Atenção", "Selecione um caso de teste para visualizar.")
            return
        item = self.hist_ct_tree.item(sel[0])
        caso_id = item["values"][0]
        reg = database.buscar_caso_teste(caso_id)
        if not reg:
            return
        text = (
            f"📅 Data: {reg['data_hora']}\n"
            f"🆔 CT ID: {reg['ct_id']}\n"
            f"📌 Título: {reg['titulo']}\n"
            f"⚡ Prioridade: {reg['prioridade'] or '—'}\n\n"
            f"📋 Pré-condições:\n{reg['pre_condicoes'] or '—'}\n\n"
            f"📊 Dados: {reg['dados'] or '—'}\n\n"
            f"👣 Passos:\n{reg['passos']}\n\n"
            f"✅ Resultado Esperado:\n{reg['resultado_esperado']}\n\n"
            f"📋 Pós-condições: {reg['pos_condicoes'] or '—'}"
        )
        self._show_detail_popup("Detalhes do Caso de Teste", text)

    def _delete_hist_caso(self):
        sel = self.hist_ct_tree.selection()
        if not sel:
            messagebox.showwarning("Atenção", "Selecione um registro para excluir.")
            return
        item = self.hist_ct_tree.item(sel[0])
        caso_id = item["values"][0]
        if messagebox.askyesno("Confirmar exclusão",
                               f"Deseja realmente excluir o caso de teste #{caso_id}?"):
            database.excluir_caso_teste(caso_id)
            self._refresh_hist_casos()
            messagebox.showinfo("Sucesso", "Caso de teste excluído com sucesso.")

    def _build_hist_defeitos(self):
        """Constrói a aba de defeitos."""
        frame = self.hist_def_frame
        btn_frame = ttkb.Frame(frame)
        btn_frame.pack(fill=X, padx=10, pady=10)
        ttkb.Button(btn_frame, text="🔄 Atualizar", bootstyle="info",
                    command=self._refresh_hist_defeitos, padding=(15, 8)).pack(side=LEFT, padx=5)
        ttkb.Button(btn_frame, text="👁️ Visualizar Detalhes", bootstyle="secondary",
                    command=lambda: self._show_defeito_detail(None), padding=(15, 8)).pack(side=LEFT, padx=5)
        ttkb.Button(btn_frame, text="🗑️ Excluir selecionado", bootstyle="danger",
                    command=self._delete_hist_defeito, padding=(15, 8)).pack(side=LEFT, padx=5)

        cols = ("id", "data", "titulo", "severidade", "prioridade")
        self.hist_def_tree = ttkb.Treeview(frame, columns=cols, show="headings", height=12)
        for col, heading, width in [
            ("id", "ID", 40), ("data", "Data", 130), ("titulo", "Título", 350),
            ("severidade", "Severidade", 100), ("prioridade", "Prioridade", 100),
        ]:
            self.hist_def_tree.heading(col, text=heading)
            self.hist_def_tree.column(col, width=width, minwidth=40)

        scroll = ttkb.Scrollbar(frame, orient="vertical",
                                command=self.hist_def_tree.yview)
        self.hist_def_tree.configure(yscrollcommand=scroll.set)
        self.hist_def_tree.pack(side=LEFT, fill=BOTH, expand=True, padx=(10, 0), pady=(0, 10))
        scroll.pack(side=LEFT, fill=Y, padx=(0, 10), pady=(0, 10))
        self.hist_def_tree.bind("<Double-1>", self._show_defeito_detail)

    def _refresh_hist_defeitos(self):
        for item in self.hist_def_tree.get_children():
            self.hist_def_tree.delete(item)
        for row in database.listar_defeitos():
            self.hist_def_tree.insert("", "end", values=(
                row["id"], row["data_hora"], row["titulo"][:60],
                row["severidade"] or "", row["prioridade"] or "",
            ))

    def _show_defeito_detail(self, event=None):
        sel = self.hist_def_tree.selection()
        if not sel:
            if event is None:
                messagebox.showwarning("Atenção", "Selecione um defeito para visualizar.")
            return
        item = self.hist_def_tree.item(sel[0])
        def_id = item["values"][0]
        reg = database.buscar_defeito(def_id)
        if not reg:
            return
        text = (
            f"📅 Data: {reg['data_hora']}\n"
            f"📌 Título: {reg['titulo']}\n"
            f"📝 Contexto: {reg['contexto'] or '—'}\n\n"
            f"👣 Passos para Reprodução:\n{reg['passos_reproducao']}\n\n"
            f"✅ Resultado Esperado:\n{reg['resultado_esperado']}\n\n"
            f"❌ Resultado Atual:\n{reg['resultado_atual']}\n\n"
            f"📷 Evidência: {reg['evidencia'] or '—'}\n"
            f"💻 Ambiente: {reg['ambiente'] or '—'}\n"
            f"🔢 Versão: {reg['versao'] or '—'}\n"
            f"⚠️ Severidade: {reg['severidade'] or '—'}\n"
            f"🔺 Prioridade: {reg['prioridade'] or '—'}"
        )
        self._show_detail_popup("Detalhes do Defeito", text)

    def _delete_hist_defeito(self):
        sel = self.hist_def_tree.selection()
        if not sel:
            messagebox.showwarning("Atenção", "Selecione um registro para excluir.")
            return
        item = self.hist_def_tree.item(sel[0])
        def_id = item["values"][0]
        if messagebox.askyesno("Confirmar exclusão",
                               f"Deseja realmente excluir o defeito #{def_id}?"):
            database.excluir_defeito(def_id)
            self._refresh_hist_defeitos()
            messagebox.showinfo("Sucesso", "Defeito excluído com sucesso.")

    def _show_detail_popup(self, title, text):
        """Mostra detalhes em uma janela pop-up."""
        popup = ttkb.Toplevel(self.window)
        popup.title(title)
        popup.geometry("650x500")
        popup.resizable(True, True)

        txt = ttkb.Text(popup, font=FONT_BODY, wrap="word", padx=15, pady=15)
        txt.insert("1.0", text)
        txt.configure(state="disabled")
        txt.pack(fill=BOTH, expand=True)

        ttkb.Button(
            popup, text="Fechar", bootstyle="secondary",
            command=popup.destroy, padding=(20, 10),
        ).pack(pady=10)

    def _refresh_historico(self):
        """Atualiza todas as abas do histórico."""
        self._refresh_hist_aval()
        self._refresh_hist_casos()
        self._refresh_hist_defeitos()

    # =================================================================
    # TELA PROGRESSO
    # =================================================================

    def _create_screen_progresso(self):
        """Cria a tela de progresso."""
        frame = ScrolledFrame(self.content_area, autohide=True)
        self.screens["progresso"] = frame
        inner = frame

        ttkb.Label(inner, text="📊 Progresso das Atividades", font=FONT_TITLE,
                   anchor="w").pack(fill=X, padx=PAD_X, pady=(20, 10))

        # Resumo geral
        self.prog_summary_card = self._create_card(inner, title="Resumo Geral")
        self.prog_summary_label = ttkb.Label(
            self.prog_summary_card, text="Carregando...", font=FONT_BODY,
            wraplength=700, justify="left",
        )
        self.prog_summary_label.pack(fill=X, pady=5)

        # Tabela detalhada
        detail_card = self._create_card(inner, title="Detalhes por Atividade")
        cols = ("atividade", "total", "acertos", "erros", "taxa")
        self.prog_tree = ttkb.Treeview(detail_card, columns=cols,
                                       show="headings", height=12)
        for col, heading, width in [
            ("atividade", "Atividade", 350), ("total", "Total", 80),
            ("acertos", "Acertos", 80), ("erros", "Erros", 80),
            ("taxa", "Taxa de Acerto", 120),
        ]:
            self.prog_tree.heading(col, text=heading)
            self.prog_tree.column(col, width=width, minwidth=60)
        self.prog_tree.pack(fill=BOTH, expand=True, pady=5)

        # Botões
        btn_frame = ttkb.Frame(inner)
        btn_frame.pack(fill=X, padx=PAD_X, pady=10)
        ttkb.Button(btn_frame, text="🔄 Atualizar", bootstyle="info",
                    command=self._refresh_progresso, padding=(15, 8),
                    ).pack(side=LEFT, padx=5)
        ttkb.Button(btn_frame, text="🗑️ Limpar progresso", bootstyle="danger-outline",
                    command=self._clear_progresso, padding=(15, 8),
                    ).pack(side=LEFT, padx=5)

        # Histórico detalhado
        hist_card = self._create_card(inner, title="Histórico de Tentativas")
        cols2 = ("data", "atividade", "resultado", "detalhes")
        self.prog_hist_tree = ttkb.Treeview(hist_card, columns=cols2,
                                            show="headings", height=8)
        for col, heading, width in [
            ("data", "Data/Hora", 150), ("atividade", "Atividade", 300),
            ("resultado", "Resultado", 100), ("detalhes", "Detalhes", 200),
        ]:
            self.prog_hist_tree.heading(col, text=heading)
            self.prog_hist_tree.column(col, width=width, minwidth=60)
        self.prog_hist_tree.pack(fill=BOTH, expand=True, pady=5)

        self._add_watermark(inner)

    def _refresh_progresso(self):
        """Atualiza os dados de progresso."""
        # Limpar tabelas
        for item in self.prog_tree.get_children():
            self.prog_tree.delete(item)
        for item in self.prog_hist_tree.get_children():
            self.prog_hist_tree.delete(item)

        # Estatísticas por atividade
        stats = database.obter_estatisticas_progresso()
        total_geral = 0
        acertos_geral = 0

        for stat in stats:
            total = stat["total"]
            acertos = stat["acertos"] or 0
            erros = total - acertos
            taxa = f"{(acertos/total*100):.0f}%" if total > 0 else "—"
            total_geral += total
            acertos_geral += acertos
            self.prog_tree.insert("", "end", values=(
                stat["atividade"], total, acertos, erros, taxa,
            ))

        # Resumo
        if total_geral > 0:
            taxa_geral = f"{(acertos_geral/total_geral*100):.0f}%"
            self.prog_summary_label.configure(
                text=(
                    f"📊 Total de tentativas: {total_geral}\n"
                    f"✅ Acertos: {acertos_geral}\n"
                    f"❌ Erros: {total_geral - acertos_geral}\n"
                    f"📈 Taxa de acerto geral: {taxa_geral}\n"
                    f"📝 Atividades praticadas: {len(stats)} de 10"
                ),
            )
        else:
            self.prog_summary_label.configure(
                text=(
                    "Nenhuma atividade realizada ainda.\n\n"
                    "Acesse 📝 Atividades de Testes para começar a praticar!"
                ),
            )

        # Histórico detalhado
        for row in database.listar_progresso():
            resultado = "✅ Acerto" if row["acertou"] else "❌ Erro"
            self.prog_hist_tree.insert("", "end", values=(
                row["data_hora"], row["atividade"],
                resultado, row["detalhes"] or "",
            ))

    def _clear_progresso(self):
        """Limpa todo o progresso."""
        if messagebox.askyesno(
            "Confirmar limpeza",
            "Deseja realmente limpar todo o progresso?\nEssa ação não pode ser desfeita.",
        ):
            database.limpar_progresso()
            self._refresh_progresso()
            messagebox.showinfo("Sucesso", "Progresso limpo com sucesso.")

    # =================================================================
    # TELA SOBRE
    # =================================================================

    def _create_screen_sobre(self):
        """Cria a tela Sobre."""
        frame = ScrolledFrame(self.content_area, autohide=True)
        self.screens["sobre"] = frame
        inner = frame

        ttkb.Label(inner, text="ℹ️ Sobre", font=FONT_TITLE,
                   anchor="w").pack(fill=X, padx=PAD_X, pady=(20, 10))

        card = self._create_card(inner, title="Assistente de Estudos — Mentoria 2.0")

        info = [
            ("Aplicativo", "Assistente de Estudos — Mentoria 2.0"),
            ("Versão", "1.0.0"),
            ("Objetivo", "Apoiar estudos de Testes de Software"),
            ("Conteúdo", "Módulos 1 e 2 da Mentoria"),
            ("Tecnologias", "Python, ttkbootstrap, SQLite"),
            ("Plataforma", "Windows 11"),
        ]
        for label, value in info:
            row = ttkb.Frame(card)
            row.pack(fill=X, pady=3)
            ttkb.Label(row, text=f"{label}:", font=FONT_BODY_BOLD, width=15,
                       anchor="w").pack(side=LEFT)
            ttkb.Label(row, text=value, font=FONT_BODY).pack(side=LEFT)

        ttkb.Separator(card).pack(fill=X, pady=15)

        ttkb.Label(
            card, text="MENTORIA 2.0 — por Júlio de Lima",
            font=("Segoe UI", 16, "bold"), bootstyle="primary", anchor="center",
        ).pack(fill=X, pady=10)

        ttkb.Label(
            card, text="Desenvolvido por Adalton",
            font=("Segoe UI", 14), anchor="center",
        ).pack(fill=X, pady=5)

        ttkb.Separator(card).pack(fill=X, pady=15)

        ttkb.Label(
            card,
            text=(
                "Este aplicativo foi criado como parte da Mentoria 2.0 de Testes de Software.\n"
                "Todas as respostas e atividades são baseadas exclusivamente nos conteúdos\n"
                "dos Módulos 1 e 2 fornecidos para o projeto.\n\n"
                "O aplicativo funciona localmente, sem necessidade de internet,\n"
                "servidores ou APIs pagas."
            ),
            font=FONT_BODY, wraplength=700, justify="center", anchor="center",
        ).pack(fill=X, pady=10)

        self._add_watermark(inner)

    # =================================================================
    # EXECUTAR APLICATIVO
    # =================================================================

    def run(self):
        """Inicia o loop principal do aplicativo."""
        self.window.mainloop()

