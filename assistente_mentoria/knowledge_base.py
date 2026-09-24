"""
Base de conhecimento — Assistente de Estudos — Mentoria 2.0
Conteúdo completo dos Módulos 1 e 2 de Testes de Software.
Motor de busca por palavras-chave com scoring e sinônimos.
Desenvolvido por Adalton.
"""

import unicodedata
import re


# =====================================================================
# MÓDULO 1 — FUNDAMENTOS E MENTALIDADE
# =====================================================================

MODULO_1 = [
    {
        "titulo": "O verdadeiro papel dos testes de software",
        "conteudo": (
            "Testar envolve investigação, aprendizagem, exploração, observação e busca "
            "por informações sobre o produto. Os testes não provam que um sistema está "
            "completamente livre de defeitos. O trabalho do QA está relacionado à "
            "identificação e redução de riscos."
        ),
    },
    {
        "titulo": "Testar e garantir qualidade",
        "conteudo": (
            "Teste de Software está relacionado à avaliação do produto. Quality Assurance "
            "possui uma visão mais ampla, envolvendo processos, práticas e prevenção de "
            "problemas."
        ),
    },
    {
        "titulo": "Como o QA define o que testar",
        "conteudo": (
            "A definição pode considerar requisitos, regras de negócio, comportamento esperado, "
            "interface, APIs, código, histórico de problemas e riscos. O QA utiliza experiência, "
            "conhecimento técnico e pensamento crítico."
        ),
    },
    {
        "titulo": "Execução de testes",
        "conteudo": (
            "Casos de teste podem conter ID, título, pré-condições, dados, passos, resultado "
            "esperado, pós-condições, ambiente e versão. Isso facilita reprodução e rastreabilidade."
        ),
    },
    {
        "titulo": "Gherkin",
        "conteudo": (
            "Gherkin é uma linguagem/sintaxe utilizada para descrever cenários de forma legível, "
            "usando palavras-chave como Dado, Quando e Então. Gherkin não é o mesmo que BDD. "
            "BDD (Behavior Driven Development) é uma abordagem de desenvolvimento, enquanto "
            "Gherkin é a sintaxe utilizada para descrever os cenários de comportamento."
        ),
    },
    {
        "titulo": "Registro de defeitos",
        "conteudo": (
            "Um bom relatório deve permitir que outra pessoa compreenda e reproduza o problema. "
            "Deve conter informações como título, passos, resultado esperado, resultado atual, "
            "evidências, ambiente, versão, severidade, prioridade e status."
        ),
    },
    {
        "titulo": "Severidade e prioridade",
        "conteudo": (
            "Severidade está relacionada ao impacto técnico ou de negócio causado pelo problema. "
            "Prioridade está relacionada à urgência ou ordem de tratamento. "
            "Severidade e prioridade são conceitos complementares mas independentes. "
            "Um defeito pode ter alta severidade mas baixa prioridade, ou vice-versa, "
            "dependendo do contexto e do impacto para o negócio."
        ),
    },
    {
        "titulo": "Processo de testes",
        "conteudo": (
            "Analisar requisitos → Identificar riscos → Definir testes → Criar cenários → "
            "Executar → Registrar resultados → Reportar defeitos → Retestar. "
            "Esse fluxo garante organização e rastreabilidade no processo de testes."
        ),
    },
    {
        "titulo": "Reteste e regressão",
        "conteudo": (
            "Reteste verifica se o defeito corrigido foi realmente solucionado. "
            "Testes de regressão verificam se alterações não prejudicaram funcionalidades "
            "que anteriormente funcionavam. Ambos são essenciais para garantir a qualidade "
            "após correções e mudanças no sistema."
        ),
    },
    {
        "titulo": "Inteligência Artificial no QA",
        "conteudo": (
            "IA pode auxiliar na análise de requisitos, identificação de riscos, criação de "
            "cenários, dados de teste, scripts e automação. Toda saída da IA deve ser revisada "
            "e validada pelo QA. A IA é uma ferramenta de apoio, não substitui o raciocínio "
            "e a experiência do profissional."
        ),
    },
    {
        "titulo": "Valor do QA",
        "conteudo": (
            "QA contribui para reduzir riscos, evitar prejuízos, retrabalho, problemas "
            "operacionais e impactos negativos para o negócio. O profissional de QA agrega "
            "valor ao identificar problemas antes que cheguem ao usuário final."
        ),
    },
    {
        "titulo": "Programação e QA",
        "conteudo": (
            "Conhecimentos de lógica, código, APIs, automação e integração ajudam o "
            "profissional de QA a investigar problemas e colaborar com desenvolvedores. "
            "Não é obrigatório saber programar para ser QA, mas o conhecimento técnico "
            "amplia as possibilidades de atuação."
        ),
    },
    {
        "titulo": "Automação de testes",
        "conteudo": (
            "Automação traz velocidade, repetibilidade e escala, mas não substitui o "
            "raciocínio do QA. O profissional precisa decidir o que automatizar, por que "
            "automatizar e como validar. Nem tudo precisa ou deve ser automatizado."
        ),
    },
    {
        "titulo": "Tecnologias para QA",
        "conteudo": (
            "Entre as tecnologias citadas estão JavaScript, Python, Java, C#, Ruby, "
            "Selenium, Cypress, Playwright, Postman, Cucumber, Jira e Jenkins. "
            "A escolha depende do projeto, da equipe e do contexto."
        ),
    },
    {
        "titulo": "Testes baseados em riscos",
        "conteudo": (
            "O QA deve identificar quais partes do sistema apresentam maior risco e "
            "impacto e direcionar os esforços para essas áreas. Nem tudo pode ser testado "
            "exaustivamente, por isso a priorização por risco é fundamental."
        ),
    },
    {
        "titulo": "Trabalho em equipe",
        "conteudo": (
            "QA e desenvolvimento fazem parte do mesmo time. O objetivo ao encontrar "
            "defeitos é colaborar para solucionar problemas, utilizando evidências e "
            "comunicação técnica. O QA não é adversário do desenvolvedor."
        ),
    },
    {
        "titulo": "Senioridade em QA",
        "conteudo": (
            "A senioridade varia conforme empresa e contexto. O crescimento envolve "
            "conhecimentos técnicos, autonomia, visão de negócio, comunicação e "
            "capacidade de investigação."
        ),
    },
]


