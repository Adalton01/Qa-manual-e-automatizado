# Assistente de Estudos — Mentoria 2.0

> **Desenvolvido por:** Adalton  
> **Identidade visual / Marca d'água:** MENTORIA 2.0 — por Júlio de Lima  
> **Ambiente:** Windows 11 (Python 3.10+ e SQLite local)

---

## 1. Nome do Projeto

**Assistente de Estudos — Mentoria 2.0**

---

## 2. Objetivo do Aplicativo

O aplicativo foi desenvolvido como um assistente desktop completo para apoiar a fixação e o aprendizado prático de **Testes de Software / Quality Assurance (QA)**. Ele permite consultar tópicos teóricos, pesquisar respostas fundamentadas, executar exercícios práticos baseados nas técnicas aprendidas, avaliar respostas de 1 a 5 estrelas e acompanhar todo o histórico e progresso do estudante localmente.

O software funciona 100% offline no **Windows 11**, sem a necessidade de internet, servidores web ou APIs externas pagas.

---

## 3. Relação com os Estudos dos Módulos 1 e 2

Todo o motor de busca e as regras de avaliação das atividades são rigorosamente fundamentados nos conteúdos da Mentoria:

- **Módulo 1 — Fundamentos e Mentalidade:**
  - Papel do teste e redução de riscos;
  - Teste vs Garantia de Qualidade (QA);
  - Como o QA define o que testar (riscos, requisitos, código, APIs);
  - Execução e estrutura de casos de teste;
  - Conceito de Gherkin e distinção em relação ao BDD;
  - Relatórios e registro de defeitos;
  - Severidade (impacto) vs Prioridade (urgência);
  - Processo de testes (análise, modelagem, execução, reporte e reteste);
  - Reteste vs Testes de Regressão;
  - Inteligência Artificial no QA e validação humana;
  - Valor do QA para o negócio;
  - Programação, automação e ferramentas (Selenium, Playwright, Cypress, Postman, Jira, Jenkins);
  - Trabalho colaborativo em equipe e níveis de senioridade.

- **Módulo 2 — Modelagem, Documentação e Execução:**
  - Fluxo de testes (Compreender → Modelar → Documentar → Executar → Comunicar → Confirmar);
  - Checking (verificação objetiva de expectativa conhecida) vs Testing (investigação e exploração);
  - Teste Ad hoc, Teste Exploratório e Heurísticas;
  - SBTM (Session-Based Test Management) e Test Charter;
  - Partição de Equivalência (classes válidas e inválidas);
  - Análise do Valor Limite (fronteiras de regras);
  - Tabela de Decisão para combinações de condições complexas;
  - Cobertura de Sentença e Decisão;
  - Documentação e gestão com Jira e Zephyr Squad.

---

## 4. Funcionalidades Existentes na Versão Final

O aplicativo conta com **6 telas principais**, navegáveis por um menu lateral moderno:

1. **🏠 Início:**
   - Apresentação acolhedora e síntese dos recursos disponíveis.
   - Marca d'água discreta _"MENTORIA 2.0 — por Júlio de Lima"_.

2. **📚 Perguntas e Respostas:**
   - Seleção do escopo da consulta: _Módulo 1_, _Módulo 2_ ou _Todos os módulos_.
   - Campo de busca para perguntas abertas com atalhos de sugestões frequentes.
   - Resposta detalhada e indicação explícita da fonte (_"📎 Fonte: Módulo 1"_ ou _"Módulo 2"_).
   - Mensagem padrão de segurança quando o assunto não constar na base: _"Não encontrei informação suficiente sobre esse assunto nos materiais cadastrados."_
   - Sistema de avaliação com **5 estrelas clicáveis** (☆ $\rightarrow$ ★), campo opcional de observação e botão para salvar no banco SQLite.

3. **📝 Atividades de Testes (10 Atividades Práticas):**
   - Ambiente prático onde o aluno realiza exercícios baseados nas técnicas aprendidas, recebe feedback imediato com justificativa técnica, pontuação e registro automático no banco.

4. **📋 Histórico:**
   - Abas organizadas para visualização:
     - **⭐ Avaliações:** histórico de perguntas feitas, respostas obtidas, notas em estrelas e observações.
     - **📄 Casos de Teste:** casos criados e salvos durante a prática da Atividade 8.
     - **🐛 Defeitos:** relatórios de bugs registrados durante a prática da Atividade 10.
   - Visualização detalhada do registro completo em janela pop-up.
   - Botões de **Atualizar** e **Excluir registro** com caixa de confirmação.

