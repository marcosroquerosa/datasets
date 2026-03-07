```markdown
# 📊 Projeto: Análise de Vendas com Google Planilhas usando o Dataset Olist

## 🎯 Objetivo

Este projeto tem como objetivo aplicar conceitos introdutórios de **Ciência de Dados** utilizando **Google Planilhas**, a partir do dataset público de e-commerce brasileiro **Brazilian E-Commerce Public Dataset by Olist**.

Durante a atividade são explorados conceitos importantes como:

- Estrutura de dados tabular
- Integração de dados de múltiplas tabelas
- Tratamento e preparação de dados
- Criação de variáveis derivadas
- Construção de métricas de negócio (KPIs)
- Uso da função **QUERY** (semelhante ao SQL)
- Análise exploratória de dados

Este roteiro foi desenvolvido para uso educacional em atividades de **introdução à Ciência de Dados**.

---

# 📦 Dataset Utilizado

Dataset original:

Brazilian E-Commerce Public Dataset by Olist

Disponível em:

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Para uso em sala de aula foi utilizada uma **versão reduzida do dataset**, evitando problemas de desempenho no Google Planilhas.

---

# 🧪 Roteiro da Atividade

## 1️⃣ Download do Dataset

Realizar o download do dataset **Brazilian E-Commerce Olist** em formato **ZIP**.

---

# 2️⃣ Criar a Planilha

Criar uma nova planilha no Google Planilhas com o nome:

```

PROJETO_ANALISE_VENDAS

```

---

# 3️⃣ Importar os Arquivos CSV

Criar as seguintes abas na planilha e importar os arquivos CSV correspondentes.

Durante a importação selecionar:

```

Substituir página atual

```

### Abas criadas

| Aba | Arquivo |
|----|----|
| ORDERS | olist_orders_dataset.csv |
| ORDERS_ITEMS | olist_order_items_dataset.csv |
| CUSTOMERS | olist_customers_dataset.csv |
| PRODUCTS | olist_products_dataset.csv |

---

# 4️⃣ Criar a Aba de Dados Tratados

Criar uma nova aba chamada:

```

DADOS_TRATADOS

```

Essa aba será responsável por integrar os dados e preparar as variáveis para análise.

---

# 5️⃣ Estrutura da Tabela DADOS_TRATADOS

Criar as seguintes colunas:

| Coluna | Campo |
|---|---|
| A | order_id |
| B | data_pedido |
| C | status |
| D | ano |
| E | mes |
| F | mes_ano |
| G | pedido_valido |
| H | customer_id |
| I | estado_cliente |
| J | product_id |
| K | categoria |
| L | seller_id |
| M | price |
| N | frete |
| O | receita |

---

# 🔧 Tratamento e Integração dos Dados

## order_id

Copiar a coluna **order_id** da tabela **ORDERS_ITEMS**.

---

## data_pedido

```

=PROCV(A2;ORDERS!A:D;4;0)

```

Depois formatar a coluna como data:

```

Formatar → Número → Data

```

---

## status

```

=PROCV(A2;ORDERS!A:C;3;0)

```

---

## ano

```

=ANO(B2)

```

---

## mes

```

=MÊS(B2)

```

---

## mes_ano

```

=TEXTO(MÊS(B2);"00")&"/"&ANO(B2)

```

---

## pedido_valido

Identifica pedidos entregues.

```

=SE(C2="delivered";"Sim";"Não")

```

---

## customer_id

```

=PROCV(A2;ORDERS!A:B;2;0)

```

---

## estado_cliente

```

=PROCV(H2;CUSTOMERS!A:E;5;0)

```

---

## product_id

Copiar da tabela:

```

ORDERS_ITEMS

```

---

## categoria

```

=PROCV(J2;PRODUCTS!A:B;2;0)

```

---

## seller_id

Copiar da tabela:

```

ORDERS_ITEMS

```

---

## price

Copiar da tabela:

```

ORDERS_ITEMS

```

---

## frete

Copiar da tabela:

```

ORDERS_ITEMS

```

---

## receita

```

