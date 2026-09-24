"""
Atividades práticas de Testes de Software — Mentoria 2.0
Contém cenários, regras de validação e explicações para as 10 atividades.
Todas as regras são fundamentadas nos Módulos 1 e 2.
Desenvolvido por Adalton.
"""


# =====================================================================
# NOMES DAS ATIVIDADES
# =====================================================================

NOMES_ATIVIDADES = {
    1: "Valor Limite — Análise de Valor de Fronteira",
    2: "Particionamento de Equivalência",
    3: "Tabela de Decisão",
    4: "Checking × Testing",
    5: "Ad hoc × Exploratório",
    6: "Test Charter / SBTM",
    7: "Severidade × Prioridade",
    8: "Caso de Teste",
    9: "Gherkin",
    10: "Registro de Defeito",
}


# =====================================================================
# 1. VALOR LIMITE — ANÁLISE DE VALOR DE FRONTEIRA
# =====================================================================

VALOR_LIMITE_REGRA = "Valor mínimo permitido para transferência: R$ 10,00"

VALOR_LIMITE_CENARIOS = [
    {
        "valor": 9.99,
        "label": "R$ 9,99",
        "resposta_correta": "Abaixo do limite",
        "explicacao": (
            "R$ 9,99 está abaixo do valor mínimo de R$ 10,00. "
            "Este é um cenário INVÁLIDO — a transferência não deve ser permitida. "
            "Testar valores logo abaixo do limite ajuda a verificar se o sistema "
            "rejeita corretamente entradas fora da fronteira."
        ),
    },
    {
        "valor": 10.00,
        "label": "R$ 10,00",
        "resposta_correta": "No limite",
        "explicacao": (
            "R$ 10,00 está exatamente no valor mínimo permitido. "
            "Este é um cenário VÁLIDO — a transferência deve ser aceita. "
            "Testar o valor exato do limite é essencial para verificar "
            "se a regra de fronteira foi implementada corretamente."
        ),
    },
    {
        "valor": 10.01,
        "label": "R$ 10,01",
        "resposta_correta": "Acima do limite",
        "explicacao": (
            "R$ 10,01 está acima do valor mínimo de R$ 10,00. "
            "Este é um cenário VÁLIDO — a transferência deve ser aceita. "
            "Testar valores logo acima do limite confirma que o sistema "
            "aceita valores válidos próximos à fronteira."
        ),
    },
]

VALOR_LIMITE_OPCOES = ["Abaixo do limite", "No limite", "Acima do limite"]

VALOR_LIMITE_EXPLICACAO_GERAL = (
    "A Análise do Valor Limite concentra os testes nas fronteiras de uma regra. "
    "Defeitos frequentemente ocorrem nos limites das condições. "
    "Ao testar R$ 9,99, R$ 10,00 e R$ 10,01, verificamos como o sistema "
    "se comporta exatamente na fronteira da regra de valor mínimo.\n\n"
    "Fonte: Módulo 2, item 10 — Análise do valor limite."
)


# =====================================================================
# 2. PARTICIONAMENTO DE EQUIVALÊNCIA
# =====================================================================

PARTICAO_REGRA = "Transferências a partir de R$ 10,00 são permitidas."

PARTICAO_CLASSES = {
    "invalida": {
        "nome": "Classe Inválida",
        "descricao": "Valores menores que R$ 10,00",
        "condicao": lambda v: v < 10.00,
    },
    "valida": {
        "nome": "Classe Válida",
        "descricao": "Valores iguais ou maiores que R$ 10,00",
        "condicao": lambda v: v >= 10.00,
    },
}

PARTICAO_EXPLICACAO = (
    "Partição de Equivalência divide entradas em grupos (classes) que "
    "apresentam comportamento semelhante. Em vez de testar todos os valores "
    "possíveis, seleciona-se um representante de cada classe.\n\n"
    "Neste exercício:\n"
    "• Classe Inválida: valores menores que R$ 10,00 (ex: R$ 5,00, R$ 0,01)\n"
    "• Classe Válida: valores iguais ou maiores que R$ 10,00 (ex: R$ 10,00, R$ 50,00)\n\n"
    "Fonte: Módulo 2, item 9 — Partição de equivalência."
)


