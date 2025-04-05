import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("💰 Simulador de Investimento com Juros Compostos")

# Entradas do usuário
valor_inicial = st.number_input("Valor Inicial (R$)", min_value=0.0, value=1000.0, step=100.0)
taxa_juros = st.slider("Taxa de Juros Anual (%)", min_value=0.0, max_value=20.0, value=5.0, step=0.1)
anos = st.selectbox("Período de Investimento (anos)", options=list(range(1, 31)), index=4)

# Cálculo do montante ao longo do tempo
anos_lista = np.arange(0, anos + 1)
montantes = valor_inicial * (1 + taxa_juros / 100) ** anos_lista

# Criar DataFrame para o gráfico
df_investimento = pd.DataFrame({
    "Ano": anos_lista,
    "Montante (R$)": montantes
})

# Mostrar resultado final
montante_final = montantes[-1]
st.markdown(f"### 💵 Montante Final após {anos} anos: **R$ {montante_final:,.2f}**")

# Gráfico de crescimento
fig = px.line(df_investimento, x="Ano", y="Montante (R$)", markers=True,
              title="Crescimento do Investimento ao Longo do Tempo")
st.plotly_chart(fig)
