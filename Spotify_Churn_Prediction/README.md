Vamos nos conectar?
[Linkedin](https://www.linkedin.com/in/jeduardosleite/)

<img width="1198" height="539" alt="image" src="https://github.com/user-attachments/assets/cb006013-dcf4-44b9-8783-f37fdb33ae4e" />

# Índice

- [Visão Geral do Projeto](#visão-geral-do-projeto)
- [Objetivo](#objetivo)
- [Dataset](#dataset)
- [Ferramentas Utilizadas](#ferramentas-utilizadas)
- [Preparação dos Dados](#preparação-dos-dados)
- [Análise das Variáveis Quantitativas](#análise-das-variáveis-quantitativas)
- [Engenharia de Atributos](#engenharia-de-atributos)
- [Multicolinearidade](#multicolinearidade)
- [Tratamento de Desbalanceamento](#tratamento-de-desbalanceamento)
- [Treinamento do Modelo](#treinamento-do-modelo)
- [Tunando o Modelo](#tunando-o-modelo)
- [Conclusão](#conclusão)

---

# Visão Geral do Projeto

Este projeto tem como objetivo prever o churn de usuários do Spotify, utilizando Machine Learning para identificar quais usuários têm maior probabilidade de cancelar o serviço. 
O foco principal está em práticas reais de preparação de dados, engenharia de atributos, tratamento de desbalanceamento e otimização de modelos.

[⬆ Voltar ao topo](#índice)
---

## Objetivo

Construir um modelo supervisionado capaz de prever usuários churn com foco em alto recall, priorizando a detecção de usuários propensos ao cancelamento para ações preventivas.

[⬆ Voltar ao topo](#índice)
---

## Dataset
```user_id``` → Identificador único para cada usuário

```gender``` → Sexo do usuário (Masculino/Feminino/Outro)

```age``` → Idade do usuário

```country``` → Localização do usuário

```subscription_type``` → Tipo de assinatura do Spotify (Gratuita, Premium, Família, Estudante)

```listening_time``` → Minutos de audição por dia

```songs_played_per_day``` → Número de músicas reproduzidas diariamente

```skip_rate``` → Percentual de músicas puladas

```device_type``` → Dispositivo utilizado (Celular, Computador, Web)

```ads_listened_per_week``` → Número de anúncios visualizados por semana

```offline_listening``` → Uso do modo offline

```is_churned``` → Variável alvo (0 = Ativo, 1 = Cancelado)

[⬆ Voltar ao topo](#índice)
---

## Ferramentas Utilizadas

- Python (Jupyter Notebook)
- Pandas, NumPy, Matplotlib, Seaborn
- PyCaret (Classificação)
- Scikit-learn

[⬆ Voltar ao topo](#índice)
---

## Preparação dos Dados

1) Remoção de colunas dispensáveis para o projeto, neste caso, a ```user_id```;
2) Verificação e possível tratamento dos valores nulos;
3) Criação do metadado para entender a dimensão do conjunto;

<img width="503" height="365" alt="image" src="https://github.com/user-attachments/assets/9ef10d13-97ef-4604-93db-b0b6d4631d38" />

[⬆ Voltar ao topo](#índice)
---

## Análise das variáveis quantitativas

- ```Contagem``` (count)
- ```Média``` (mean)
- ```Desvio padrão``` (std) - *dispersão dos dados*
- ```Mínimo``` (min)
- ```Quartis``` (25%, 50%, 75%)
- ```Máximo``` (max)

<img width="587" height="239" alt="image" src="https://github.com/user-attachments/assets/c25bfaad-ae98-44e4-a7d9-3153bccc45b6" />

Dentro do notebook estão documentadas as interpretações dessa informação.

[⬆ Voltar ao topo](#índice)
---

## Engenharia de Atributos

Inicialmente, tive problemas para treinar o meu modelo, pois as features estavam com o ```information value``` baixíssimo, ou seja, seu comportamento estava fraco. 

|Faixa|Poder preditivo|
|:-|:-|
|0 a 0,02| Inútil |
|0,02 a 0,1| Fraco |
|0,1 a 0,3| Médio |
|0,3 a 0,5| Forte |
|0,5 ou mais| Suspeito de tão alto |

<img width="566" height="370" alt="image" src="https://github.com/user-attachments/assets/123a796f-596d-44c5-be42-02dfafee0dc7" />

Para solucionar esse problema, criei novas features, tais como:

- **daily_engagement** = listening_time / songs_played_per_day
- **skip_intensity = skip_rate** * songs_played_per_day
- **premium_use_factor** = premium * (1 - skip_rate)
- **listening_ratio** = listening_time / (songs_played_per_day + 1)

Após criar, as colunas utilizadas na composição também foram mantidas para interpretação.

[⬆ Voltar ao topo](#índice)
---

## Multicolinearidade
A multicolinearidade ocorre quando duas ou mais variáveis independentes (preditoras) em um modelo de regressão são altamente correlacionadas entre si. 
Isso significa que elas fornecem informações redundantes ou muito semelhantes sobre a variável dependente do modelo. 

<img width="784" height="652" alt="image" src="https://github.com/user-attachments/assets/875d6cdc-2bbf-4bd3-a2a4-6fe139e67f79" />

O único comportamento diferente é da variável **offline_listening** que apresentou um coeficiente extremamente alto de **-0.88** (quase uma relação perfeita). Mas por quê?

Olhando para o plano de negócio, podemos deduzir que o *modo offline* é uma função exclusiva de planos pagos (*Premium*), indicando que:
- ```offline_listening = 1```: usuário Premium
- ```offline_listening = 0```: usuário gratuíto

Dentro do conjunto de dados, temos o ```subscription_type``` que se refere ao tipo de assinatura (gratuita, premium, família, estudante). Podemos deduzir que há uma redundância de informações entre estas duas variáveis, ocasionando uma *multicolinearidade*.

Partindo da relação observada entre usuários ```Premium``` e ```Free```, levantei a seguinte questão:

> Existe alguma outra variável que esteja conceitualmente relacionada a esse mesmo comportamento?

Ao analisar a descrição das colunas, identifiquei que a variável **ads_listened_per_week** é uma forte candidata. 

A lógica é simples: usuários Premium não escutam ou assistem anúncios, pois essa é uma das principais vantagens do plano pago.
Portanto, essa variável também reflete o conceito de ```Premium vs Free```, indicando redundância de informação com ```offline_listening```.

### Tratamento da Multicolinearidade

Para evitar redundância no modelo e garantir uma melhor interpretação dos resultados, adotei o seguinte tratamento:
- Remoção das variáveis ```subscription_type``` e ```ads_listening_per_week```;
- Renomear a variável ```offline_listening``` para ```premium```, sendo:
  - *1*: Premium
  - *0*: Free 

[⬆ Voltar ao topo](#índice)
---

## Tratamento de Desbalanceamento

Outro problema encontrado foi o desbalanceamento da target. Primeiramente, tratei com ```smote``` após a separação da base de treinamento e teste, todavia, o resultado não foi satisfatório. 
Realizando uma pesquisa em fóruns, vídeos e visitando outros projeto que utilizaram o mesmo dataset, me deparei com a ideia de tratar o desbalanceamento dentro do próprio PyCaret, ativando:

```python
fix_imbalance=True  
fix_imbalance_method='smote'
```

Isso garante reamostragem apenas nos dados de treino, evitando vazamento.

[⬆ Voltar ao topo](#índice)
---

## Treinamento do Modelo

1) **Preparação**: Converti as colunas categóricas em variáveis numéricas, utilizando o pd.get_dummies

2) **Pycaret**: Usei o método PyCaret para comparar os melhores modelos.

### Qual modelo?
A escolha do modelo está ligada ao ponto central deste projeto:
> Identificar o maior número possível de clientes que vão sair (recall alto), sem gerar muitos falsos positivos (boa precisão).

Analisando rapidamente a tabela abaixo, a escolha coerente a se fazer seria o ```Gradient Boosting Classifier```, mas vamos analisar o plano de negócio e estudar os modelos disponíveis.

Peguei os quatro modelos principais e analisei as métricas.
- **gbc**
- **Ada**
- **rf**
- **lightgbm**

<img width="723" height="491" alt="image" src="https://github.com/user-attachments/assets/8a068bde-02a0-4896-9a85-5829e231767f" />

Após analisar os modelos, escolhi o ```gbc_model```, pois ele:
- tem equilíbrio entre desempenho e velocidade;
- possui alta capacidade de generalização;
- treina rápido e consome pouca memória;
- permite ajuste finvia *tune_model()*

[⬆ Voltar ao topo](#índice)
---

## Tunando o modelo

| Parâmetro             | O que faz                                                               | Impacto no modelo                                                                      |
| --------------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **n_estimators**      | Número de árvores (iterações de boosting).                              | Mais árvores → mais capacidade, porém risco de overfitting e maior tempo.              |
| **learning_rate**     | Taxa de aprendizado que controla o peso de cada árvore adicionada.      | Menor valor → aprendizado mais lento, porém mais robusto; exige mais árvores.          |
| **max_depth**         | Profundidade máxima de cada árvore.                                     | Profundidade maior → modelo mais complexo; risco de overfitting.                       |
| **min_samples_split** | Número mínimo de amostras para dividir um nó.                           | Valores maiores tornam o modelo mais simples e evitam divisões muito pequenas.         |
| **min_samples_leaf**  | Número mínimo de amostras que um nó folha deve ter.                     | Folhas maiores → generalização melhor, menos overfitting.                              |
| **subsample**         | Proporção de amostras usadas em cada árvore (amostragem sem reposição). | <1.0 adiciona aleatoriedade → reduz overfitting (como “stochastic gradient boosting”). |
| **max_features**      | Número de features usadas para procurar a melhor divisão em cada split. | `sqrt` e `log2` reduzem correlação entre árvores, diminuem overfitting.                |

```python
params = {
    'n_estimators': [100, 200, 300, 500],
    'learning_rate': [0.01, 0.05, 0.1],
    'max_depth': [2, 3, 5, 7],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 5],
    'subsample': [0.6, 0.8, 1.0],
    'max_features': ['sqrt', 'log2', None],
}

tuned_gbc = tune_model(
    gbc_model,
    custom_grid=params,
    optimize='F1',
    fold=5,
    n_iter=100,
    choose_better=True
)
```
<img width="575" height="63" alt="image" src="https://github.com/user-attachments/assets/ced931cf-5174-4081-bffa-03a91b0d15e7" />

[⬆ Voltar ao topo](#índice)
---

## Conclusão

O modelo desenvolvido apresentou desempenho consistente e alinhado ao objetivo principal: maximizar a identificação correta da classe positiva, priorizando recall por meio do F2-Score. Após a otimização do limiar de decisão, o melhor threshold encontrado foi 0.22, resultando em um F2-Score de 0.8009, indicando boa capacidade do modelo em identificar casos positivos mesmo em um cenário desbalanceado.

As métricas finais evidenciam um equilíbrio importante entre desempenho da classe majoritária e da classe minoritária. O modelo atingiu recall de 0.83 para a classe positiva, reduzindo significativamente falsos negativos — o erro mais crítico para o problema. A matriz de confusão confirma essa eficiência, mostrando que o modelo reconhece a maior parte das ocorrências positivas, mantendo ao mesmo tempo uma precisão adequada.

Além disso, o uso de técnicas de balanceamento, análise de métricas complementares e ajuste fino dos hiperparâmetros contribuiu diretamente para melhorar a performance do modelo. Os resultados obtidos demonstram que a solução é robusta, generaliza bem para dados não vistos e está pronta para ser aplicada em um ambiente real ou integrada a processos de tomada de decisão.

<img width="398" height="218" alt="image" src="https://github.com/user-attachments/assets/3345ebe3-6557-4c47-a41d-789cdbda30ac" />

[⬆ Voltar ao topo](#índice)