def verificar_particao(valor_texto):
    """
    Verifica em qual classe de equivalência o valor se encaixa.

    Returns:
        (classe, explicacao) ou (None, mensagem_erro)
    """
    try:
        valor_texto = valor_texto.replace("R$", "").replace(",", ".").strip()
        valor = float(valor_texto)
    except (ValueError, AttributeError):
        return None, "Valor inválido. Informe um número, ex: 15.00"

    if valor < 0:
        return None, "Informe um valor positivo."

    if PARTICAO_CLASSES["invalida"]["condicao"](valor):
        return (
            "invalida",
            f"R$ {valor:.2f} pertence à CLASSE INVÁLIDA (valores menores que R$ 10,00).\n"
            f"A transferência NÃO deve ser permitida.",
        )
    else:
        return (
            "valida",
            f"R$ {valor:.2f} pertence à CLASSE VÁLIDA (valores iguais ou maiores que R$ 10,00).\n"
            f"A transferência DEVE ser permitida.",
        )


# =====================================================================
# 3. TABELA DE DECISÃO
# =====================================================================

TABELA_DECISAO_OPCOES = [
    "Aprovada",
    "Rejeitada",
    "Aprovada (confirmação adicional)",
]

TABELA_DECISAO_CONDICOES = {
    "valor": ["Menor que R$ 5.000", "Maior ou igual a R$ 5.000"],
    "token": ["Válido", "Inválido", "Não informado"],
}

TABELA_DECISAO_COMBINACOES = [
    {"valor": "Menor que R$ 5.000", "token": "Válido",
     "opcao_esperada": "Aprovada",
     "resultado": "Transferência aprovada"},
    {"valor": "Menor que R$ 5.000", "token": "Inválido",
     "opcao_esperada": "Rejeitada",
     "resultado": "Transferência rejeitada — token inválido"},
    {"valor": "Menor que R$ 5.000", "token": "Não informado",
     "opcao_esperada": "Rejeitada",
     "resultado": "Transferência rejeitada — token não informado"},
    {"valor": "Maior ou igual a R$ 5.000", "token": "Válido",
     "opcao_esperada": "Aprovada (confirmação adicional)",
     "resultado": "Transferência aprovada (pode exigir confirmação adicional)"},
    {"valor": "Maior ou igual a R$ 5.000", "token": "Inválido",
     "opcao_esperada": "Rejeitada",
     "resultado": "Transferência rejeitada — token inválido"},
    {"valor": "Maior ou igual a R$ 5.000", "token": "Não informado",
     "opcao_esperada": "Rejeitada",
     "resultado": "Transferência rejeitada — token não informado"},
]

TABELA_DECISAO_EXPLICACAO = (
    "A Tabela de Decisão combina diferentes condições e resultados para "
    "gerar cenários de teste. Neste exercício, combinamos 2 condições de "
    "valor (< R$ 5.000 e ≥ R$ 5.000) com 3 estados de token (válido, "
    "inválido, não informado), gerando 6 combinações possíveis.\n\n"
    "Essa técnica é útil quando há múltiplas condições que interagem "
    "entre si e precisam ser testadas em combinação.\n\n"
    "Fonte: Módulo 2, item 11 — Tabela de decisão."
)


def validar_cenario_tabela_decisao(cenario, resposta):
    """
    Valida a resposta para um cenário da tabela de decisão.
    Exige correspondência estrita com a opção esperada para evitar falsos positivos
    (por exemplo, 'Aprovada' NÃO é aceito quando a resposta esperada exige
    'Aprovada (confirmação adicional)').

    Args:
        cenario: dict do cenário de TABELA_DECISAO_COMBINACOES
        resposta: str com a opção selecionada pelo usuário

    Returns:
        (correto: bool, opcao_esperada: str, resultado_completo: str)
    """
    opcao_esperada = cenario.get("opcao_esperada", cenario["resultado"])
    resultado_completo = cenario["resultado"]
    # Validação exata e estrita (sem substring in para evitar falsos positivos)
    resp_limpa = str(resposta).strip()
    correto = (resp_limpa == opcao_esperada.strip())
    return correto, opcao_esperada, resultado_completo