5. **📊 Progresso:**
   - Painel de desempenho exibindo total de tentativas, acertos, erros e taxa percentual de sucesso.
   - Tabela consolidada com as estatísticas de cada uma das 10 atividades.
   - Histórico detalhado de execuções com data e hora.
   - Opção para limpar o histórico com confirmação.

6. **ℹ️ Sobre:**
   - Informações sobre a versão da aplicação, tecnologias utilizadas e créditos a **Adalton** e à **Mentoria 2.0 por Júlio de Lima**.

---

## 5. Estrutura dos Arquivos

```text
assistente_mentoria/
│
├── main.py              # Ponto de entrada do aplicativo (inicialização)
├── ui.py                # Interface gráfica moderna (ttkbootstrap) com as 6 telas
├── knowledge_base.py    # Base de conhecimento dos Módulos 1 e 2 + busca com sinônimos
├── activities.py        # Cenários e regras de validação das 10 atividades práticas
├── database.py          # Gerenciamento do banco de dados SQLite local (CRUD)
├── avaliacoes.db        # Banco SQLite gerado automaticamente na primeira execução
└── README.md            # Documentação técnica e guia do usuário
```

---

## 6. Dependências

O aplicativo requer Python 3.10 ou superior e as seguintes bibliotecas:

- `ttkbootstrap` (estilização e temas modernos sobre Tkinter)
- `Pillow` (suporte a renderização e manipulação gráfica)
- `sqlite3` (incluso nativamente no Python padrão)

---

## 7. Como Instalar no Windows 11

