import streamlit as st
import pandas as pd
import numpy as np

st.title("🗺️ Mapa Interativo com Pontos Geográficos")

# Gerar dados fictícios com categorias
np.random.seed(42)
categorias = ["Restaurante", "Parque", "Museu"]
data = pd.DataFrame({
    "Latitude": np.random.uniform(-23.7, -23.5, 100),
    "Longitude": np.random.uniform(-46.7, -46.5, 100),
    "Categoria": np.random.choice(categorias, 100)
})

# Filtro por categoria
categoria_selecionada = st.selectbox("Selecione uma categoria para exibir no mapa:", categorias)

# Filtrar dados com base na categoria
dados_filtrados = data[data["Categoria"] == categoria_selecionada]

st.subheader(f"📍 Exibindo pontos da categoria: {categoria_selecionada}")

# Renomear colunas para compatibilidade com st.map
map_data = dados_filtrados.rename(columns={"Latitude": "latitude", "Longitude": "longitude"})
st.map(map_data[['latitude', 'longitude']])
