import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Dashboard de Análise de Dados")

# Upload do arquivo CSV
uploaded_file = st.file_uploader("Faça upload de um arquivo CSV", type=["csv"])

if uploaded_file is not None:
    # Leitura do CSV
    df = pd.read_csv(uploaded_file)

    st.subheader("Prévia dos Dados")
    st.dataframe(df)

    # Seleção de coluna numérica
    numeric_cols = df.select_dtypes(include='number').columns.tolist()

    if numeric_cols:
        selected_col = st.selectbox("Selecione uma coluna numérica para análise:", numeric_cols)

        # Cálculos estatísticos
        mean_val = df[selected_col].mean()
        median_val = df[selected_col].median()
        std_val = df[selected_col].std()

        st.markdown(f"**Média:** {mean_val:.2f}")
        st.markdown(f"**Mediana:** {median_val:.2f}")
        st.markdown(f"**Desvio Padrão:** {std_val:.2f}")

        # Gráfico interativo
        st.subheader("Histograma")
        fig = px.histogram(df, x=selected_col, nbins=20, title=f"Distribuição de {selected_col}")
        st.plotly_chart(fig)
    else:
        st.warning("O arquivo não possui colunas numéricas para análise.")
else:
    st.info("Por favor, envie um arquivo CSV para começar.")
