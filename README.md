# Projeto de previsão de vendas
![image](https://user-images.githubusercontent.com/75793555/155318064-9fa0f5f9-d53a-4f8e-869e-e0584eb814fb.png)
**Aviso:** O seguinte contexto é completamente fictício, a empresa, o contexto, o CEO, as questões de negócios existem apenas na minha imaginação.

# 1. Descrição

Uma das maiores redes de drogarias da Europa a Rossmann opera mais de 3000 unidades em 7 paises da europa. Com o sucesso de sua marca, a Rossmann planeja uma reforma geral em todas as suas lojas, porem atualmente a previsão de vendas é realizada por cada gestor de cada loja, através de uma planilha em excel considerando a média das vendas, achando essa metodologia falha e antiga, a administração da empresa busca novas soluções.

Essa nova solução surgiu através de uma reunião estratégica, onde foi identificado a necessidade de realizar reformas nas lojas e para esse investimento, é indispensável uma previsão de vendas assertiva. Neste sentido, a equipe estratégica solicitou para o Cientista de dados uma previsão de vendas das próximas 6 semanas, com resultados acurados por loja.

Questão de negócio: Qual o valor de vendas de cada loja nas próxima 06 semanas?

Acesso ao bot do modelo no Telegram:

[<img alt="Telegram" src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>](https://t.me/rb_rossman_bot)

# 2. Premissas de negócio

* Lojas que não contém informações sobre a distância entre concorrentes (competition_distance) foi atribuído um valor 2x maior que o valor máximo;
* Caso não haja a data em que a concorrência abriu ou dados em relação aos periodos promocionais (competition_open_since, promo2_since), o valor nulo será substituído pelo valor da venda, pensando na premissa que algumas variáveis derivadas do tempo são extremamente importantes para representar um comportamento;
* Dados que descrevem a quantidade de funcionários da loja (customers), foi descartado. Pois, não podemos prever a quantidade de funcionários nas próximas seis semanas, abrindo espaço para um outro projeto;
* Dias em que as lojas as lojas estavam fechadas foram retirados;
* Apenas registros com venda superior a 0 (sales).

# 3. Lista de atributos

| Atributos                        | Explicação                                                      |
| -------------------------------- | ------------------------------------------------------------ |
| Id                               | Um Id que representa uma dupla (Store, Date) dentro do conjunto de teste |
| Store                            | Um id único para cada loja                                   |
| Sales                            | O volume de vendas para qualquer dia                         |
| Customers                        | O número de clientes em um determinado dia                       |
| Open                             | Um indicador para saber se a loja estava aberta: 0 = fechada, 1 = aberta |
| StateHoliday                     | Indica um feriado estadual. Normalmente todas as lojas, com poucas exceções, fecham nos feriados estaduais. Observe que todas as escolas fecham nos feriados e finais de semana. a = feriado, b = feriado da Páscoa, c = Natal, 0 = Nenhum |
| SchoolHoliday                    | Indica se (Loja, Data) foi afetado pelo fechamento de escolas públicas |
| StoreType                        | Diferencia entre 4 modelos de loja diferentes: a, b, c, d  |
| Assortment                       | Descreve um nível de estoque: a = básico, b = extra, c = estendido |
| CompetitionDistance              | Distancia em metros do competidor mais proximo           |
| CompetitionOpenSince[Month/Year] | Dá o ano e mês aproximados em que o concorrente mais próximo foi aberto |
| Promo                            | Indica se uma loja está fazendo uma promoção naquele dia         |
| Promo2                           | Promo2 é uma promoção contínua e consecutiva para algumas lojas: 0 = a loja não está participando, 1 = a loja está participando |
| Promo2Since[Year/Week]           | Descreve o ano e a semana em que a loja começou a participar da Promo2 |
| PromoInterval                    | Descreve os intervalos consecutivos de início da promoção 2, nomeando os meses em que a promoção é iniciada novamente. Por exemplo. "Fev, maio, agosto, novembro" significa que cada rodada começa em fevereiro, maio, agosto, novembro de qualquer ano para aquela loja |

# 4. Estratégias para solução

1. **Entendimento dos dados:** nessa etapa, é utilizado métricas estatísticas para mapeamento e entendimento dos dados;
2. **Tratamento de dados:** tratamento de dados nulos e dados fora do escopo de negócio, derivar novos atributos e filtragem de linhas e colunas para modelagem de dados;
3. **Análise exploratória de dados:** explorar dados para retirar insights e para entendimento de cada variável para aprendizado do modelo;
4. **Preparação e seleção de dados para o modelo:** transformação dos dados para que os algoritmos possam aprendem o comportamento dos dados e seleção das melhores variáveis;
5. **Treinamento do modelo:**  treinamento do modelo de aprendizado;
6. **Hyperparameter Fine Tunning:** escolha dos melhores valores para cada um dos parâmetros do modelo;
7. **Métricas do modelo e métricas de negócio:** desempenho do modelo para o resultado de negócios;
8. **Deploy:** deploy do modelo em nuvem e criação do bot no Telegram para consulta da previsão.

# 4.1. Top Insights

1. **H2. Lojas com competidores mais próximos deveriam vender menos.** Falsa, a relação de venda com a distância de competidores não se correlacionam.

2. **H7. Em média, as vendas no natal deveriam ser maiores.** Verdadeira, o volume de vendas em comparação aos outros dias é maior, na média.

3. **H11. Lojas que abrem nos finais de semana deveriam vender menos.** Verdadeiro, o volume reduz durante a semana, significativamente durante os finais de semana, em relação aos outros dias.

# 5. Modelos de Machine Learning e Performance

Modelos utilizados para teste:
- Average Model
- Linear Regression Model
- Linear Regression Regularized Model - Lasso
- Random Forest Regressor
- XGBoost Regressor

**Performance**

| Model Name | MAE | MAPE  | RMSE |
|-----------|---------|-----------|---------|
|  Linear Regression  | 1864.29 |	0.29	| 2660.29 |
|  Linear Regression Lasso	| 1862.75 |	0.29 | 2680.59 |
|  Random Forest Regressor	  | 674.85 |	0.10 |	1006.19 |
|  XGBoost Regressor | 6683.34 |	0.95 |	7330.61 |

**Performance Cross Validation**

| Model Name | MAE CV   | MAPE CV      | RMSE CV |
|-----------|---------|-----------|---------|
|  Random Forest Regressor  | 838.79 +/- 221.98| 0.12 +/- 0.02  | 1257.26 +/- 323.91 |
|  Linear Regression	  | 2075.55 +/- 294.74 | 0.3 +/- 0.01   | 2949.35 +/- 463.59 |
|  Linear Regression - Lasso	  | 2116.72 +/- 341.48 | 0.29 +/- 0.01	   | 3057.96 +/- 504.86 |
|  XGBoost Regressor	  | 7049.09 +/- 588.66 | 0.95 +/- 0.00   | 7715.15 +/- 689.64 |

No processo de aplicação de algoritmos, os modelos lineares não tiveram bons resultados. A Random Forest Regressor teve um resultado superior aos outros, mas antes de selecionar o modelo ideal, temos alguns pontos para avaliar.

Fatores como recurso computacional, tempo e espaço de armazenamento, influênciaram na seleção do modelo. Neste sentido, o algoritmo selecionado foi o XGBoost Regressor, por ser um modelo mais performático que a RFR. E Para uma primeira entrega (MVP) a RFR não faria muito sentido, neste momento.

# 6. Hyperparameter Fine Tunning

Após a seleção do modelo, foi submetido ao procedimento de Fine Tunning, através do método Random Search, os melhores parâmetros foram selecionados e o modelo foi treinado e testado novamente. Apresentando os seguintes resultados:

| Model Name| MAE CV  | MAPE CV   | RMSE CV |
|-----------|---------|-----------|---------|
|XGBoost Regressor |	875.97+/-147.62 |	0.12+/-0.02 |	1248.59+/-207.69|

# 7. Métricas do modelo e métricas de negócio

Para verificar a performance do modelo, é necessário comparar com o atual modelo utilizado pela empresa (Average Model) com modelo proposto (XGBoost Regressor):

**Average Model**
| Cenário | Predições | 
|-----------|---------|
| Total Predictions| R$280,754,389.45|

**XGBoost**
| Cenário | Predições | 
|-----------|---------|
| predições |	R$282,954,840.45 |
| melhor cenário |	R$255,429,264.00 |
| pior cenário |	R$310,480,416.91 |

## 7.1. Comparativo entre modelos

Desempenho entre modelos:

| Model Name| MAE | MAPE | RMSE |
|-----------|---------|-----------|---------|
| Average Model	|	1354.80 |	0.46 |	1835.14|
|XGBoost Regressor Tuned| 664.93 | 0.10 | 964.50|

Comparativo entre cenários:

| Cenário | Predições | 
|-----------|---------|
| melhor cenário | - R$25.325.125,45 |
| pior cenário | + R$29.726.027,46 |

Obs: predições do XGB - predições Avarege Model

# 8. Conclusão

Sobre o modelo XGBoost apresentou resultados consideráveis para um primeiro ciclo do método CRISP, principalmente ao aprendizado do comportamento e oscilações de cada loja, ponto que o modelo de média não realiza. As predições do modelo em sua maioria subestimam as predições, e de 1.115 lojas, 1% das lojas tem o erro média absoluto acima de 20%, sendo a média de 10% (MAPE) com desvio padrão de 3%. 

Por mais que o modelo de média seja um modelo simples e que apresentou valores de predições parecidos com o XGBoost, o MAPE é de 46%. Nesse sentido, como o problema de negócio é uma predição de valores por loja nas próximas seis semanas. Faz sentido a utilização do modelo proposto como solução.

# 9. Proximos passos

Para um segundo ciclo, notou-se alguns pontos para melhoria do modelo:

- Desenvolver um modelo para predição de colaboradores na loja (customers), para trabalhar em conjunto com o modelo de predição de vendas;
- Tentar abordagens diferentes com dados Nulos;
- Testar outros enconders ou rescaling de dados;
- Tunar os parâmetros do modelo com outra metodologia;
- Criar novos outputs para o bot no Telegram.