=M2+N2

```

---

# 📊 Criação da Aba KPIs

Criar uma nova aba chamada:

```

KPIs

```

Nesta aba serão calculados os principais indicadores de negócio.

---

# 📈 Indicadores Calculados

## Receita com todos os status

```

=SOMA(DADOS_TRATADOS!O:O)

```

---

## Receita Total (apenas pedidos válidos)

```

=SOMASE(DADOS_TRATADOS!G:G;"Sim";DADOS_TRATADOS!O:O)

```

---

## Total de Pedidos Válidos (entregues)

```

=COUNTUNIQUE(FILTER(DADOS_TRATADOS!A:A;DADOS_TRATADOS!G:G="Sim"))

```

---

## Ticket Médio

```

Receita Total / Total de Pedidos

```

---

## Clientes Únicos

```

=COUNTUNIQUE(FILTER(DADOS_TRATADOS!H:H;DADOS_TRATADOS!G:G="Sim"))

```

---

## Receita Média por Cliente

```

Receita Total / Clientes Únicos

```

---

## Total de Itens Únicos Vendidos

```

=COUNTUNIQUE(FILTER(DADOS_TRATADOS!J:J;DADOS_TRATADOS!G:G="Sim"))

```

---

# 📊 Análises com QUERY (Estilo SQL)

A função **QUERY** permite realizar consultas semelhantes ao SQL diretamente no Google Planilhas.

Sintaxe:

```

QUERY(intervalo; "consulta"; numero_de_cabecalhos)

```

---

# 📊 Receita por Categoria (Top 5)

```

QUERY(DADOS_TRATADOS!A:O;
"SELECT K, SUM(O)
WHERE G='Sim'
GROUP BY K
ORDER BY SUM(O) DESC
LIMIT 5
LABEL K 'CATEGORIA', SUM(O) 'SOMA'";
1)

```

---

# 📊 Receita por Estado (Top 5)

```

QUERY(DADOS_TRATADOS!A:O;
"SELECT I, SUM(O)
WHERE G='Sim'
GROUP BY I
ORDER BY SUM(O) DESC
LIMIT 5
LABEL I 'UF', SUM(O) 'SOMA'";
1)

```

---

# 📊 Receita por Vendedor (Top 5)

```

QUERY(DADOS_TRATADOS!A:O;
"SELECT L, SUM(O)
WHERE G='Sim'
GROUP BY L
ORDER BY SUM(O) DESC
LIMIT 5
LABEL L 'VENDEDOR', SUM(O) 'SOMA'";
1)

```

---

# 📊 Receita por Mês (Tendência)

```

QUERY(DADOS_TRATADOS!A:O;
"SELECT D, E, SUM(O)
WHERE G='Sim'
GROUP BY D, E
ORDER BY D, E";
1)

```

---

# 📊 Receita por Ano (Tendência)

```

QUERY(DADOS_TRATADOS!A:O;
"SELECT D, SUM(O)
WHERE G='Sim'
GROUP BY D
ORDER BY D";
1)

```

---

# 🧠 Conceitos Trabalhados

Durante o desenvolvimento do projeto foram explorados os seguintes conceitos:

- Integração de dados de múltiplas tabelas
- Tratamento e preparação de dados
- Criação de variáveis derivadas
- Contagem de valores únicos
- Identificação de pedidos válidos
- Agregação de dados
- Introdução a consultas estilo SQL
- Análise exploratória de dados
- Construção de indicadores de negócio

---

# 🚀 Próximos Passos

Após a criação dos KPIs, o projeto pode evoluir para:

- Construção de **dashboards**
- Visualização de dados
- Análise de crescimento de vendas
- Segmentação de clientes
- Análise geográfica de vendas
- Introdução a ferramentas de BI

---

# 👨‍🏫 Uso Educacional

Este material foi desenvolvido para atividades didáticas na disciplina de **Ciência de Dados**, utilizando ferramentas acessíveis como **Google Planilhas** para introduzir conceitos fundamentais de análise de dados e pensamento analítico.
```