1. Certifique-se de que o **Python 3.10+** está instalado no Windows 11 (disponível na Microsoft Store ou em [python.org](https://www.python.org)). Durante a instalação pelo instalador padrão, marque a opção _"Add Python to PATH"_.
2. Abra o **Terminal do Windows**, **PowerShell** ou **Prompt de Comando (CMD)**.
3. Instale as dependências com o comando:
   ```powershell
   pip install ttkbootstrap pillow
   ```

---

## 8. Como Executar

### Opção A — Pelo Terminal

1. Navegue até a pasta do projeto:
   ```powershell
   cd "C:\Users\Dalton\Desktop\Julio de lima\Projeto do Claude\assistente_mentoria"
   ```
2. Execute o comando:
   ```powershell
   python main.py
   ```

### Opção B — Pelo Explorador de Arquivos

1. Abra a pasta `assistente_mentoria` no Explorador de Arquivos do Windows.
2. Dê um **duplo clique** no arquivo `main.py`.

---

## 9. Como Utilizar as Principais Funcionalidades

### Fazendo uma Consulta de Estudos

1. Clique em **📚 Perguntas e Respostas** no menu lateral.
2. Escolha o módulo desejado ou selecione "Todos os módulos".
3. Digite sua pergunta (ex: _"Qual a diferença entre Testing e Checking?"_ ou _"O que é análise do valor limite?"_).
4. Clique em **🔎 Pesquisar resposta**.
5. Leia a resposta e a fonte indicada.
6. Clique nas estrelas para avaliar a resposta (de 1 a 5), escreva uma observação se desejar e clique em **💾 Salvar avaliação**.

### Consultando o Histórico

1. Clique em **📋 Histórico** no menu lateral.
2. Navegue entre as abas (_Avaliações_, _Casos de Teste_ ou _Defeitos_).
3. Clique em um item da tabela para abrir a janela pop-up com todas as informações completas.
4. Use o botão **🗑️ Excluir selecionado** caso queira remover um item após confirmação.

---

## 10. Como Funcionam as Atividades Práticas

Acesse a tela **📝 Atividades de Testes** e escolha qualquer um dos 10 exercícios clicando em **Iniciar ▶**:

1. **Valor Limite — Análise de Valor de Fronteira:**
   - Avalia a regra de valor mínimo (R$ 10,00) testando R$ 9,99 (abaixo), R$ 10,00 (no limite) e R$ 10,01 (acima). O sistema analisa as fronteiras e justifica os cenários válidos e inválidos.
2. **Particionamento de Equivalência:**
   - O aluno identifica a classe inválida (< R$ 10,00) e a classe válida ($\ge$ R$ 10,00), informando valores numéricos reais. O sistema analisa dinamicamente se o valor pertence à classe esperada.
3. **Tabela de Decisão:**
   - Exercício com condições de valor (< R$ 5.000 vs $\ge$ R$ 5.000) e estados de token bancário (válido, inválido, não informado), validando as decisões de negócio para cada combinação.
4. **Checking × Testing:**
   - 5 cenários do cotidiano de QA para classificar se a ação representa checagem de expectativa conhecida (Checking) ou exploração investigativa (Testing).
5. **Ad hoc × Exploratório:**
   - Cenários práticos para diferenciar teste ad hoc (sem planejamento/registro), teste exploratório (com aprendizagem contínua) e SBTM (com sessão e charter).
6. **Test Charter / SBTM:**
   - Montagem de missão de teste exploratório seguindo a estrutura: _"Explorar [alvo] com [recursos/técnicas] para descobrir [informação]"_. O sistema valida a presença de todos os elementos obrigatórios.
7. **Severidade × Prioridade:**
   - Classificação de defeitos reais, reforçando que Severidade mede o impacto do problema e Prioridade mede a urgência de tratamento, considerando o contexto de negócio.
8. **Caso de Teste:**
   - Formulário guiado com ID, título, prioridade, pré-condições, dados, passos, resultado esperado e pós-condições. Ao validar a estrutura, **salva o caso de teste diretamente no banco SQLite**.
9. **Gherkin:**
   - Prática de escrita com as palavras-chave _Dado_, _E_, _Quando_, _E_, _Então_. O sistema confere a estrutura lógica do cenário BDD.
10. **Registro de Defeito:**
    - Formulário com título, contexto, passos de reprodução, resultados esperado e atual, evidências, ambiente, severidade e prioridade. Ao validar, **armazena o defeito no banco SQLite**.

Cada atividade conta com botão **✔ Verificar resposta**, explicação técnica baseada nos módulos, opção de **🔄 Tentar novamente** e salvamento automático do resultado.

---

## 11. Como o SQLite é Utilizado

O arquivo de banco de dados `avaliacoes.db` é gerado na mesma pasta do projeto de forma automática. Ele possui 4 tabelas relacionais dedicadas:

- `avaliacoes`: armazena data/hora, módulo consultado, pergunta, resposta gerada, estrelas atribuídas e observação.
- `casos_teste`: armazena os casos de teste elaborados na Atividade 8 com todos os seus atributos técnicos.
- `defeitos`: armazena os defeitos cadastrados na Atividade 10 com passos de reprodução, severidade e prioridade.
- `progresso_atividades`: registra cada tentativa de exercício realizada, indicando data/hora, atividade, status de acerto/erro e detalhes do resultado.

Todos os dados permanecem salvos localmente no computador, mantendo o histórico intacto entre execuções do aplicativo.

---

## 12. Como Funciona o Sistema de Progresso

Na tela **📊 Progresso**, o estudante acompanha:

- Total geral de tentativas realizadas;
- Quantidade e percentual geral de acertos e erros;
- Tabela analítica com o aproveitamento individual em cada uma das 10 atividades;
- Lista histórica de todas as tentativas anteriores com data e detalhamento.
- Botão para reiniciar/limpar as estatísticas de estudo se desejar começar uma nova rodada de práticas.

---

## 13. Limitações Atuais

- **Base de Conteúdo Focada:** O conhecimento e as respostas estão restritos exclusivamente aos Módulos 1 e 2 da Mentoria. Perguntas fora desse domínio acadêmico retornarão a mensagem padrão de não localização.
- **Execução Monousuário Local:** O banco SQLite foi desenhado para uso individual na máquina local do aluno.
- **Dependência de Ambiente Gráfico:** O aplicativo requer ambiente com suporte a interface gráfica no Windows 11.

---

## 14. Possíveis Melhorias Futuras

- Inclusão de conteúdos e exercícios dos Módulos 3, 4 e seguintes da Mentoria;
- Exportação de casos de teste e defeitos em formato PDF, Excel ou JSON para importação no Jira/Zephyr;
- Modo escuro (Dark Mode) nativo alternável nas configurações;
- Temporizador de sessões para apoiar a execução prática do método SBTM em tempo real.
