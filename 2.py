import streamlit as st
import pandas as pd
import numpy as np

st.title("🔍 Filtro Dinâmico em Tabela")

# Gerar conjunto de dados exemplo
np.random.seed(42)
df = pd.DataFrame({
    "Cidade": np.random.choice(["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"], size=200),
    "Categoria": np.random.choice(["A", "B", "C"], size=200),
    "Idade": np.random.randint(18, 65, size=200),
    "Salário": np.random.normal(3000, 1000, size=200).astype(int)
})

st.subheader("Filtros")

# Filtros categóricos
cidades = st.multiselect("Filtrar por Cidade:", options=df["Cidade"].unique(), default=df["Cidade"].unique())
categorias = st.multiselect("Filtrar por Categoria:", options=df["Categoria"].unique(), default=df["Categoria"].unique())

# Filtros numéricos
idade_min, idade_max = int(df["Idade"].min()), int(df["Idade"].max())
salario_min, salario_max = int(df["Salário"].min()), int(df["Salário"].max())

idade_range = st.slider("Faixa de Idade:", min_value=idade_min, max_value=idade_max, value=(idade_min, idade_max))
salario_range = st.slider("Faixa de Salário:", min_value=salario_min, max_value=salario_max, value=(salario_min, salario_max))

# Aplicando os filtros
df_filtrado = df[
    (df["Cidade"].isin(cidades)) &
    (df["Categoria"].isin(categorias)) &
    (df["Idade"].between(*idade_range)) &
    (df["Salário"].between(*salario_range))
]

st.subheader("Tabela Filtrada")
st.dataframe(df_filtrado)
