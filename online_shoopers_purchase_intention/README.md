# Índice

1. [Definição Técnica do Projeto](#1-definição-técnica-do-projeto)  
2. [Tecnologias Utilizadas](#2-tecnologias-utilizadas)  
3. [Objetivo Final](#3-objetivo-final)  
4. [Dataset](#4-dataset)  
5. [Como defini o número de cluster?](#5-como-defini-o-número-de-cluster)  
   - [Método do Cotovelo (Elbow Method)](#método-do-cotovelo-elbow-method)  
   - [Coeficiente de Silhueta (Silhouette Score)](#coeficiente-de-silhueta-silhouette-score)  
   - [Análise de Negócio](#análise-de-negócio)  
6. [Avaliação dos Grupos](#6-avaliação-dos-grupos)  
   - [2 Clusters](#2-clusters)  
   - [3 Clusters](#3-clusters)  
   - [4 Clusters](#4-cluster)  
7. [Avaliação de Resultados](#7-avaliação-de-resultados)  
   - [Cluster 1 — Compradores Ativos](#cluster-1--compradores-ativos)  
   - [Cluster 0 — Pesquisadores antes de comprar](#cluster-0--pesquisadores-antes-de-comprar)  
   - [Cluster 2 — Não compradores](#cluster-2--não-compradores-ou-baixo-engajamento)  
8. [Escolhendo o cluster](#8-escolhendo-o-cluster)  
9. [Por que focar em "Pesquisam antes de comprar?"](#9-por-que-focar-em-pesquisam-antes-de-comprar)  
   - [1. Alto potencial de receita](#1-alto-potencial-de-receita)  
   - [2. Comportamento estratégico](#2-comportamento-estratégico)  
   - [3. Margem de crescimento](#3-margem-de-crescimento)  
   - [4. Eficiência de investimento](#4-eficiência-de-investimento)  
10. [Conclusão Final](#10-conclusão-final)  
   - [Estímulos de Marketing para "Pesquisam antes de comprar"](#estímulos-de-marketing-para-pesquisam-antes-de-comprar)


#### Contate-me: https://www.linkedin.com/in/jos%C3%A9-eduardo-souza-leite/

---

<h1 align="center">Intenção de Compra Online</h1>
<h3 align="center">Projeto de Clusterização</h3>

<p align="center">
<img width="827" height="673" alt="image" src="https://github.com/user-attachments/assets/128daf4b-4dc1-4fa9-921c-ca55c729be4c" />
</p>

---

## 1. Definição Técnica do Projeto

Este projeto tem como objetivo a **segmentação de clientes** com base em dados de navegação e comportamento de compra, utilizando técnicas de análise estatística e machine learning.  

A metodologia aplicada envolveu as seguintes etapas:

1. **Pré-processamento de dados**  
   - Limpeza e padronização da base de dados.  
   - Seleção de variáveis relevantes (ex.: PageValue, Bounce Rate, Revenue).  
   - Padronização dos dados numéricos para aplicação de algoritmos de clusterização.  

2. **Clusterização de clientes**  
   - Aplicação do algoritmo **K-Means** para identificar padrões de comportamento.  
   - Avaliação de métricas de qualidade dos clusters (Silhouette Score) para definição do número ótimo de grupos.  
   - Interpretação dos clusters em perfis acionáveis:  
     - **Compradores Ativos**  
     - **Pesquisam Antes de Comprar**  
     - **Não Engajados**  

3. **Análise de valor (PageValue)**  
   - Cálculo de estatísticas descritivas do PageValue por cluster.  
   - Estimativa de receita potencial atribuída a cada perfil de cliente.  
   - Identificação do grupo **“Pesquisam Antes de Comprar”** como segmento estratégico, com maior potencial de conversão em **Compradores Ativos**.  

4. **Recomendações de negócio**  
   - Definição de estímulos de marketing personalizados (remarketing, ofertas direcionadas, prova social).  
   - Priorização de investimentos em clientes com maior probabilidade de gerar receita.  
   - Estratégia de retenção focada em transformar clientes de alto potencial em compradores recorrentes.  

[🔝 Voltar ao topo](#índice)
---

## 2. Tecnologias Utilizadas
- **Python** (pandas, numpy, matplotlib, seaborn, scikit-learn)  
- **Jupyter Notebook** para análise e visualização  
- **Markdown** para documentação
- **Git/Git Hub** para versionamento

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from sklearn.metrics import silhouette_score
from tqdm.notebook import tqdm
from sklearn.metrics import silhouette_samples
```
[🔝 Voltar ao topo](#índice)
---

## 3. Objetivo Final

Responder a questão:

- **Por que os clientes que pesquisam antes de comprar são mais propensos à compra, apesar de serem estatisticamente inferiores aos clientes do grupo compras ativas?**

Demonstrarei, de forma analítica e visual, como a **ciência de dados aplicada à segmentação de clientes** pode gerar insights estratégicos para otimização de conversão, aumento de receita e eficiência em ações de marketing.

[🔝 Voltar ao topo](#índice)
---

## 4. Dataset

Neste projeto utilizarei a base [online shoppers purchase intention](https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset) de Sakar, C.O., Polat, S.O., Katircioglu, M. et al. Neural Comput & Applic (2018). [Web Link](https://doi.org/10.1007/s00521-018-3523-0).

A base trata de registros de 12.330 sessões de acesso a páginas, cada sessão sendo de um único usuário em um período de 12 meses
|Variavel                |Descrição          | 
|------------------------|:-------------------| 
|Administrative          | Quantidade de acessos em páginas administrativas| 
|Administrative_Duration | Tempo de acesso em páginas administrativas | 
|Informational           | Quantidade de acessos em páginas informativas  | 
|Informational_Duration  | Tempo de acesso em páginas informativas  | 
|ProductRelated          | Quantidade de acessos em páginas de produtos | 
|ProductRelated_Duration | Tempo de acesso em páginas de produtos | 
|BounceRates             | *Percentual de visitantes que entram no site e saem sem acionar outros *requests* durante a sessão  | 
|ExitRates               | * Soma de vezes que a página é visualizada por último em uma sessão dividido pelo total de visualizações | 
|PageValues              | * Representa o valor médio de uma página da Web que um usuário visitou antes de concluir uma transação de comércio eletrônico | 
|SpecialDay              | Indica a proximidade a uma data festiva (dia das mães etc) | 
|Month                   | Mês  | 
|OperatingSystems        | Sistema operacional do visitante | 
|Browser                 | Browser do visitante | 
|Region                  | Região | 
|TrafficType             | Tipo de tráfego                  | 
|VisitorType             | Tipo de visitante: novo ou recorrente | 
|Weekend                 | Indica final de semana | 
|Revenue                 | Indica se houve compra ou não |

\* variávels calculadas pelo google analytics

<img width="375" height="305" alt="image" src="https://github.com/user-attachments/assets/e6dbdb92-b7be-45f3-8583-2edacc9e1be4" />

[🔝 Voltar ao topo](#índice)
---

## 5. Como defini o número de cluster?

Para encontrar a quantidade ideal de clusters, utilizei métricas de avaliação que ajudam a medir a qualidade da segmentação:  

1. **Método do Cotovelo (Elbow Method)**  
   - Calcula o *inertia* (soma das distâncias dos pontos ao centróide do cluster).
   - O ponto onde a redução começa a ser menos significativa (o "cotovelo" da curva) sugere o número ideal de clusters.  

<img width="494" height="386" alt="image" src="https://github.com/user-attachments/assets/8d6f1a57-c0b8-406a-bf94-6cf8102d1ef7" />

2. **Coeficiente de Silhueta (Silhouette Score)**  
   - Mede o quão semelhantes os pontos estão dentro de um cluster em comparação com outros clusters.  
   - Varia de -1 a 1:  
     - Valores próximos de **1** → clusters bem separados.  
     - Valores próximos de **0** → sobreposição entre clusters.  
     - Valores negativos → pontos classificados no cluster errado.  
   - O número de clusters com maior *Silhouette Score* costuma ser o mais adequado.  

<img width="385" height="269" alt="image" src="https://github.com/user-attachments/assets/19044174-901b-4df2-833a-735cc7cf3b7d" />

3. **Análise de Negócio**  
   - Mesmo que estatisticamente seja sugerido um número X de clusters, é fundamental verificar se eles fazem sentido no contexto do negócio.  
   - Por exemplo: 2 clusters podem simplificar demais a análise, enquanto 3 ou 4 podem revelar segmentos mais estratégicos e acionáveis.  

Neste projeto, combinei o **método estatístico (Silhouette)** com a **relevância prática para o negócio**, garantindo que os clusters encontrados sejam ao mesmo tempo **tecnicamente válidos e úteis para tomada de decisão**.

[🔝 Voltar ao topo](#índice)
---

## 6. Avaliação dos Grupos  

Para identificar a segmentação mais adequada, realizei uma análise descritiva comparando diferentes valores de **n_clusters**.  
Além dos indicadores estatísticos (como silhueta média e distribuição de variáveis), também considerei a **perspectiva de negócio**, avaliando o impacto potencial de cada grupo em termos de receita, engajamento e oportunidades de conversão.  

Esse processo uniu a visão analítica baseada em dados com o olhar estratégico, permitindo escolher a configuração de clusters que não apenas apresenta boa performance técnica, mas também gera **insights acionáveis** para a empresa.  

### 2 clusters
Possui a maior média, com *0,73*. Porém, vejo que a discriminação em 2 grupos é pouco informativo, pois separa o grupo em **compradores** e **não compradores**, por exemplo. Visto que o objetivo do negócio é tentar agrupar os clientes conforme seu comportamento de navegação entre páginas administrativas, informativas e de produtos, acredito que não seja o mais aconselhável escolher apenas dois grupos.

### 3 clusters
Embora a análise estatística inicial apontasse para apenas 2 agrupamentos, a opção por segmentar em 3 revelou um público-alvo extremamente valioso que, de outra forma, permaneceria invisível. Essa classificação em 3 clusters me possibilitou organizar os clientes em categorias distintas e operacionais, permitindo uma compreensão mais profunda do comportamento, maior precisão nas ações de marketing e vendas, além de oferecer subsídios concretos para decisões estratégicas. Por estas razões, escolhi trabalhar com 3 clusters.

- ```Compradores ativos```: visitam várias páginas de produtos e passam mais tempo navegando.

- ```Pesquisadores antes de comprar```: visitam páginas informacionais, navegam um pouco mais devagar. Compram, mas depois de pesquisar, comportamento intermediário.

- ```Não engajados```: navegação rápida, pouco interesse em produtos.

### 4 cluster
Apesar de a média apresentar resultados semelhantes quando utilizamos 3 clusters, a escolha por esse número é mais adequada para este caso de negócio. Isso porque:
- Três grupos já conseguem responder de forma consistente à questão central: identificar quais clientes são mais propensos à compra.
- Incluir um quarto cluster não agrega novos insights relevantes, apenas aumenta a complexidade da análise sem ganho prático.
- A simplicidade na segmentação facilita tanto a interpretação dos resultados quanto a aplicação de estratégias de marketing direcionadas.

[🔝 Voltar ao topo](#índice)
---

## 7. Avaliação de Resultados

Nesta etapa, o foco foi responder à questão central do projeto:  

- **Qual grupo dos 3 clusters concentra os clientes mais propensos à compra?**  

Para isso, conduzi uma análise detalhada das variáveis, não apenas sob a ótica estatística, mas também considerando o **contexto de negócio**.  
Esse processo permitiu gerar **insights estratégicos** para apoiar decisões gerenciais e propor **ações de marketing direcionadas**, aumentando as chances de conversão e retenção de clientes.

### Definindo os grupos

<img width="488" height="147" alt="image" src="https://github.com/user-attachments/assets/63cbf896-a24a-4468-b1e0-3be7c651480f" />

Nesta etapa, apresentarei a segmentação dos clientes com o objetivo de demonstrar como as métricas foram interpretadas, quais caminhos analíticos conduziram às informações obtidas, a definição dos perfis identificados e, por fim, recomendações práticas para retenção dos clientes mais relevantes e captação dos clientes menos engajados.

## Cluster 1 — “Compradores ativos”
- **Maior taxa de conversão (34%)** e maior **ProductRelated_Duration (9.07)**.  
- **Bounce/Exit muito baixos** → visitantes permanecem no site e não abandonam logo.  
- **PageValues moderado (5.94)** — não é o mais alto, mas o tempo em produto é o maior.  

**Interpretação:**  
Usuários que passam tempo em páginas de produto, examinam detalhes e convertem. Perfil valioso e com alto engajamento.  

**Ações recomendadas:**  
- Programas de retenção / upsell (cross-sell, bundles).  
- Incentivos de fidelização (cupom pós-compra, e-mails de recompra).  
- Priorizar A/B tests de checkout para aumentar AOV (valor médio do pedido).  

---

## Cluster 0 — “Pesquisadores antes de comprar”
- **Taxa de conversão alta-moderada (25%)**.  
- **PageValues mais alto (8.78)** — sessões com páginas que historicamente trazem valor.  
- **Tempo em produto mediano (7.91)**, bounce/exit baixos.  

**Interpretação:**  
Exploram bastante, visitam páginas que têm boa performance (por isso PageValues alto), mas convertem menos que cluster 1 — parecem comparar/avaliar antes de comprar.  

**Ações recomendadas:**  
- Conteúdo que ajude decisão: comparativos, avaliações, Q&A, frete gratuito no carrinho.  
- Remarketing com provas sociais e ofertas segmentadas (recuperação de carrinho, ofertas personalizadas).  
- Testar CTAs mais claros em páginas com grande PageValue.  

---

## Cluster 2 — “Não compradores” (ou baixo-engajamento)
- **Menor taxa de conversão (13%)**.  
- **Bounce/Exit bem maiores (2,54% e 4,79%)** — comparativamente ~4x os outros.  
- **PageValues e ProductRelated_Duration mais baixos** → menor engajamento e menos interação com páginas de valor.  

**Interpretação:**  
Tráfego de baixa qualidade ou visitantes pouco engajados — muitas sessões rápidas, poucos que chegam a considerar compra.  

**Ações recomendadas:**  
- Revisar origem do tráfego (canais/campanhas): ajustar segmentação, excluir fontes de baixo ROI.  
- Melhorar landing pages (mensagem, velocidade, experiência mobile).  
- Captura de e-mails/lead magnets para nutrir (em vez de tentar converter na primeira visita).  
- Retargeting com oferta de entrada (frete grátis, desconto inicial) para mover alguns para grupo pesquisador.  

[🔝 Voltar ao topo](#índice)
---

## 8. Escolhendo o cluster

<img width="693" height="112" alt="image" src="https://github.com/user-attachments/assets/7142b6d2-ffda-4f41-8e73-63a7a470bae3" />

Isso confirma que o **Cluster 1** (Compradores ativos) tem maior taxa de conversão, mas o **Cluster 0** (Pesquisam antes de comprar) é o mais estratégico por ter mais usuários próximos da compra.

<img width="604" height="623" alt="image" src="https://github.com/user-attachments/assets/f8948bc2-f304-4f05-b273-6fc529049324" />

| Cluster                    | Taxa de Conversão | PageValue Médio | Receita Estimada (PageValue) | Interpretação Executiva |
|-----------------------------|------------------:|----------------:|-----------------------------:|--------------------------|
| Compradores ativos         | Alta (≈34%)       | R\$ 5,94         | R\$ 1.181                    | Grupo confiável, já gera valor de forma consistente |
| **Pesquisam antes de comprar** | **Média (≈25%)**      | **R\$ 8,78**     | **R\$ 16.546**               | **Potencial estratégico: clientes que só precisam de estímulo certo para converter** |
| Não engajados              | Baixa (≈13%)      | R\$ 5,35         | R\$ 54.887                   | Alto volume, mas pouco retorno consistente  |

[🔝 Voltar ao topo](#índice)
---

## 9. Por que focar em "Pesquisam antes de comprar?"

### 1. Alto potencial de receita
- Esse grupo apresenta o maior PageValue médio (R$ 8,78).  
- Quando interagem com páginas relevantes (ex.: carrinho, checkout), geram mais valor por visita do que qualquer outro cluster.  

### 2. Comportamento estratégico
- Embora nem todos convertam, o fato de pesquisarem antes de decidir indica que estão em um estágio avançado da jornada de compra.  
- São clientes quase prontos para comprar, apenas aguardando um incentivo (remarketing, oferta direcionada, frete grátis).  

### 3. Margem de crescimento
- A taxa de conversão ainda não é a mais alta, mas existe espaço para ganho.  
- Com estratégias adequadas, parte desse grupo pode migrar para o perfil de "Compradores Ativos".  

### 4. Eficiência de investimento
- Diferente dos "Não Engajados", onde o esforço dificilmente se paga, esse cluster concentra clientes que respondem melhor a estímulos de marketing.  
- Isso torna os investimentos mais eficazes e com maior retorno.  

[🔝 Voltar ao topo](#índice)
---

## 10. Conclusão final

Focar no cluster ```"Pesquisam antes de comprar"``` significa apostar em clientes estratégicos, com alto valor potencial e grande margem de conversão adicional.  
Esse grupo representa o elo de crescimento sustentável entre manter os compradores fiéis e descartar esforços improdutivos com clientes não engajados.
Eles já demonstraram interesse real. O papel do marketing é remover fricções e dar o empurrão final — seja com incentivos financeiros (desconto, frete grátis), seja com prova social e segurança.
Isso aumenta a chance de eles migrarem para o cluster Compradores Ativos, que é o mais consistente e rentável.

### Estímulos de Marketing para "Pesquisam antes de comprar"

| Objetivo              | Estímulo de Marketing                                                                 |
|-----------------------|----------------------------------------------------------------------------------------|
| **Converter**         | - Remarketing em Google/Meta Ads com produtos pesquisados                              |
|                       | - E-mails de abandono de carrinho com incentivo (ex.: desconto válido por 24h)         |
|                       | - Ofertas direcionadas (cupons exclusivos, descontos progressivos, combos promocionais)|
| **Fidelizar**         | - Programas de pontos ou cashback                                                      |
|                       | - Recomendações inteligentes com base em compras anteriores                            |
|                       | - Conteúdo de relacionamento (ex.: guias, dicas, tutoriais)                            |
| **Reduzir objeções**  | - Frete grátis ou upgrade de envio rápido                                              |
|                       | - Garantias claras (devolução grátis, suporte ativo, parcelamento facilitado)          |
|                       | - Prova social: avaliações, depoimentos e “últimas unidades” para gerar urgência       |

[🔝 Voltar ao topo](#índice)
---



