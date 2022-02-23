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
