## Vamos nos conectar:
[Linkedin](https://www.linkedin.com/in/jeduardosleite/)
---

---

<img width="527" height="342" alt="image" src="https://github.com/user-attachments/assets/5a0247af-8042-44a5-8983-1bcfc05f548c" />


# Objetivo

Predizer o valor do contrato com base em variáveis socioeconômicas e comportamentais utilizando a regressão linear. 

```Regressão linear``` é uma técnica estatística usada para modelar e prever a relação entre uma variável dependente (Y) e uma ou mais variáveis independentes (X), assumindo que essa relação pode ser representada por uma linha reta.

# Etapas

## 1) Entendendo o problema
Para este tipo de problema, utilizarei o **aprendizado supervisionado**, aquele em que o modelo aprende a partir de ```dados rotulados```. Existe uma variável alto(*target*) que queremos prever, neste caso, é a ```charges```. Para explicar essa variável, temos: idade, sexo, IMC, número de filhos, região e tabagismo.

Para as **métricas de avaliação**, usarei as seguintes:

- **MAE** (*Mean Absolute Error*): mede o erro médio absoluto entre os valores previstos e reais. Indica, em média, quanto o modelo erra em unidades reais (ex.: reais). Quanto menor o MAE, menor é o erro médio das previsões.
    
- **RMSE** (*Root Mean Squared Error*): mede a raiz do erro quadrático médio, penalizando mais fortemente erros grandes. É indicada quando erros elevados têm maior impacto. Quanto menor o RMSE, melhor o modelo em evitar grandes erros.
    
- **R²** (*Coeficiente de Determinação*): indica a proporção da variabilidade dos dados explicada pelo modelo. Varia geralmente entre 0 e 1 e é útil para comparar o desempenho geral entre modelos.


O ```MAE``` foi adotado como métrica principal por indicar diretamente o erro médio na previsão do valor do plano, alinhando-se ao objetivo do modelo de estimar o custo do contrato de forma clara e interpretável.


## 2) Dataset

Este conjunto de dados contém informações sobre a relação entre atributos pessoais (idade, sexo, IMC, tamanho da família, tabagismo), fatores geográficos e seu impacto nos custos do seguro saúde.

| Variável   | Descrição                                                                 |
|------------|---------------------------------------------------------------------------|
| age      | A idade da pessoa segurada.                                                |
| sex       | Gênero (masculino ou feminino) do segurado.                                |
| bmi        | Índice de Massa Corporal, medida da gordura corporal baseada em peso e altura. |
| children     | Número de dependentes abrangidos pelo seguro.                              |
| smoker    | Indica se o segurado é fumante (sim ou não).                               |
| region     | Área geográfica de cobertura do seguro.                                   |
| charges   | Custos do seguro de saúde incorridos pela pessoa segurada.                |

Para facilitar a interpretação do *BMI* (Índice de Massa Corporal), serão aplicados rótulos que indicam a faixa em que cada valor se enquadra. Inicialmente, essa categorização será utilizada apenas para fins de análise e explicação do negócio, sem a decisão prévia de incluí-la no treinamento do modelo. Ao longo do desenvolvimento do projeto, será avaliada a real necessidade dessa variável com base em seu impacto no desempenho do modelo.

| Faixa de BMI (kg/m²) | Descrição         |
|----------------------|-------------------|
|< 18,5                | Magreza           |
| 18,5 – 24,9          | Normal            |
| 25,0 – 29,9          | Sobrepeso         |
| 30,0 – 39,9          | Obesidade         |
| ≥ 40,0               | Obesidade grave   |

fonte: https://abran.org.br/calculadoras/imc

## 3) EDA (Análise Explanatória de Dados)
1) Verificar os valores nulos, faltantes e a dimensão do dataset;
2) Estatística descritiva (média, mediana, dispersão, quartis etc);
3) Análise de correlação entre as variáveis;
4) Identificação outliers.

## 4) Pré-processamento dos dados
Nesta etapa, será realizada a análise e o tratamento de *outliers*, caso necessário. Em seguida, será feita uma avaliação mais aprofundada das variáveis, com o objetivo de definir quais serão utilizadas no modelo, bem como identificar a necessidade de aplicação de técnicas de *feature engineering* e quais delas serão mais adequadas.

Ao final, será realizada a sepação em treino e teste.

## 5) Modelagem
Com a base separada, está na hora de treinar e comparar diferentes modelos de regressão linear para identificar qual apresenta o melhor desempenho na previsão do valor do plano, considerando erro, estabilidade e capacidade de generalização.

## 6) Avaliação
Após o treinamento, os modelos serão avaliados para verificar qual generaliza melhor para os dados não vistos. Lembrando que a métrica principal será a ```MAE```, porém o *R²* e o *RMSE* serão avaliados também.

