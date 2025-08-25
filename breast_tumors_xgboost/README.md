<h1 style="color:blue;">Classificação de tumores de mama com XGBoost</h1>

<img width="1019" height="526" alt="image" src="https://github.com/user-attachments/assets/7f69f940-bf5d-4e35-bc89-9b9c0b61c985" />

# Índice
Justificativa para não aplicar transformação logarítmica nos outlie
- [1. Objetivo](#1-objetivo)
- [2. Contexto](#2-contexto)
- [3. Etapas do Projeto](#3-etapas-do-projeto)
- [4. Tratamento dos outliers](#4-justificativa-para-nao-aplicar-transformacao-logaritmica-nos-outliers)
- [5. Resultados](#5-resultados)
  - [Principais variáveis para previsão](#principais-variáveis-para-previsão)
  - [Significado das colunas](#significado-das-colunas)
  - [Principais colunas](#principais-colunas)
- [6. Insights do Modelo](#6-insights-do-modelo)
- [7. Insights de Aplicabilidade](#7-insights-de-aplicabilidade)


### 1. Objetivo

Desenvolver um modelo de *machine learning* capaz de classificar tumores de mama como malignos ou benignos com alta acurácia, utilizando o algoritmo **XGBoost**.  
A ideia é mostrar como um modelo de *ensemble* pode ser aplicado a problemas de saúde, auxiliando na detecção precoce do câncer de mama.

#### [🔝 Voltar ao índice](#índice)
---

### 2. Contexto
O câncer de mama é uma das principais causas de morte entre mulheres em todo o mundo. A detecção precoce é essencial para aumentar as chances de tratamento eficaz. Este projeto utiliza o **Breast Cancer Wisconsin Dataset**, amplamente usado na comunidade científica para testar modelos de classificação.

#### [🔝 Voltar ao índice](#índice)
---

### 3. Etapas do Projeto
- Coleta e carregamento dos dados — uso do dataset `load_breast_cancer` do scikit-learn.  
- Análise exploratória — visualização das distribuições e correlações entre variáveis.  
- Divisão treino/teste — 80% dos dados para treino, 20% para teste.  
- Treinamento do modelo — aplicação do XGBoost.  
- Avaliação do modelo — cálculo de *accuracy*, *precision*, *recall* e *F1-score*.  
- Interpretação dos resultados — identificação das variáveis mais importantes.  
- Conclusões — análise do impacto das variáveis e aplicabilidade do modelo.  

#### [🔝 Voltar ao índice](#índice)
---

### 4. Justificativa para não aplicar transformação logarítmica nos outliers

Neste projeto, a análise exploratória mostrou que variáveis como **`area_error`** e **`radius_error`** apresentam valores considerados outliers.  
Em muitos cenários de *machine learning*, uma prática comum seria aplicar transformações como o logaritmo natural (`np.log1p`) para reduzir a assimetria e suavizar o impacto desses valores extremos.

No entanto, optou-se por **não realizar essa transformação** neste caso, pelos seguintes motivos:

#### 1. Significado clínico dos outliers
- Os valores extremos podem representar **pacientes com tumores maiores ou mais irregulares**, ou seja, casos clinicamente relevantes.  
- Aplicar log reduziria a magnitude desses valores, podendo **atenuar sinais importantes para o diagnóstico**.  

---

#### 2. Capacidade do XGBoost em lidar com outliers
- O **XGBoost** é um algoritmo baseado em **árvores de decisão**, que cria divisões por meio de **limiares (thresholds)**.  
- Isso torna o modelo **menos sensível a escala e assimetria**, dispensando a necessidade de normalizações ou transformações logarítmicas.  

---

#### 3. Resultados experimentais
O modelo treinado **sem a transformação logarítmica** apresentou métricas muito altas:  

- **Recall = 0.96** para a classe positiva (câncer), garantindo que a maioria dos casos de câncer sejam identificados.  
- **ROC AUC = 0.994**, indicando separação quase perfeita entre as classes.  

Esses resultados demonstram que os outliers não prejudicaram o desempenho; pelo contrário, foram **bem absorvidos pelo modelo**.  

---

#### 4. Priorização do Recall
- Em diagnósticos médicos, o **recall é crítico**: um falso negativo pode ter consequências graves.  
- A suavização dos outliers poderia **reduzir a sensibilidade do modelo** em relação a casos extremos de câncer, diminuindo sua capacidade de detecção.  

#### [🔝 Voltar ao índice](#índice)
---

### 5. Resultados

<img width="373" height="305" alt="image" src="https://github.com/user-attachments/assets/ad202644-8c74-4b19-a9c0-f8ba130c76a2" />

#### Classe 0 (Sem câncer)
- **Precision = 0.93** → 93% dos pacientes classificados como “sem câncer” realmente não têm.  
- **Recall = 0.95** → o modelo consegue identificar 95% dos casos benignos corretamente.  

#### Classe 1 (Com câncer)
- **Precision = 0.97** → quase nenhum falso positivo (ótimo do ponto de vista clínico).  
- **Recall = 0.96** → o mais importante: o modelo detecta **96% dos casos de câncer**.  

#### Métricas gerais
- **Acurácia = 0.96** → desempenho geral altíssimo.  
- **ROC AUC = 0.994** → separação quase perfeita entre classes.  

#### Principais variáveis para previsão
Características relacionadas ao formato e tamanho do tumor, como:  
- **mean concave points**  
- **worst concave points**  
- **worst area**  

#### Significado das colunas
O dataset possui 30 variáveis numéricas derivadas da análise digital de imagens de massas mamárias obtidas por biópsia.  
Cada variável representa uma característica geométrica ou textural da célula tumoral.  
As medidas foram calculadas de três formas:  

- **mean** (média)  
- **se** (erro padrão)  
- **worst** (maior valor observado)  

#### Principais colunas:

| Feature              | Descrição                                                                   |
|-----------------------|-----------------------------------------------------------------------------|
| **radius**           | Distância média do centro até o perímetro do tumor                          |
| **texture**          | Variação da intensidade de cinza da imagem                                  |
| **perimeter**        | Comprimento do contorno do tumor                                            |
| **area**             | Área ocupada pelo tumor                                                     |
| **smoothness**       | Variação no comprimento dos raios, indicando irregularidade da superfície   |
| **compactness**      | Relação entre perímetro e área, medindo a compacidade                       |
| **concavity**        | Grau de concavidade em partes do contorno                                   |
| **concave points**   | Número de pontos côncavos no contorno                                       |
| **symmetry**         | Simetria da forma                                                           |
| **fractal dimension**| Complexidade do contorno                                                    |

#### Variável alvo
- **0 → Maligno**  
- **1 → Benigno**  

#### [🔝 Voltar ao índice](#índice)
---

### 6. Insights do Modelo

1. **Alto Desempenho Preditivo**  
   - O modelo atingiu **96% de acurácia** e alto **recall para tumores malignos**, mostrando-se muito eficaz em identificar casos de câncer e reduzindo os **falsos negativos** (o risco mais crítico em diagnósticos médicos).  
   - Isso sugere que o XGBoost é uma ótima escolha para problemas de saúde em que a **segurança do paciente** é prioridade.

<img width="382" height="300" alt="image" src="https://github.com/user-attachments/assets/007a6e5a-11bb-4f9e-8731-5561bd92721b" />

2. **Variáveis Mais Importantes**  
   - As principais variáveis preditivas estão relacionadas a **formato e tamanho do tumor**:  
     - **Mean concave points**  
     - **Worst concave points**  
     - **Worst area**  
     - **Mean concavity**  
     - **Worst radius**  
   - Isso indica que **irregularidades no contorno do tumor** e **dimensões do tumor** são fatores críticos na detecção de malignidade.  

3. **Interpretação Clínica**  
   - Tumores malignos tendem a apresentar **bordas mais irregulares e formas menos uniformes**, refletidas nos pontos côncavos.  
   - Tumores maiores e mais agressivos costumam apresentar valores mais altos de **área** e **raio**.  
   - Portanto, o modelo reforça achados já conhecidos na literatura médica, aumentando sua credibilidade.  

#### [🔝 Voltar ao índice](#índice)
---

### 7. Insights de Aplicabilidade

1. **Suporte à Decisão Clínica**  
   - O modelo pode ser utilizado como uma **ferramenta de apoio à decisão** para médicos, auxiliando no rastreamento inicial e na priorização de exames mais detalhados.  

2. **Interpretabilidade do Modelo**  
   - O XGBoost permite interpretar a importância das variáveis, o que é crucial em aplicações médicas, onde o “porquê” da decisão é quase tão importante quanto a decisão em si.  

3. **Potencial de Integração**  
   - O modelo poderia ser integrado em **sistemas hospitalares** para análise automática de dados de exames, ajudando a reduzir o tempo de diagnóstico e aumentando as taxas de detecção precoce.  

#### [🔝 Voltar ao índice](#índice)
---