# =====================================================================
# 4. CHECKING × TESTING
# =====================================================================

CENARIOS_CHECKING_TESTING = [
    {
        "descricao": (
            "Verificar se o botão 'Entrar' exibe a cor azul (#0066CC) "
            "conforme especificado no layout aprovado."
        ),
        "resposta_correta": "Checking",
        "justificativa": (
            "Trata-se de CHECKING porque estamos verificando uma expectativa "
            "conhecida e objetiva — a cor do botão conforme a especificação. "
            "É uma conferência de resultado pré-definido."
        ),
    },
    {
        "descricao": (
            "Explorar o formulário de cadastro informando dados inesperados "
            "(caracteres especiais, campos vazios, valores extremos) para "
            "observar como o sistema reage."
        ),
        "resposta_correta": "Testing",
        "justificativa": (
            "Trata-se de TESTING porque envolve investigação, hipóteses e "
            "observação. O objetivo é descobrir comportamentos inesperados, "
            "não apenas confirmar uma especificação."
        ),
    },
    {
        "descricao": (
            "Confirmar que o campo de e-mail aceita o formato usuario@dominio.com "
            "conforme a regra documentada no requisito REQ-042."
        ),
        "resposta_correta": "Checking",
        "justificativa": (
            "Trata-se de CHECKING porque estamos conferindo se o sistema "
            "aceita um formato previamente definido no requisito. "
            "A expectativa é conhecida e objetiva."
        ),
    },
    {
        "descricao": (
            "Navegar por diferentes fluxos do aplicativo tentando entender "
            "como ele se comporta quando a conexão de internet é interrompida "
            "durante uma operação."
        ),
        "resposta_correta": "Testing",
        "justificativa": (
            "Trata-se de TESTING porque envolve exploração e investigação "
            "de comportamentos em situações não triviais. O testador busca "
            "aprender e descobrir informações sobre o sistema."
        ),
    },
    {
        "descricao": (
            "Executar o caso de teste CT-015 que verifica se o saldo é "
            "atualizado corretamente após uma transferência de R$ 100,00."
        ),
        "resposta_correta": "Checking",
        "justificativa": (
            "Trata-se de CHECKING porque estamos seguindo um caso de teste "
            "pré-definido com resultado esperado conhecido. A verificação "
            "é objetiva e reproduzível."
        ),
    },
]


# =====================================================================
# 5. AD HOC × EXPLORATÓRIO
# =====================================================================

CENARIOS_ADHOC_EXPLORATORIO = [
    {
        "descricao": (
            "Um testador recebe uma nova funcionalidade e começa a clicar "
            "em diferentes partes da tela, sem planejamento prévio, apenas "
            "para ter uma ideia geral do que mudou."
        ),
        "resposta_correta": "Ad hoc",
        "justificativa": (
            "Trata-se de teste AD HOC porque não há roteiro, planejamento "
            "ou estrutura definida. O testador está explorando de forma "
            "informal e rápida, sem registro sistemático."
        ),
    },
    {
        "descricao": (
            "O testador define uma sessão de 45 minutos com a missão: "
            "'Explorar o módulo de pagamento com dados inválidos para "
            "descobrir como o sistema trata erros.' Ao final, documenta "
            "o que encontrou."
        ),
        "resposta_correta": "SBTM",
        "justificativa": (
            "Trata-se de SBTM (Session-Based Test Management) porque "
            "há uma sessão com tempo definido, um charter (missão) "
            "estruturado e documentação dos resultados ao final."
        ),
    },
    {
        "descricao": (
            "O testador está aprendendo sobre o fluxo de cadastro enquanto "
            "testa. A cada descoberta, adapta seus testes para investigar "
            "comportamentos relacionados."
        ),
        "resposta_correta": "Exploratório",
        "justificativa": (
            "Trata-se de teste EXPLORATÓRIO porque combina aprendizagem, "
            "desenho do teste e execução simultaneamente. O testador "
            "adapta sua abordagem conforme descobre informações."
        ),
    },
    {
        "descricao": (
            "Após uma reunião, o testador rapidamente acessa o sistema "
            "em produção para verificar se um problema relatado por um "
            "cliente realmente acontece, sem documentar os passos."
        ),
        "resposta_correta": "Ad hoc",
        "justificativa": (
            "Trata-se de teste AD HOC porque é uma verificação rápida, "
            "sem roteiro formal e sem documentação estruturada. "
            "O objetivo é uma conferência pontual e imediata."
        ),
    },
]


