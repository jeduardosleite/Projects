# 📑 Sumário

- [1. Contexto](#1-contexto)
- [2. Conjunto de dados](#2-conjunto-de-dados)
  - [Dicionário de dados](#dicionário-de-dados)
  - [Variáveis do Conjunto de Dados](#variáveis-do-conjunto-de-dados)
- [3. Objetivo](#3-objetivo)
- [4. Ferramentas e tecnologias](#4-ferramentas-e-tecnologias)
- [5. CRISP-DM](#5-crisp-dm)
- [6. Análise Exploratória de Dados (EDA)](#6-análise-exploratória-de-dados-eda)
  - [Visão Geral do Conjunto de Dados](#i-visão-geral-do-conjunto-de-dados)
  - [Verificação da Qualidade dos Dados](#ii-verificação-da-qualidade-dos-dados)
  - [Distribuição das Variáveis Numéricas](#iii-distribuição-das-variáveis-numéricas)
  - [Distribuição das Variáveis Binárias](#iv-distribuição-das-variáveis-binárias)
  - [Fraudes vs. Transações Legítimas](#v-fraudes-vs-transações-legítimas)
  - [Principais Insights para Modelagem](#vi-principais-insights-para-modelagem)
- [7. Dificuldades](#7-dificuldades)
- [8. Estimativa de ganho financeiro](#8-estimativa-de-ganho-financeiro)
- [9. Fluxograma e Ações Corretivas](#9-fluxograma-e-ações-corretivas)
- [10. Baixando o Arquivo](#10-baixando-o-arquivo)

#### Contate-me: https://www.linkedin.com/in/jos%C3%A9-eduardo-souza-leite/

# Caso de Prevenção a Fraudes em Transações com Cartão de Crédito

<img width="830" height="449" alt="image" src="https://github.com/user-attachments/assets/97c3994d-8ed2-4452-80d1-2f47596da794" />

## 1. Contexto

A empresa está enfrentando um aumento significativo de transações fraudulentas com cartões de crédito, o que prejudica a confiança dos clientes e causa perdas financeiras. Sua tarefa é desenvolver um modelo preditivo que possa identificar transações fraudulentas com alta precisão, minimizando assim o impacto financeiro e protegendo a reputação da instituição.

[🔝 Voltar ao topo](#-sumário)
---

## 2. Conjunto de dados:

### Dicionário de dados

Descrição das colunas do conjunto de dados utilizadas para detecção de fraudes em transações.

#### Variáveis do Conjunto de Dados

| Variável                       | Tipo          | Descrição                                                                 |
|--------------------------------|---------------|---------------------------------------------------------------------------|
| **distance_from_home**         | float         | Distância (em unidades arbitrárias) entre o local da compra e a residência do cliente. |
| **distance_from_last_transaction** | float     | Distância entre a transação atual e a última transação registrada do mesmo cliente. |
| **ratio_to_median_purchase_price** | float     | Razão entre o valor da compra atual e o valor mediano das compras anteriores do cliente. |
| **repeat_retailer**            | float (0 ou 1) | Indica se a transação foi realizada em um varejista já utilizado anteriormente pelo cliente. |
| **used_chip**                  | float (0 ou 1) | Indica se a transação foi realizada utilizando o chip do cartão. |
| **used_pin_number**            | float (0 ou 1) | Indica se a transação exigiu a digitação da senha (PIN) do cliente. |
| **online_order**               | float (0 ou 1) | Indica se a transação foi realizada online (1) ou presencialmente (0). |
| **fraud**                      | float (0 ou 1) | Variável alvo: identifica se a transação foi fraudulenta (1) ou legítima (0). |

[🔝 Voltar ao topo](#-sumário)
---

## 3. Objetivo

O objetivo deste projeto é desenvolver, avaliar e validar modelos de aprendizado de máquina capazes de detectar transações fraudulentas de cartão de crédito com **alta precisão e recall**.  

O trabalho envolve:  
- Pré-processamento dos dados (engenharia de atributos, normalização e tratamento de desbalanceamento de classes).  
- Treinamento de modelos de classificação com **Gradient Boosting (XGBoost)**.  
- Avaliação com métricas: **ROC-AUC, precisão, recall, F1-score** e **matriz de confusão**.  

O objetivo final é criar uma solução **robusta e escalável**, aplicável em sistemas financeiros reais, reduzindo perdas econômicas e aumentando a confiança dos clientes.

[🔝 Voltar ao topo](#-sumário)
---

## 4. Ferramentas e tecnologias
As ferramentas e tecnologias que usei foram:
  - Python (pandas, numpy, math, shap, matplotlib, seaborn, plotly, XGBoost, sklearn);
  - Jupyter Notebook;
  - Git and Git/Hub;
  - Anaconda (terminal);
  - Machine Learning;
  - Conceitos de estatística.

[🔝 Voltar ao topo](#-sumário)
---

## 5. CRISP-DM

Pipeline baseada no framework **CRISP-DM**:

1. **Definir o problema de negócio.**  
2. **Coletar os dados e obter uma visão geral.**  
3. **Dividir os dados em treino e teste.**  
4. **Explorar os dados (EDA).**  
5. **Engenharia de atributos, limpeza e pré-processamento.**  
6. **Treinamento, comparação, seleção de variáveis e ajuste de hiperparâmetros.**  
7. **Teste e avaliação do modelo final.**  
8. **Conclusão e interpretação dos resultados.**  
9. **Implantação (deploy).**

[🔝 Voltar ao topo](#-sumário)
---

## 6. Análise Exploratória de Dados (EDA)

### I) Visão Geral do Conjunto de Dados
- Total de registros: **1.000.000 transações**  
- Variável alvo: **fraud** (0 = legítima, 1 = fraudulenta)  
- Variáveis analisadas:  
  - **Numéricas:** distance_from_home, distance_from_last_transaction, ratio_to_median_purchase_price  
  - **Binárias/Categóricas:** repeat_retailer, used_chip, used_pin_number, online_order  

---

### II) Verificação da Qualidade dos Dados
- Nenhum valor ausente.  
- Outliers identificados:  
  - distance_from_home → 10,36%  
  - ratio_to_median_purchase_price → 8,44%  
  - repeat_retailer → 11,86%  
  - distance_from_last_transaction → 12,43%  
  - used_pin_number → 10,07%  
- Variáveis **used_chip** e **online_order** → sem outliers.  

---

### III) Distribuição das Variáveis Numéricas
- **distance_from_home:** assimetria à direita, valores concentrados próximos a zero, alguns casos extremos.  
- **distance_from_last_transaction:** padrão semelhante, com cauda longa.  
- **ratio_to_median_purchase_price:** maioria próxima de 1, mas outliers com valores anormais.  

---

### IV) Distribuição das Variáveis Binárias
- **repeat_retailer:** ~12% anomalias (uso incomum de varejistas).  
- **used_chip:** distribuição equilibrada.  
- **used_pin_number:** ~10% anomalias (uso irregular do PIN).  
- **online_order:** distribuição equilibrada (0 = presencial, 1 = online).  

---

### V) Fraudes vs. Transações Legítimas
- Fraudes são **raras** (dataset altamente desbalanceado).  
- Visualizações iniciais:  
  - Gráfico de dispersão (`distance_from_home` vs `distance_from_last_transaction`) mostra agrupamentos de fraudes.  
  - Anomalias de preço (`ratio_to_median_purchase_price`) + distância → fortes sinais de fraude.  

---

### VI) Principais Insights para Modelagem
- **Preditores fortes:** distance_from_home, distance_from_last_transaction, ratio_to_median_purchase_price.  
- **Variáveis binárias (used_pin_number, online_order):** bons separadores entre fraude e legítimo.
- **Necessário tratamento do desbalanceamento (ex.: SMOTE).**  

[🔝 Voltar ao topo](#-sumário)
---

## 7. Dificuldades
Durante a fase de Análise Exploratória de Dados (EDA), foram identificados desafios críticos relacionados a outliers, desbalancemento de classes e data leakage. O comportamento atípico dos dados, bem como a suspeita de um vazamento que inflava as métricas de desempenho do modelo, exigiu uma investigação aprofundada.

<img width="330" height="301" alt="image" src="https://github.com/user-attachments/assets/90198d18-4a7e-48c2-ba0d-c96c8c4ae88f" />

<img width="426" height="254" alt="image" src="https://github.com/user-attachments/assets/2c2cd13e-7406-40bc-a47c-6b6ac665c839" />


A solução não se limitou a um simples ajuste; foi necessário um aprofundamento nos conceitos de pré-processamento e validação de modelo. A pesquisa em diversas fontes — como documentações de bibliotecas, comunidades online e tutoriais — foi essencial para compreender a raiz dos problemas e implementar correções. Este processo de depuração não apenas resolveu a questão da métrica inflada, mas também solidificou a integridade metodológica do projeto, garantindo que os resultados finais são uma representação fiel do desempenho do modelo.

[🔝 Voltar ao topo](#-sumário)
---

## 8. Estimativa de ganho financeiro

### Cenário estimado com ticket médio real (com base em dados da Serasa Experian)

- **Ticket médio mensal estimado**: **R$ 1.416,58**  
  Fonte: Serasa Experian – levantamento "Cadastro Positivo: Brasileiro tem gasto médio de R$ 1.416,58 no cartão de crédito" ('https://www.infomoney.com.br/minhas-financas/brasileiro-gasta-r-14-mil-por-mes-com-cartao-de-credito-diz-serasa-experian/')
  
Cálculos (com TP = 17.477 e FN = 4):

- **Perda sem modelo**: (17.481 fraudes) × R$ 1.416,58 ≈ **R$ 24.768.694,98**  
- **Perda com modelo**: 4 fraudes × R$ 1.416,58 = **R$ 5.666,32**  
- **Ganho estimado (economia)**: **≈ R$ 24.763.028,66**

 Esses valores são estimativas baseadas em ticket médio real e úteis para contextualizar o impacto financeiro do modelo mesmo sem dados individuais de valor de transação no dataset.

[🔝 Voltar ao topo](#-sumário)
 ---

 ## 9. Fluxograma e Ações Corretivas

<img width="442" height="663" alt="image" src="https://github.com/user-attachments/assets/e9dbe346-7e2d-44c7-9fd9-bb05aa7c5834" />

 ## 1️⃣ Desvios no histórico de gastos (`ratio_to_median_purchase_price_log`) 
- **Insight:** Compras muito acima ou abaixo da média histórica do cliente indicam forte risco de fraude.  
- **Ação recomendada:**  
  - Alertas automáticos para transações fora do padrão histórico.  
  - Revisão manual ou validação adicional para compras com valores atípicos.

---

## 2️⃣ Compras online (`online_order`)
- **Insight:** Fraudes são mais comuns em transações online do que físicas.  
- **Ação recomendada:**  
  - Autenticação adicional em pedidos online (ex.: SMS, e-mail).  
  - Bloqueio temporário ou revisão manual de compras suspeitas.

---

## 3️⃣ Localização das transações
- **Insight:** Compras realizadas longe da residência ou da última transação aumentam o risco.  
- **Ação recomendada:**  
  - Monitorar padrões geográficos de cada cliente.  
  - Gerar alertas para transações fora das áreas habituais.

---

## 4️⃣ Segurança do cartão
- **Insight:** Fraudes tendem a ocorrer quando o chip ou o PIN não são utilizados.  
- **Ação recomendada:**  
  - Incentivar ou exigir o uso de chip e PIN, principalmente em compras online.

---

## 5️⃣ Histórico de compras em uma loja (`repeat_retailer`)
- **Insight:** Pouco relevante para prever fraude.  
- **Ação recomendada:**  
  - Nenhuma ação específica necessária; foco em outros fatores mais críticos.

[🔝 Voltar ao topo](#-sumário)

---

## 10. Baixando o arquivo
O arquivo `fraud_dataset.csv` é grande (~80 MB) e está armazenado via **Git LFS**.  
Para garantir que o arquivo seja baixado corretamente, siga estas instruções:

#### 1️⃣ Instale o Git LFS
- **Windows**: [https://git-lfs.github.com/](https://git-lfs.github.com/)  
- **macOS**: `brew install git-lfs`  
- **Linux**: `sudo apt install git-lfs`

#### 2️⃣ Inicialize o Git LFS (uma vez)
git lfs install

#### 3️⃣ Clone o repositório
git clone https://github.com/jeduardosleite/Projects.git

cd Projects/fraud_credit

#### 4️⃣ Baixe os arquivos grandes via LFS
git lfs pull

Agora o arquivo fraud_dataset.csv estará disponível para uso no projeto.

⚠️ Lembre-se: é necessário ter o Git LFS instalado para baixar corretamente o CSV.
Caso não tenha o LFS, o arquivo aparecerá apenas como um ponteiro de texto.

### Opção alternativa
Acesse o link do arquivo bruto, cole numa planilha excel e salve como CSV.
https://raw.githubusercontent.com/alura-cursos/youtube-alura/refs/heads/main/fraud_dataset.csv


[🔝 Voltar ao topo](#-sumário)

