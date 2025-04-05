import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🎯 Sistema de Recomendação de Filmes")

# Preferências do usuário
st.subheader("Selecione os gêneros que você gosta:")
generos = ["Ação", "Comédia", "Drama", "Terror", "Ficção Científica", "Romance"]
preferencias = st.multiselect("Gêneros preferidos:", generos)

# Base de filmes (exemplo simples)
filmes = [
    {"Filme": "Vingadores", "Gêneros": ["Ação", "Ficção Científica"]},
    {"Filme": "Se Beber, Não Case", "Gêneros": ["Comédia"]},
    {"Filme": "O Poderoso Chefão", "Gêneros": ["Drama"]},
    {"Filme": "Invocação do Mal", "Gêneros": ["Terror"]},
    {"Filme": "Interestelar", "Gêneros": ["Ficção Científica", "Drama"]},
    {"Filme": "Titanic", "Gêneros": ["Romance", "Drama"]},
    {"Filme": "Deadpool", "Gêneros": ["Ação", "Comédia"]},
]

# Cálculo da pontuação simples
recomendacoes = []
for filme in filmes:
    score = len(set(filme["Gêneros"]) & set(preferencias))
    if score > 0:
        recomendacoes.append({"Filme": filme["Filme"], "Pontuação": score})

# Mostrar resultados
if preferencias:
    if recomendacoes:
        df_recomendado = pd.DataFrame(recomendacoes).sort_values(by="Pontuação", ascending=False)
        st.subheader("🎬 Recomendações com base nos gêneros selecionados:")
        st.dataframe(df_recomendado)

        # Gráfico de barras
        st.subheader("📊 Pontuação das Recomendações")
        fig = px.bar(df_recomendado, x="Filme", y="Pontuação", text="Pontuação", title="Ranking de Filmes Recomendados")
        st.plotly_chart(fig)
    else:
        st.warning("Nenhum filme encontrado para os gêneros selecionados.")
else:
    st.info("Selecione ao menos um gênero para receber recomendações.")