# =====================================================================
# 6. TEST CHARTER / SBTM
# =====================================================================

CHARTER_MODELO = 'Explorar [alvo] com [recursos/técnicas] para descobrir [informação].'

CHARTER_EXPLICACAO = (
    "O Test Charter é a missão que guia uma sessão de teste exploratório. "
    "Ele deve conter três elementos essenciais:\n\n"
    "1. ALVO — O que será explorado (funcionalidade, módulo, tela)\n"
    "2. RECURSOS/TÉCNICAS — Como será explorado (dados, ferramentas, heurísticas)\n"
    "3. INFORMAÇÃO — O que se deseja descobrir (comportamentos, riscos, problemas)\n\n"
    "Um charter bem definido garante que a exploração tenha foco e propósito, "
    "mantendo a liberdade do teste exploratório com estrutura do SBTM.\n\n"
    "Fonte: Módulo 2, itens 7 e 8 — SBTM e Test Charter."
)


def validar_test_charter(alvo, recursos, informacao):
    """
    Valida se os três elementos do Test Charter foram preenchidos.

    Returns:
        (valido, mensagem, charter_formatado)
    """
    alvo = alvo.strip() if alvo else ""
    recursos = recursos.strip() if recursos else ""
    informacao = informacao.strip() if informacao else ""

    erros = []
    if len(alvo) < 3:
        erros.append("• O ALVO (o que será explorado) precisa ser preenchido.")
    if len(recursos) < 3:
        erros.append("• Os RECURSOS/TÉCNICAS precisam ser preenchidos.")
    if len(informacao) < 3:
        erros.append("• A INFORMAÇÃO desejada precisa ser preenchida.")

    if erros:
        return False, "O Test Charter está incompleto:\n\n" + "\n".join(erros), ""

    charter = f"Explorar {alvo} com {recursos} para descobrir {informacao}."
    return (
        True,
        "✅ Test Charter válido! Todos os elementos foram preenchidos.\n\n"
        "O charter contém:\n"
        f"• Alvo: {alvo}\n"
        f"• Recursos/Técnicas: {recursos}\n"
        f"• Informação desejada: {informacao}",
        charter,
    )


# =====================================================================
# 7. SEVERIDADE × PRIORIDADE
# =====================================================================

SEVERIDADE_OPCOES = ["Baixa", "Média", "Alta", "Crítica"]
PRIORIDADE_OPCOES = ["Baixa", "Média", "Alta", "Urgente"]

