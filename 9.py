import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Painel Multi-página", layout="wide")
st.title("📚 Painel Multi-página com Cache")

# Sidebar de navegação
pagina = st.sidebar.radio("Navegar entre as páginas:", ["1. Upload e Visualização", "2. Análise Estatística", "3. Gráficos Interativos"])

# Página 1: Upload e visualização
if pagina.startswith("1"):
    st.header("📥 Página 1: Upload e Visualização de Dados")
    uploaded_file = st.file_uploader("Envie seu arquivo CSV:", type=["csv"])
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.session_state["dados"] = df  # salvar em session_state
        st.dataframe(df)
    elif "dados" in st.session_state:
        st.info("Usando dados carregados anteriormente.")
        st.dataframe(st.session_state["dados"])
    else:
        st.warning("Por favor, envie um arquivo CSV.")

# Página 2: Análise estatística
elif pagina.startswith("2"):
    st.header("📊 Página 2: Análise Estatística dos Dados")

    if "dados" in st.session_state:
        df = st.session_state["dados"]

        # Usando cache para cálculos estatísticos
        @st.cache_data
        def calcular_estatisticas(dados):
            return dados.describe()

        st.subheader("Resumo Estatístico")
        st.dataframe(calcular_estatisticas(df.select_dtypes(include="number")))
    else:
        st.error("Você precisa carregar um arquivo na Página 1.")

# Página 3: Gráficos interativos
elif pagina.startswith("3"):
    st.header("📈 Página 3: Gráficos Interativos")

    if "dados" in st.session_state:
        df = st.session_state["dados"]

        cols_numericas = df.select_dtypes(include="number").columns.tolist()

        if len(cols_numericas) >= 2:
            x_col = st.selectbox("Eixo X:", cols_numericas)
            y_col = st.selectbox("Eixo Y:", cols_numericas, index=1)

            fig = px.scatter(df, x=x_col, y=y_col, title=f"{y_col} vs {x_col}", size_max=60)
            st.plotly_chart(fig)
        else:
            st.warning("São necessárias pelo menos duas colunas numéricas para o gráfico.")
    else:
        st.error("Você precisa carregar um arquivo na Página 1.")
