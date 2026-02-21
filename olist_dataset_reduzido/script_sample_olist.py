import pandas as pd
import os

# ==============================
# CONFIGURAÇÃO
# ==============================

CAMINHO_ORIGINAL = "dataset_original"   # pasta com CSVs originais
CAMINHO_SAIDA = "dataset_reduzido"      # pasta para salvar versão reduzida
TAMANHO_AMOSTRA = 5000                  # número de pedidos desejado

os.makedirs(CAMINHO_SAIDA, exist_ok=True)

# ==============================
# 1. CARREGAR DATASETS
# ==============================

orders = pd.read_csv(f"{CAMINHO_ORIGINAL}/olist_orders_dataset.csv")
order_items = pd.read_csv(f"{CAMINHO_ORIGINAL}/olist_order_items_dataset.csv")
order_payments = pd.read_csv(f"{CAMINHO_ORIGINAL}/olist_order_payments_dataset.csv")
order_reviews = pd.read_csv(f"{CAMINHO_ORIGINAL}/olist_order_reviews_dataset.csv")
customers = pd.read_csv(f"{CAMINHO_ORIGINAL}/olist_customers_dataset.csv")
products = pd.read_csv(f"{CAMINHO_ORIGINAL}/olist_products_dataset.csv")
sellers = pd.read_csv(f"{CAMINHO_ORIGINAL}/olist_sellers_dataset.csv")
geolocation = pd.read_csv(f"{CAMINHO_ORIGINAL}/olist_geolocation_dataset.csv")
category_translation = pd.read_csv(f"{CAMINHO_ORIGINAL}/product_category_name_translation.csv")

# ==============================
# 2. AMOSTRAR PEDIDOS
# ==============================

orders_sample = orders.sample(n=TAMANHO_AMOSTRA, random_state=42)

# ==============================
# 3. FILTRAR TABELAS RELACIONADAS
# ==============================

# Filtrar order_items
order_items_sample = order_items[
    order_items["order_id"].isin(orders_sample["order_id"])
]

# Filtrar payments
order_payments_sample = order_payments[
    order_payments["order_id"].isin(orders_sample["order_id"])
]

# Filtrar reviews
order_reviews_sample = order_reviews[
    order_reviews["order_id"].isin(orders_sample["order_id"])
]

# Filtrar customers
customers_sample = customers[
    customers["customer_id"].isin(orders_sample["customer_id"])
]

# Identificar produtos e vendedores usados
produtos_usados = order_items_sample["product_id"].unique()
vendedores_usados = order_items_sample["seller_id"].unique()

products_sample = products[
    products["product_id"].isin(produtos_usados)
]

sellers_sample = sellers[
    sellers["seller_id"].isin(vendedores_usados)
]

# Filtrar geolocalização apenas pelos ZIP usados
geolocation_sample = geolocation[
    geolocation["geolocation_zip_code_prefix"].isin(
        customers_sample["customer_zip_code_prefix"]
    )
]

# ==============================
# 4. SALVAR NOVOS CSVs
# ==============================

orders_sample.to_csv(f"{CAMINHO_SAIDA}/olist_orders_dataset.csv", index=False)
order_items_sample.to_csv(f"{CAMINHO_SAIDA}/olist_order_items_dataset.csv", index=False)
order_payments_sample.to_csv(f"{CAMINHO_SAIDA}/olist_order_payments_dataset.csv", index=False)
order_reviews_sample.to_csv(f"{CAMINHO_SAIDA}/olist_order_reviews_dataset.csv", index=False)
customers_sample.to_csv(f"{CAMINHO_SAIDA}/olist_customers_dataset.csv", index=False)
products_sample.to_csv(f"{CAMINHO_SAIDA}/olist_products_dataset.csv", index=False)
sellers_sample.to_csv(f"{CAMINHO_SAIDA}/olist_sellers_dataset.csv", index=False)
geolocation_sample.to_csv(f"{CAMINHO_SAIDA}/olist_geolocation_dataset.csv", index=False)
category_translation.to_csv(f"{CAMINHO_SAIDA}/product_category_name_translation.csv", index=False)

print("Dataset reduzido criado com sucesso!")