CENARIOS_SEVERIDADE_PRIORIDADE = [
    {
        "descricao": (
            "O sistema de login não funciona. Nenhum usuário consegue "
            "acessar a plataforma."
        ),
        "severidades_aceitaveis": ["Crítica", "Alta"],
        "prioridades_aceitaveis": ["Urgente", "Alta"],
        "severidade_sugerida": "Crítica",
        "prioridade_sugerida": "Urgente",
        "explicacao": (
            "A severidade é CRÍTICA (ou Alta) porque o impacto é total (sistema inoperante para os usuários). "
            "A prioridade é URGENTE (ou Alta), pois restabelecer o acesso ao sistema exige tratamento imediato "
            "da equipe técnica para evitar paradas operacionais."
        ),
    },
    {
        "descricao": (
            "Há um erro de ortografia na palavra 'Benvindo' exibida "
            "na tela inicial (deveria ser 'Bem-vindo')."
        ),
        "severidades_aceitaveis": ["Baixa"],
        "prioridades_aceitaveis": ["Baixa", "Média"],
        "severidade_sugerida": "Baixa",
        "prioridade_sugerida": "Baixa",
        "explicacao": (
            "A severidade é BAIXA porque o erro não afeta o funcionamento funcional do sistema. "
            "A prioridade pode ser classificada como BAIXA (corrigir em versão futura) ou MÉDIA "
            "(caso a empresa considere a imagem institucional na tela inicial de alto valor de marca). "
            "Ambos os pontos de vista são contextualmente coerentes."
        ),
    },
    {
        "descricao": (
            "O botão 'Finalizar Compra' não funciona na versão mobile. "
            "Na versão desktop, funciona normalmente."
        ),
        "severidades_aceitaveis": ["Alta", "Crítica"],
        "prioridades_aceitaveis": ["Alta", "Urgente"],
        "severidade_sugerida": "Alta",
        "prioridade_sugerida": "Alta",
        "explicacao": (
            "A severidade é ALTA (ou CRÍTICA) porque impede completamente as vendas pelo canal mobile. "
            "A prioridade é ALTA (ou URGENTE) pela perda direta de receita e impacto imediato nas conversões do e-commerce."
        ),
    },
    {
        "descricao": (
            "O relatório mensal exibe os valores financeiros sem o "
            "símbolo 'R$', dificultando a leitura. Os valores estão corretos."
        ),
        "severidades_aceitaveis": ["Baixa", "Média"],
        "prioridades_aceitaveis": ["Baixa", "Média", "Alta"],
        "severidade_sugerida": "Baixa",
        "prioridade_sugerida": "Média",
        "explicacao": (
            "A severidade é BAIXA (ou MÉDIA) porque os cálculos e dados estão corretos, tratando-se de formatação visual. "
            "A prioridade pode ser BAIXA (se for uso interno da equipe), MÉDIA ou ALTA (se for enviado imediatamente a "
            "clientes ou auditoria externa). O contexto de negócio dita a urgência."
        ),
    },
]

SEVERIDADE_PRIORIDADE_EXPLICACAO = (
    "Severidade está relacionada ao IMPACTO técnico ou de negócio "
    "causado pelo problema.\n"
    "Prioridade está relacionada à URGÊNCIA ou ordem de tratamento.\n\n"
    "São conceitos complementares mas independentes. Um defeito pode "
    "ter alta severidade e baixa prioridade, ou vice-versa.\n\n"
    "Não existe uma regra universal que determine que determinada "
    "combinação sempre resulta em uma classificação específica. "
    "A análise deve considerar o contexto e o impacto para o negócio.\n\n"
    "Fonte: Módulo 1, item 7 e Módulo 2, itens 20 e 21."
)


def validar_severidade_prioridade(cenario, severidade, prioridade):
    """
    Avalia a classificação de severidade e prioridade de forma contextual e pedagógica.
    - Severidade é avaliada pelo impacto funcional/técnico apresentado.
    - Prioridade é avaliada considerando múltiplos contextos de negócio plausíveis,
      não punindo o aluno apenas por divergir de uma 'prioridade sugerida' fixa.

    Args:
        cenario: dict do cenário em CENARIOS_SEVERIDADE_PRIORIDADE
        severidade: str informada pelo usuário
        prioridade: str informada pelo usuário

    Returns:
        (sev_ok: bool, pri_ok: bool, f_sev: str, f_pri: str, explicacao: str)
    """
    sev_aceitaveis = cenario.get("severidades_aceitaveis", [cenario.get("severidade_sugerida")])
    pri_aceitaveis = cenario.get("prioridades_aceitaveis", [cenario.get("prioridade_sugerida")])

    sev_ok = severidade in sev_aceitaveis
    pri_ok = prioridade in pri_aceitaveis

    if sev_ok:
        f_sev = f"✅ Coerente com o impacto ({severidade})"
    else:
        f_sev = f"❌ Incoerente com o impacto funcional (impacto esperado: {', '.join(sev_aceitaveis)})"

    if pri_ok:
        f_pri = f"✅ Coerente no contexto de negócio ({prioridade})"
    else:
        f_pri = f"❌ Incoerente com a urgência deste cenário (esperado: {', '.join(pri_aceitaveis)})"

    return sev_ok, pri_ok, f_sev, f_pri, cenario["explicacao"]


