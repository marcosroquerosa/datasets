📊 Projeto: Análise de Vendas com Dataset Olist (Google Planilhas)

🎯 Objetivo do Estudo

Este projeto tem como objetivo aplicar conceitos introdutórios de Ciência de Dados utilizando o Google Planilhas, a partir de uma versão reduzida do dataset público de e-commerce brasileiro da Olist.

O foco do estudo é:

Entender a estrutura de dados relacionais

Realizar preparação e limpeza de dados

Aplicar funções analíticas no Google Planilhas

Utilizar a função QUERY (semelhante a SQL)

Construir métricas e indicadores (KPIs)

Desenvolver pensamento analítico orientado a negócio



---

📦 Dataset Utilizado

Base original: Brazilian E-Commerce Public Dataset by Olist (Kaggle)

Versão utilizada neste repositório:

Amostra reduzida para uso educacional

Mantida integridade relacional entre tabelas

Aproximadamente 5.000 pedidos


Arquivos incluídos:

olist_orders_dataset.csv

olist_order_items_dataset.csv

olist_customers_dataset.csv

olist_products_dataset.csv

olist_sellers_dataset.csv

olist_order_payments_dataset.csv

olist_order_reviews_dataset.csv

product_category_name_translation.csv



---

🏗️ Etapas do Projeto


---

1️⃣ Preparação e Integração dos Dados

Criada aba:

DADOS_TRATADOS

Estrutura final:

| order_id | data_pedido | status | ano | mes | mes_ano | pedido_valido | customer_id | customer_unique_id | estado_cliente | product_id | categoria | seller_id | price | frete | receita |


---

🔹 Extração de Ano e Mês

Ano:

=ANO(B2)

Mês:

=MÊS(B2)

Mês/Ano:

=TEXTO(B2;"mm/aaaa")


---

🔹 Receita

= M2 + N2

(price + frete)


---

🔹 Identificação de Pedido Válido

=SE(C2="delivered";"Sim";"Não")


---

🔹 Inclusão do customer_unique_id

=PROCV(H2;CUSTOMERS!A:B;2;FALSO)

Importante:
O dataset Olist possui dois identificadores de cliente:

customer_id → identifica o pedido

customer_unique_id → identifica o cliente real


Para métricas corretas de clientes, utilizamos customer_unique_id.


---

2️⃣ Introdução à Função QUERY

Sintaxe utilizada:

=QUERY(intervalo; "consulta"; numero_de_cabecalhos)

Exemplo simples:

=QUERY(DADOS_TRATADOS!A:O; "select A, O"; 1)

Principais comandos utilizados:

SELECT

WHERE

GROUP BY

ORDER BY

LIMIT

LABEL


Observação: A QUERY utiliza a Google Visualization Query Language, semelhante ao SQL, mas não é SQL completo.


---

3️⃣ KPIs Desenvolvidos

Todos os KPIs consideram apenas:

pedido_valido = "Sim"


---

🔹 Receita Total

=SOMASE(DADOS_TRATADOS!G:G;"Sim";DADOS_TRATADOS!O:O)


---

🔹 Total de Pedidos Válidos (únicos)

=COUNTUNIQUE(
  FILTER(
    DADOS_TRATADOS!A:A;
    DADOS_TRATADOS!G:G="Sim"
  )
)


---

🔹 Clientes Únicos

=COUNTUNIQUE(
  FILTER(
    DADOS_TRATADOS!I:I;
    DADOS_TRATADOS!G:G="Sim"
  )
)

(onde I = customer_unique_id)


---

🔹 Ticket Médio

Receita Total / Total de Pedidos

Ou:

=SOMASE(DADOS_TRATADOS!G:G;"Sim";DADOS_TRATADOS!O:O)
/ COUNTUNIQUE(FILTER(DADOS_TRATADOS!A:A;DADOS_TRATADOS!G:G="Sim"))


---

🔹 Receita Média por Cliente

=SOMASE(DADOS_TRATADOS!G:G;"Sim";DADOS_TRATADOS!O:O)
/ COUNTUNIQUE(FILTER(DADOS_TRATADOS!I:I;DADOS_TRATADOS!G:G="Sim"))


---

🔹 Receita por Categoria (Top 5)

=QUERY(DADOS_TRATADOS!A:O;
"select L, sum(O)
 where G = 'Sim'
 group by L
 order by sum(O) desc
 limit 5";
1)


---

🔹 Receita por Estado (Top 5)

=QUERY(DADOS_TRATADOS!A:O;
"select J, sum(O)
 where G = 'Sim'
 group by J
 order by sum(O) desc
 limit 5";
1)


---

🔹 Receita por Mês

=QUERY(DADOS_TRATADOS!A:O;
"select D, E, sum(O)
 where G = 'Sim'
 group by D, E
 order by D, E";
1)


---

📈 Conceitos Trabalhados

Dados transacionais

Chaves primárias e relacionamentos

Agregação

Contagem de valores únicos

Diferença entre pedido e cliente

Ticket Médio vs Receita por Cliente

Agrupamento temporal

Introdução a linguagem estilo SQL



---

🧠 Principais Aprendizados

1. Entender o modelo de dados é essencial antes da análise.


2. Métricas podem mudar completamente dependendo da chave utilizada.


3. Dados brutos precisam ser tratados antes da visualização.


4. QUERY no Google Planilhas permite análises semelhantes a SQL.


5. Análise de dados deve responder perguntas de negócio.




---

🚀 Próximos Passos

Construção de Dashboard interativo

Análise de recorrência de clientes

Cálculo de crescimento mensal

Segmentação por categoria

Introdução a visualização de dados



---

👨‍🏫 Uso Educacional

Este projeto foi desenvolvido para fins didáticos na disciplina de Ciência de Dados, utilizando ferramentas acessíveis para introdução prática aos conceitos fundamentais da área.