## 7) Interpretação dos resultados

# Conclusões do modelo de teste

No conjunto de teste, o modelo apresentou `R²` de 0.8187, explicando aproximadamente 82% dos custos médicos. As métricas `MAE` e `RMSE` indicam erro médio controlado e comportamento consiste. Embora a análise dos resíduos evidencie *heterocedasticidade*, isso não compromete a capacidade preditiva do modelo.

## Insights para o negócio

A interpretação dos coeficientes na escala logarítmica permite traduzir diretamente o modelo em variações percentuais de preço, facilitando sua aplicação em estratégias de pricing baseadas em risco.

| Variável         | Coef.       | Impacto no pricing                    |
| ---------------- | ----------- | ------------------------------------- |
| **age**          | 0.0416      | **+4.25% por ano**                    |
| **bmi_smoker**   | 0.0490      | **+5.03% por ponto de BMI (fumante)** |
| **age_smoker**   | -0.0334     | **−3.28% por ano (fumante)**          |
| **children_1-2** | 0.2110      | **+23.5%**                            |
| **children_3+**  | 0.3107      | **+36.5%**                            |
| **smoker_yes**   | 1.3621      | **+290.5%**                           |
| **sex_male**     | -0.0845     | **−8.1%**                             |

### `smoker_yes`
É o eixo central da predição, aumenta em quase 300% o custo.

### `age`(não fumante)
Aumento de 4,25% por ano.

### `bmi`(fumantes)
A interação de *bmi* com *smoker* foi determinante para esta variável, visto que ela só é relevante quando o cliente é fumante. Aumento de 5%.

### `age_smoker` (fumante)
Enquanto a idade eleva os custos em aproximadamente 4,2% ao ano entre **não fumantes**, esse aumento cai para cerca de *0,8%* ao ano entre fumantes, evidenciando que o risco associado à idade é condicionado ao tabagismo.
O valor de 0,82% vem da soma dos coeficientes $ 0.0416 + (-0.0334) $. Isso acontece porque o `age_smoker` é um ajuste condicional, não o efeito total.

### `filhos`
Quanto mais filhos, maior o custo. Indivíduos sem filhos constituem a categoria de referência do modelo e não apresentam acréscimo no custo estimado. Em comparação, pessoas com 1 ou 2 filhos possuem um custo aproximadamente *23,5%* maior, enquanto aquelas com três ou mais filhos apresentam um aumento médio de cerca de *36,4%*.

### `sex_male`
Clientes **masculinos** custam aproximadamente 8% a menos que o **feminino**.

## 8) Aprendizado
Ao longo deste projeto, obtive aprendizados técnicos e pessoais relevantes. Inicialmente, ficou claro que modelar a target charges sem qualquer tipo de tratamento resultava em métricas inconsistentes e padrões inadequados nos resíduos. A partir disso, pesquisei e testei alternativas, chegando à **transformação logarítmica** como uma solução eficaz para estabilizar a variância e melhorar o desempenho do modelo.

A `engenharia de features` teve papel central no projeto. As variáveis de interação entre **tabagismo**, **idade** e **BMI** mostraram-se determinantes para capturar efeitos que não seriam explicados por relações lineares simples. O entendimento sobre a exclusão de variáveis redundantes ou estatisticamente irrelevantes contribuiu para um modelo mais interpretável e eficiente.

Outro aprendizado técnico importante foi compreender que a **heterocedasticidade**, embora presente, *não invalida o modelo* quando as métricas de desempenho são consistentes e os coeficientes permanecem estatisticamente significativos.

Durante a validação no conjunto de teste, enfrentei dificuldades práticas, como a **interpretação de métricas negativas**, que serviram como sinal de inconsistências no pipeline de preparação dos dados. Esses episódios foram fundamentais para reforçar boas práticas de validação e consistência entre treino e teste.

Além da parte técnica, procurei conduzir o projeto com uma visão orientada ao negócio, questionando constantemente se os resultados faziam sentido no mundo real e se os efeitos estimados eram plausíveis do ponto de vista econômico e comportamental. Erros fizeram parte de todo o processo, desde a criação de variáveis dummy, tratamento de outliers, até problemas de interpretação de métricas e gráficos. Lidei com esses desafios de forma madura e estruturada, utilizando cada falha como uma oportunidade de aprendizado e refinamento do modelo.

Por fim, consolidei a percepção de que *Ciência de Dados* só gera valor quando se transforma em **decisão**. Por isso, fui além do ajuste do modelo e da análise de métricas, aplicando os resultados em um contexto realista de pricing, avaliando o impacto financeiro e estratégico das variáveis no negócio.