# =====================================================================
# 8. CASO DE TESTE
# =====================================================================

CASO_TESTE_CAMPOS = [
    ("ct_id", "ID do Caso de Teste", True),
    ("titulo", "Título", True),
    ("prioridade", "Prioridade", False),
    ("pre_condicoes", "Pré-condições", False),
    ("dados", "Dados de Teste", False),
    ("passos", "Passos", True),
    ("resultado_esperado", "Resultado Esperado", True),
    ("pos_condicoes", "Pós-condições", False),
]

CASO_TESTE_EXPLICACAO = (
    "Um caso de teste bem estruturado deve conter informações "
    "suficientes para que qualquer pessoa consiga executá-lo.\n\n"
    "Campos obrigatórios:\n"
    "• ID — Identificador único do caso de teste\n"
    "• Título — Descrição clara do que está sendo testado\n"
    "• Passos — Sequência de ações a serem executadas\n"
    "• Resultado Esperado — O que deve acontecer ao final\n\n"
    "Campos opcionais (mas recomendados):\n"
    "• Prioridade — Importância do caso de teste\n"
    "• Pré-condições — O que precisa estar configurado antes\n"
    "• Dados de Teste — Valores a serem utilizados\n"
    "• Pós-condições — Estado do sistema após a execução\n\n"
    "Fonte: Módulo 1, item 4 e Módulo 2, item 15."
)


def validar_caso_teste(campos):
    """
    Valida os campos obrigatórios de um caso de teste.

    Args:
        campos: dict com os campos do caso de teste

    Returns:
        (valido, mensagem)
    """
    erros = []

    for campo_id, nome, obrigatorio in CASO_TESTE_CAMPOS:
        valor = campos.get(campo_id, "").strip()
        if obrigatorio and len(valor) < 2:
            erros.append(f"• {nome} é obrigatório e precisa ser preenchido.")

    if erros:
        return False, "O caso de teste está incompleto:\n\n" + "\n".join(erros)

    return (
        True,
        "✅ Caso de teste válido! Todos os campos obrigatórios foram preenchidos.\n\n"
        "O caso de teste foi salvo com sucesso.",
    )


# =====================================================================
# 9. GHERKIN
# =====================================================================

GHERKIN_PALAVRAS_CHAVE = ["Dado", "E", "Quando", "E", "Então"]

GHERKIN_EXEMPLO = (
    "Exemplo de cenário Gherkin:\n\n"
    "Dado que o usuário está na página de login\n"
    "E possui credenciais válidas\n"
    "Quando informa e-mail e senha\n"
    "E clica em entrar\n"
    "Então o sistema exibe a página inicial"
)

GHERKIN_EXPLICACAO = (
    "Gherkin é uma sintaxe utilizada para descrever cenários de forma "
    "legível usando palavras-chave: Dado, E, Quando, Então.\n\n"
    "Estrutura:\n"
    "• DADO — Estabelece o contexto inicial (pré-condição)\n"
    "• E — Complementa a etapa anterior\n"
    "• QUANDO — Descreve a ação executada\n"
    "• E — Complementa a ação\n"
    "• ENTÃO — Define o resultado esperado\n\n"
    "Gherkin não é o mesmo que BDD. BDD é uma abordagem de desenvolvimento, "
    "enquanto Gherkin é a sintaxe utilizada para descrever comportamentos.\n\n"
    "Fonte: Módulo 1, item 5 e Módulo 2, item 16."
)