# =====================================================================
# MÓDULO 2 — MODELAGEM, DOCUMENTAÇÃO E EXECUÇÃO DE TESTES
# =====================================================================

MODULO_2 = [
    {
        "titulo": "Fluxo de testes",
        "conteudo": (
            "O fluxo de testes segue as etapas: Compreender → Modelar → Documentar → "
            "Executar → Comunicar → Confirmar. Cada etapa é importante para garantir "
            "que os testes sejam eficazes e rastreáveis."
        ),
    },
    {
        "titulo": "Checking",
        "conteudo": (
            "Checking verifica uma expectativa ou resultado conhecido. É uma verificação "
            "objetiva, geralmente automatizável, que confirma se algo funciona conforme "
            "o esperado. Exemplo: verificar se um botão exibe a cor correta."
        ),
    },
    {
        "titulo": "Testing",
        "conteudo": (
            "Testing possui característica investigativa, utilizando perguntas, hipóteses, "
            "observação e aprendizado. Vai além da simples verificação e busca descobrir "
            "comportamentos inesperados. Exemplo: explorar um formulário com dados "
            "inesperados para observar como o sistema reage."
        ),
    },
    {
        "titulo": "Teste Ad hoc",
        "conteudo": (
            "Teste Ad hoc não depende de roteiro formal pré-definido e pode ser útil "
            "para exploração rápida, embora possa apresentar baixa rastreabilidade se "
            "não for registrado. É realizado sem planejamento prévio estruturado."
        ),
    },
    {
        "titulo": "Teste exploratório",
        "conteudo": (
            "Teste exploratório combina aprendizagem, desenho do teste e execução. "
            "O testador aprende sobre o sistema enquanto testa, adaptando sua abordagem "
            "conforme descobre informações. É uma abordagem estruturada de exploração."
        ),
    },
    {
        "titulo": "Heurísticas",
        "conteudo": (
            "Heurísticas orientam o pensamento durante a investigação e ajudam a ampliar "
            "os cenários considerados. São regras práticas ou guias mentais que auxiliam "
            "na identificação de possíveis problemas."
        ),
    },
    {
        "titulo": "SBTM — Session-Based Test Management",
        "conteudo": (
            "SBTM (Session-Based Test Management) organiza testes exploratórios por "
            "sessões, combinando liberdade e estrutura. Cada sessão tem tempo definido, "
            "um charter (missão) e gera um relatório ao final."
        ),
    },
    {
        "titulo": "Test Charter",
        "conteudo": (
            "Test Charter é a missão que define o alvo da exploração, os recursos ou "
            "técnicas a serem utilizados e a informação que se deseja descobrir. "
            'Modelo: "Explorar [alvo] com [recursos/técnicas] para descobrir [informação]."'
        ),
    },
    {
        "titulo": "Partição de equivalência",
        "conteudo": (
            "Partição de equivalência divide entradas em grupos (classes) que apresentam "
            "comportamento semelhante. Em vez de testar todos os valores possíveis, "
            "seleciona-se um representante de cada classe. Exemplo: se o mínimo aceito "
            "é R$ 10,00, uma classe inválida seria valores menores que R$ 10,00 e uma "
            "classe válida seria valores iguais ou maiores que R$ 10,00."
        ),
    },
    {
        "titulo": "Análise do valor limite",
        "conteudo": (
            "Análise do valor limite concentra os testes nas fronteiras de uma regra. "
            "Os defeitos frequentemente ocorrem nos limites das condições. "
            "Exemplo: se o mínimo é R$ 10,00, testar R$ 9,99 (abaixo do limite), "
            "R$ 10,00 (no limite) e R$ 10,01 (acima do limite)."
        ),
    },
    {
        "titulo": "Tabela de decisão",
        "conteudo": (
            "Tabela de decisão combina diferentes condições e resultados para gerar "
            "cenários de teste. É útil quando há múltiplas condições que interagem "
            "entre si e precisam ser testadas em combinação."
        ),
    },
    {
        "titulo": "Cobertura de sentença",
        "conteudo": (
            "Cobertura de sentença busca exercitar comandos executáveis relevantes "
            "do código. O objetivo é garantir que cada instrução do código seja "
            "executada pelo menos uma vez durante os testes."
        ),
    },
    {
        "titulo": "Cobertura de decisão",
        "conteudo": (
            "Cobertura de decisão exercita resultados verdadeiro e falso de uma "
            "condição. Garante que cada desvio no código (if/else) seja exercitado "
            "em ambas as direções."
        ),
    },
    {
        "titulo": "Condição de teste",
        "conteudo": (
            "Condição de teste representa o que precisa ser testado a partir de um "
            "requisito, regra ou risco. É a base para a criação dos casos de teste."
        ),
    },
    {
        "titulo": "Caso de teste",
        "conteudo": (
            "Caso de teste pode conter ID, título, prioridade, rastreabilidade, "
            "pré-condições, passos, dados, resultados esperados e pós-condições. "
            "Um bom caso de teste é claro, reproduzível e rastreável ao requisito."
        ),
    },
    {
        "titulo": "Gherkin (Módulo 2)",
        "conteudo": (
            "Gherkin utiliza as palavras-chave Dado, Quando, Então e E para descrever "
            "comportamentos esperados. É uma forma estruturada e legível de documentar "
            "cenários de teste. Exemplo:\n"
            "Dado que o usuário está na página de login\n"
            "E possui credenciais válidas\n"
            "Quando informa e-mail e senha\n"
            "E clica em entrar\n"
            "Então o sistema exibe a página inicial"
        ),
    },
    {
        "titulo": "Cucumber",
        "conteudo": (
            "Cucumber é uma ferramenta relacionada à automação de cenários descritos "
            "em Gherkin. Permite executar os cenários escritos em linguagem natural "
            "como testes automatizados."
        ),
    },
    {
        "titulo": "Jira e Zephyr",
        "conteudo": (
            "Jira pode ser utilizado para gerenciamento de projetos e Zephyr Squad "
            "para apoiar a execução e organização dos testes. Ambas são ferramentas "
            "amplamente utilizadas em equipes de QA."
        ),
    },
    {
        "titulo": "Registro de defeitos (Módulo 2)",
        "conteudo": (
            "O registro de defeitos deve possuir informações suficientes para "
            "compreensão, reprodução, análise e acompanhamento do problema. "
            "Inclui: título, contexto, passos para reprodução, resultado esperado, "
            "resultado atual, evidências, ambiente, versão, severidade e prioridade."
        ),
    },
    {
        "titulo": "Severidade",
        "conteudo": (
            "Severidade refere-se ao impacto causado pelo defeito. Pode ser classificada "
            "como Baixa, Média, Alta ou Crítica, dependendo do quanto o defeito afeta "
            "o funcionamento do sistema ou o negócio."
        ),
    },
    {
        "titulo": "Prioridade",
        "conteudo": (
            "Prioridade refere-se à urgência de tratamento do defeito. Indica a ordem "
            "em que o defeito deve ser corrigido. Pode ser classificada como Baixa, "
            "Média, Alta ou Urgente."
        ),
    },
    {
        "titulo": "Reteste",
        "conteudo": (
            "Reteste verifica se uma correção solucionou o problema identificado. "
            "Após o desenvolvedor corrigir um defeito, o QA executa o reteste para "
            "confirmar que a correção foi efetiva."
        ),
    },
    {
        "titulo": "Regressão",
        "conteudo": (
            "Testes de regressão verificam possíveis impactos colaterais causados "
            "por alterações. Garantem que funcionalidades que funcionavam antes "
            "continuem funcionando após mudanças no sistema."
        ),
    },
]


