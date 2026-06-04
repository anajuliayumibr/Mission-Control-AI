# Mission Control AI
GS2026.1 —> Pensamento Computacional e Automação com Python  

Objetivo: Programa em Python que simule um sistema básico de controle de missão espacial.

### Missão: **Astra Polaris**

## *Equipe:* 

Ana Julia Yumi Inoue - RM: 569430

João Pedro Santos Ferreira - RM: 569202

Maria Fernanda Dias Ribeiro - RM: 569999


Descrição
----------

O Mission Control AI é um sistema em Python que simula o monitoramento inteligente de uma missão espacial experimental. Ele analisa ciclos de dados simulados: temperatura, comunicação, bateria, oxigênio e estabilidade e gera alertas automáticos, calcula o risco de cada ciclo e apresenta um relatório final completo no terminal.



---

Como executar
---------------
Nenhuma biblioteca externa é necessária, apenas ter o Python 3 instalado. 

---

Estrutura dos dados
--------------------

A missão é representada por uma matriz chamada `dados_missao`.

Cada linha corresponde a um ciclo e cada coluna guarda uma informação específica: temperatura (°C), comunicação (%), bateria (%), oxigênio (%) e estabilidade (%).

A missão Astra Polaris possui 8 ciclos, cobrindo desde o lançamento até a estabilização após uma crise.


-----------------
Regras de alerta!!!!
-----------------
---------------------
* TEMPERATURA:

1) abaixo de 18 °C ou acima de 30 °C exige atenção;

2) acima de 35 °C é considerado crítico.

---------------
* COMUNICAÇÃO:

1) sinais abaixo de 30% são críticos;

2) entre 30% e 59% exigem atenção;

3) acima de 60% são normais.

---------------
* BATERIA:

1) menos de 20% é crítico;

2) entre 20% e 49% exige atenção;

3) acima de 50% é normal.

----------------
* OXIGÊNIO:

1) abaixo de 80% é crítico;

2) entre 80% e 89% exige atenção;

3) acima de 90% é normal.

----------------
* ESTABILIDADE:

1) abaixo de 40% é crítico; 

2) entre 40% e 69% exige atenção; 

3) acima de 70% é normal.

---------------------
 Pontuação de risco
---------------------
* Cada condição normal vale 0 pontos, atenção vale 1 ponto e crítico vale 2 pontos.
A soma máxima por ciclo é de 10 pontos.

* Ciclos com até 2 pontos são considerados estáveis.

* Entre 3 e 5 pontos, a missão está em atenção.

* De 6 a 10 pontos, a missão entra em estado crítico.

-----------------------
 Funções implementadas
 ----------------------

FUNÇÃO e DESCRIÇÃO

`analisar_temperatura()`     =      Classifica a temperatura do módulo 

`analisar_comunicacao()`     =      Classifica a qualidade do sinal

`analisar_bateria()`         =      Classifica o nível de bateria 

`analisar_oxigenio()`        =      Classifica o nível de oxigênio 

`analisar_estabilidade()`    =      Classifica a estabilidade dos sistemas 

`calcular_risco_ciclo()`     =      Calcula a pontuação total do ciclo 

`classificar_ciclo()`        =      Retorna o status do ciclo pela pontuação 

`gerar_recomendacao()`       =      Gera recomendações automáticas por ciclo 

`analisar_tendencia()`       =      Compara o risco do 1º e último ciclos 

`identificar_area_mais_afetada()`  = Soma risco acumulado por área 

`identificar_area_mais_afetada()`  = Soma risco acumulado por área 

`exibir_ciclos()`                  = Exibe a análise detalhada de cada ciclo 

`gerar_relatorio_final()`          = Exibe o relatório consolidado da missão 