def validar_gherkin(dado, e1, quando, e2, entao):
    """
    Valida se o cenário Gherkin possui os elementos obrigatórios preenchidos.

    Returns:
        (valido, mensagem, cenario_formatado)
    """
    dado = dado.strip() if dado else ""
    e1 = e1.strip() if e1 else ""
    quando = quando.strip() if quando else ""
    e2 = e2.strip() if e2 else ""
    entao = entao.strip() if entao else ""

    erros = []
    if len(dado) < 3:
        erros.append("• O campo DADO precisa ser preenchido (contexto inicial).")
    if len(quando) < 3:
        erros.append("• O campo QUANDO precisa ser preenchido (ação executada).")
    if len(entao) < 3:
        erros.append("• O campo ENTÃO precisa ser preenchido (resultado esperado).")

    if erros:
        return (
            False,
            "O cenário Gherkin está incompleto:\n\n" + "\n".join(erros) +
            "\n\nOs campos Dado, Quando e Então são obrigatórios. "
            "Os campos E são opcionais.",
            "",
        )

    # Montar cenário formatado
    linhas = [f"Dado {dado}"]
    if e1:
        linhas.append(f"E {e1}")
    linhas.append(f"Quando {quando}")
    if e2:
        linhas.append(f"E {e2}")
    linhas.append(f"Então {entao}")

    cenario = "\n".join(linhas)

    return (
        True,
        "✅ Cenário Gherkin válido! A estrutura está correta.\n\n"
        "Seu cenário utiliza as palavras-chave corretas e segue "
        "a estrutura Dado/Quando/Então.",
        cenario,
    )


# =====================================================================
# 10. REGISTRO DE DEFEITO
# =====================================================================

DEFEITO_CAMPOS = [
    ("titulo", "Título", True),
    ("contexto", "Contexto", False),
    ("passos_reproducao", "Passos para Reprodução", True),
    ("resultado_esperado", "Resultado Esperado", True),
    ("resultado_atual", "Resultado Atual", True),
    ("evidencia", "Evidência", False),
    ("ambiente", "Ambiente", False),
    ("versao", "Versão", False),
    ("severidade", "Severidade", False),
    ("prioridade", "Prioridade", False),
]

DEFEITO_EXPLICACAO = (
    "Um bom registro de defeito deve permitir que outra pessoa "
    "compreenda e reproduza o problema.\n\n"
    "Campos obrigatórios:\n"
    "• Título — Descrição clara e objetiva do defeito\n"
    "• Passos para Reprodução — Como chegar ao problema\n"
    "• Resultado Esperado — O que deveria acontecer\n"
    "• Resultado Atual — O que realmente aconteceu\n\n"
    "Campos recomendados:\n"
    "• Contexto — Informações adicionais sobre a situação\n"
    "• Evidência — Screenshots, vídeos, logs\n"
    "• Ambiente — Navegador, SO, dispositivo\n"
    "• Versão — Versão do sistema testado\n"
    "• Severidade — Impacto do defeito\n"
    "• Prioridade — Urgência de tratamento\n\n"
    "Fonte: Módulo 1, item 6 e Módulo 2, item 19."
)


def validar_registro_defeito(campos):
    """
    Valida os campos obrigatórios de um registro de defeito.

    Args:
        campos: dict com os campos do defeito

    Returns:
        (valido, mensagem)
    """
    erros = []

    for campo_id, nome, obrigatorio in DEFEITO_CAMPOS:
        valor = campos.get(campo_id, "").strip()
        if obrigatorio and len(valor) < 2:
            erros.append(f"• {nome} é obrigatório e precisa ser preenchido.")

    if erros:
        return False, "O registro de defeito está incompleto:\n\n" + "\n".join(erros)

    return (
        True,
        "✅ Registro de defeito válido! Todos os campos obrigatórios "
        "foram preenchidos.\n\n"
        "O defeito foi salvo com sucesso no banco de dados.",
    )