# =====================================================================
# SINÔNIMOS E TERMOS RELACIONADOS
# =====================================================================

SINONIMOS = {
    "qa": ["quality assurance", "qualidade", "testador", "analista de testes",
           "analista de qualidade", "profissional de qualidade"],
    "bva": ["valor limite", "valor de fronteira", "boundary value",
            "analise do valor limite", "fronteira"],
    "bug": ["defeito", "erro", "problema", "falha", "incidente", "issue"],
    "teste": ["testes", "testar", "testando", "test", "testing"],
    "automatizar": ["automacao", "automatizado", "automation", "automatizacao",
                    "automatização", "automação"],
    "explorar": ["exploratorio", "exploracao", "exploratório", "exploração",
                 "exploratory"],
    "gherkin": ["dado quando entao", "bdd", "cenario", "cenários", "cenarios"],
    "severidade": ["severity", "impacto", "gravidade", "grave"],
    "prioridade": ["priority", "urgencia", "urgência", "urgente"],
    "checking": ["verificacao", "verificação", "checar", "conferir"],
    "testing": ["teste", "testes", "testar", "test", "investigacao", "investigação"],
    "regressao": ["regressão", "regression", "regressivo"],
    "reteste": ["retest", "re-teste", "retestar"],
    "charter": ["test charter", "missao", "missão", "sbtm", "sessao", "sessão"],
    "particao": ["partição", "particionamento", "equivalencia", "equivalência",
                 "classes de equivalencia", "classes"],
    "tabela": ["tabela de decisao", "tabela de decisão", "decision table",
               "combinacoes", "combinações"],
    "cucumber": ["bdd", "automacao gherkin"],
    "jira": ["gerenciamento", "gestao", "gestão"],
    "zephyr": ["execucao de testes", "execução de testes"],
    "caso de teste": ["test case", "caso de testes", "cenario de teste",
                      "caso", "ct"],
    "defeito": ["bug", "erro", "falha", "problema", "registro de defeito"],
    "risco": ["riscos", "risk", "priorização"],
    "heuristica": ["heurísticas", "heurístico", "heuristics"],
    "ad hoc": ["adhoc", "sem roteiro", "informal"],
    "cobertura": ["coverage", "sentença", "decisão", "sentenca", "decisao"],
    "fluxo": ["processo", "etapas", "workflow"],
}

