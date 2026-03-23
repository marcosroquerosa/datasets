# 🎬 Análise de Filmes de Maior Bilheteria com Pandas

Projeto de Ciência de Dados para análise de filmes utilizando Python e Pandas, com foco em limpeza, transformação e exploração de dados reais do IMDb.
Fonte de Dados: https://www.imdb.com/pt/list/ls059930570/ 
---

## 📌 Objetivo

Transformar um dataset bruto de filmes em um dataset analítico estruturado, permitindo responder perguntas como:

- Quais filmes tiveram maior bilheteria?
- Existe relação entre nota IMDb e bilheteria?
- Quais gêneros são mais bem avaliados?
- Quais diretores aparecem com mais frequência?

---

## 📂 Dataset

O dataset contém informações sobre filmes de maior bilheteria, com as seguintes colunas:

| Coluna | Descrição |
|------|--------|
| Position | Ranking |
| Const | ID IMDb |
| Created | Data de criação |
| Modified | Data de modificação |
| Description | Contém status + bilheteria |
| Title | Nome do filme |
| Original Title | Nome original |
| URL | Link IMDb |
| Title Type | Tipo (Filme) |
| IMDb Rating | Nota IMDb |
| Runtime (mins) | Duração |
| Year | Ano |
| Genres | Gêneros |
| Num Votes | Número de votos |
| Release Date | Data de lançamento |
| Directors | Diretores |

---

## ⚠️ Problemas do Dataset (Importante)

Antes de qualquer análise, o dataset possui problemas críticos:

- Bilheteria está dentro da coluna `Description`
- Datas estão como texto
- Gêneros estão agrupados em uma única string
- Algumas colunas numéricas estão como string

Se você ignorar isso, sua análise estará errada.

---

## 🛠️ Tecnologias

- Python 3.x
- Pandas
- NumPy (opcional)

---

## 🚀 Pipeline de Análise

### 1. Carregar 
### 2. Explorar
### 3. Limpar (tipos + bilheteria)
### 4. Transformar (features)
### 5. Analisar
### 6. Exportar

👨‍🏫 Uso Educacional

Este projeto foi desenvolvido para ensino de:

Ciência de Dados
Pandas
Análise Exploratória

Ideal para cursos técnicos e graduação.
