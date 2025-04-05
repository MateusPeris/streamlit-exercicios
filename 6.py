import streamlit as st
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import re

st.title("📝 Análise de Texto em Tempo Real")

# Entrada de texto
texto = st.text_area("Digite ou cole seu texto abaixo:", height=250)

if texto:
    # Pré-processamento
    palavras = re.findall(r'\b\w+\b', texto.lower())  # separa palavras ignorando pontuação
    num_palavras = len(palavras)
    num_caracteres = len(texto)

    # Contagem de palavras
    contagem = Counter(palavras)
    palavras_comuns = contagem.most_common(5)

    # Exibir contagens
    st.markdown(f"**🔢 Número de palavras:** {num_palavras}")
    st.markdown(f"**🔡 Número de caracteres:** {num_caracteres}")

    # Exibir as 5 palavras mais frequentes
    st.subheader("🔝 Top 5 palavras mais frequentes:")
    df_freq = pd.DataFrame(palavras_comuns, columns=["Palavra", "Frequência"])
    st.dataframe(df_freq)

    # Gerar e exibir nuvem de palavras
    st.subheader("☁️ Nuvem de Palavras")
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)
else:
    st.info("Digite algum texto para ver a análise.")