# Palavras irrelevantes para a pesquisa
STOPWORDS = {
    "o", "a", "os", "as", "de", "da", "do", "das", "dos", "em", "no", "na",
    "nos", "nas", "um", "uma", "uns", "umas", "e", "ou", "que", "qual", "como",
    "para", "por", "com", "se", "eh", "sao", "esta", "estao", "foi", "foram",
    "ser", "ter", "fazer", "dizer", "ir", "ao", "pelo", "pela", "entre",
    "sobre", "mais", "muito", "tambem", "ja", "ainda", "quando", "mas", "nao",
    "sim", "isso", "isto", "esse", "essa", "este", "seu", "sua", "meu",
    "minha", "me", "te", "lhe", "voce", "ele", "ela", "nos", "eles", "elas",
    "quero", "queria", "pode", "posso", "preciso", "gostaria", "fale",
    "explique", "descreva", "conte", "diga", "diferenca", "diferença",
}


# =====================================================================
# FUNÇÕES DE BUSCA
# =====================================================================

def normalizar(texto):
    """Remove acentos e converte para minúsculas."""
    nfkd = unicodedata.normalize("NFKD", str(texto))
    sem_acentos = "".join(c for c in nfkd if not unicodedata.combining(c))
    return sem_acentos.lower().strip()


