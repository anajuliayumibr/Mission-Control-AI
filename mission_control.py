# MISSION CONTROL AI
# GS2026.1 - Pensamento Computacional e Automação com Python

#Integrantes:
# Ana Julia Yumi Inoue - RM: 569430
#João Pedro Santos Ferreira - RM: 569202
#Maria Fernanda Dias Ribeiro - RM: 569999

# --- INFORMAÇÕES DA MISSÃO ---
nome_missao = "Astra Polaris"
nome_equipe = "Equipe Polaris - Ana Julia, João Pedro e Maria Fernanda"

# Matriz principal: cada linha = 1 ciclo
# Ordem das colunas: [temperatura, comunicacao, bateria, oxigenio, estabilidade]
dados_missao = [
    [21, 94, 91, 96, 99],  # Ciclo 01 - Lançamento e estabilização inicial
    [27, 83, 75, 95, 88],  # Ciclo 02 - Ajuste de trajetória
    [30, 66, 60, 92, 71],  # Ciclo 03 - Interferência solar leve
    [36, 45, 40, 88, 58],  # Ciclo 04 - Falha parcial no painel de energia
    [41, 20, 17, 75, 32],  # Ciclo 05 - Tempestade de partículas - risco crítico
    [33, 58, 35, 83, 52],  # Ciclo 06 - Protocolo de recuperação ativado
    [29, 72, 47, 88, 62],  # Ciclo 07 - Recuperação parcial dos sistemas
    [23, 88, 63, 93, 78],  # Ciclo 08 - Estabilização pós-crise
]

# Lista de áreas monitoradas
areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

# FUNÇÕES DE ANÁLISE -----------------------------------

def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1, "Temperatura abaixo do ideal"
    elif valor <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif valor <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"

def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2, "Comunicação em nível crítico"
    elif valor < 60:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"

def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif valor < 50:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"

def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif valor < 90:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"

def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2, "Estabilidade crítica"
    elif valor < 70:
        return "ATENÇÃO", 1, "Estabilidade reduzida"
    else:
        return "NORMAL", 0, "Estabilidade adequada"


# FUNÇÕES DE LÓGICA DA MISSÃO -----------------------------------------

def calcular_risco_ciclo(ciclo):
    temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo
    _, pontos_temp, _ = analisar_temperatura(temperatura)
    _, pontos_com, _ = analisar_comunicacao(comunicacao)
    _, pontos_bat, _ = analisar_bateria(bateria)
    _, pontos_ox, _ = analisar_oxigenio(oxigenio)
    _, pontos_est, _ = analisar_estabilidade(estabilidade)
    return pontos_temp + pontos_com + pontos_bat + pontos_ox + pontos_est

def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"

def gerar_recomendacao(ciclo):
    temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo
    recomendacoes = []
    if temperatura > 35:
        recomendacoes.append("Verificar controle térmico")
    if comunicacao < 30:
        recomendacoes.append("Restabelecer contato com a base")
    if bateria < 20:
        recomendacoes.append("Ativar modo de economia de energia")
    if oxigenio < 80:
        recomendacoes.append("Acionar protocolo de suporte à vida")
    if estabilidade < 40:
        recomendacoes.append("Reduzir operações não essenciais")
    if not recomendacoes:
        return "Manter operação normal e continuar monitoramento."
    return "Ação necessária: " + ", ".join(recomendacoes) + "."


# EXIBIÇÃO DOS CICLOS -------------------------------------

def exibir_ciclos():
    riscos = []
    for i, ciclo in enumerate(dados_missao):
        temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo
        status_temp, _, desc_temp = analisar_temperatura(temperatura)
        status_com, _, desc_com = analisar_comunicacao(comunicacao)
        status_bat, _, desc_bat = analisar_bateria(bateria)
        status_ox, _, desc_ox = analisar_oxigenio(oxigenio)
        status_est, _, desc_est = analisar_estabilidade(estabilidade)
        pontuacao = calcular_risco_ciclo(ciclo)
        classificacao = classificar_ciclo(pontuacao)
        recomendacao = gerar_recomendacao(ciclo)
        riscos.append(pontuacao)

        print("\n" + "=" * 55)
        print(f" CICLO {i+1}")
        print("=" * 55)
        print(f" Temperatura : {temperatura} °C | {status_temp} | {desc_temp}")
        print(f" Comunicação : {comunicacao}%   | {status_com} | {desc_com}")
        print(f" Bateria     : {bateria}%   | {status_bat} | {desc_bat}")
        print(f" Oxigênio    : {oxigenio}%   | {status_ox} | {desc_ox}")
        print(f" Estabilidade: {estabilidade}%   | {status_est} | {desc_est}")
        print("-" * 55)
        print(f" Pontuação de risco : {pontuacao}")
        print(f" Classificação      : {classificacao}")
        print(f" Recomendação       : {recomendacao}")
    return riscos

# ============================================================
# RELATÓRIO FINAL
# ============================================================

def gerar_relatorio_final(riscos):
    num_ciclos = len(dados_missao)
    risco_medio = sum(riscos) / num_ciclos
    ciclo_critico = riscos.index(max(riscos)) + 1
    classificacao_final = classificar_ciclo(round(risco_medio))
    print("\n" + "=" * 55)
    print(" RELATÓRIO FINAL DA MISSÃO")
    print("=" * 55)
    print(f" Missão : {nome_missao}")
    print(f" Equipe : {nome_equipe}")
    print(f" Ciclos : {num_ciclos}")
    print(f" Risco médio : {risco_medio:.2f}")
    print(f" Ciclo mais crítico : {ciclo_critico}")
    print(f" Classificação final : {classificacao_final}")
    print("=" * 55)

# ============================================================
# EXECUÇÃO PRINCIPAL
# ============================================================

print("=" * 55)
print(" MISSION CONTROL AI")
print("=" * 55)
print(f" Missão : {nome_missao}")
print(f" Equipe : {nome_equipe}")
print(f" Ciclos : {len(dados_missao)}")
print("=" * 55)

riscos = exibir_ciclos()
gerar_relatorio_final(riscos)