def extrair_palavras(texto):
    """Extrai palavras significativas do texto (sem stopwords)."""
    texto_norm = normalizar(texto)
    palavras = re.findall(r"\b\w+\b", texto_norm)
    return [p for p in palavras if p not in STOPWORDS and len(p) > 1]


def expandir_sinonimos(palavras):
    """Expande a lista de palavras incluindo sinônimos conhecidos."""
    expandidas = set(palavras)
    for palavra in list(palavras):
        for chave, lista_sins in SINONIMOS.items():
            chave_norm = normalizar(chave)
            todas_formas = [chave_norm] + [normalizar(s) for s in lista_sins]
            if palavra in todas_formas:
                # Adiciona todas as formas como palavras individuais
                for forma in todas_formas:
                    for p in forma.split():
                        if p not in STOPWORDS and len(p) > 1:
                            expandidas.add(p)
    return list(expandidas)


def pesquisar(pergunta, modulo="todos"):
    """
    Pesquisa na base de conhecimento por relevância.

    Args:
        pergunta: texto da pergunta do usuário
        modulo: "modulo1", "modulo2" ou "todos"

    Returns:
        lista de dicts com: titulo, conteudo, fonte, score
    """
    # Selecionar base de dados conforme módulo
    if modulo == "modulo1":
        base = [(t, "Módulo 1 — Fundamentos e Mentalidade") for t in MODULO_1]
    elif modulo == "modulo2":
        base = [(t, "Módulo 2 — Modelagem, Documentação e Execução") for t in MODULO_2]
    else:
        base = (
            [(t, "Módulo 1 — Fundamentos e Mentalidade") for t in MODULO_1]
            + [(t, "Módulo 2 — Modelagem, Documentação e Execução") for t in MODULO_2]
        )

    # Palavras originais da pergunta (sem stopwords)
    palavras_originais = extrair_palavras(pergunta)
    if not palavras_originais:
        return []

    # Sinônimos apenas para palavras que não estão diretamente na pergunta
    todas_expandidas = expandir_sinonimos(palavras_originais)
    sinonimos_puros = [p for p in todas_expandidas if p not in palavras_originais]

    # Detectar se a pergunta envolve a dualidade Checking e Testing
    termos_checking = {"checking", "checar", "verificacao", "conferir"}
    termos_testing = {"testing", "teste", "testes", "testar"}
    tem_checking = bool(termos_checking.intersection(set(palavras_originais + todas_expandidas)))
    tem_testing = bool(termos_testing.intersection(set(palavras_originais + todas_expandidas)))
    busca_checking_testing = tem_checking and tem_testing

    resultados = []

    for topico, fonte in base:
        titulo_norm = normalizar(topico["titulo"])
        conteudo_norm = normalizar(topico["conteudo"])
        palavras_titulo = re.findall(r"\b\w+\b", titulo_norm)

        score = 0
        termos_originais_atendidos = 0

        # 1. Avaliar palavras originais da pergunta (prioridade máxima)
        for p in palavras_originais:
            match_no_topico = False
            # Match exato de palavra inteira no título
            if p in palavras_titulo:
                score += 25
                match_no_topico = True
            elif p in titulo_norm:
                score += 15
                match_no_topico = True

            # Match no conteúdo
            if p in conteudo_norm:
                score += 5
                match_no_topico = True

            if match_no_topico:
                termos_originais_atendidos += 1

        # 2. Sinônimos derivados (peso moderado para não sobrepor palavras diretas)
        for s in sinonimos_puros:
            if s in palavras_titulo:
                score += 4
            elif s in titulo_norm:
                score += 2
            if s in conteudo_norm:
                score += 1

        # 3. Bônus de cobertura multi-termo:
        # Quando o aluno pergunta sobre mais de um conceito (ex: "Testing e Checking",
        # "Severidade e prioridade"), tópicos que contemplam esses termos ganham bônus
        if len(palavras_originais) > 1 and termos_originais_atendidos > 1:
            score += termos_originais_atendidos * 15

        # 4. Tratamento específico para a dualidade Checking x Testing
        if busca_checking_testing:
            if titulo_norm in ("checking", "testing"):
                score += 60
            elif "checking" not in titulo_norm and "checking" not in conteudo_norm:
                # Tópicos genéricos sobre testes que não abordam checking perdem relevância
                score = max(0, score - 30)

        # 5. Bônus para frases contínuas ou expressões compostas da pergunta
        for i in range(len(palavras_originais)):
            for j in range(i + 2, len(palavras_originais) + 1):
                frase = " ".join(palavras_originais[i:j])
                if len(frase) > 4:
                    if frase in titulo_norm:
                        score += 30
                    elif frase in conteudo_norm:
                        score += 10

        if score > 0:
            resultados.append({
                "titulo": topico["titulo"],
                "conteudo": topico["conteudo"],
                "fonte": fonte,
                "score": score,
            })

    # Ordenar por relevância (maior score primeiro)
    resultados.sort(key=lambda x: x["score"], reverse=True)

    # Retornar os 5 mais relevantes
    return resultados[:5]


def formatar_resposta(resultados):
    """
    Formata os resultados da pesquisa em uma resposta legível.

    Returns:
        (texto_resposta, fonte_principal)
    """
    if not resultados:
        return (
            "Não encontrei informação suficiente sobre esse assunto nos "
            "materiais cadastrados.\n\n"
            "Tente reformular a pergunta ou use termos diferentes.\n"
            "Os conteúdos disponíveis são dos Módulos 1 e 2 da Mentoria.",
            "",
        )

    partes = []
    fontes = set()

    for i, res in enumerate(resultados):
        partes.append(f"📌 {res['titulo']}\n\n{res['conteudo']}")
        fontes.add(res["fonte"])

    separador = "\n\n" + ("─" * 50) + "\n\n"
    texto = separador.join(partes)
    fonte_texto = " | ".join(sorted(fontes))

    return texto.strip(), fonte_texto

