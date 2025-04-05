import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.express as px

st.title("📈 Previsão de Notas com Regressão Linear")

# Simular dados históricos de treino
np.random.seed(42)
horas_estudo = np.random.randint(1, 10, 50)
nota_anterior = np.random.randint(50, 100, 50)
nota_final = 0.4 * horas_estudo + 0.6 * (nota_anterior / 10) + np.random.normal(0, 2, 50)
df_treino = pd.DataFrame({
    "Horas de Estudo": horas_estudo,
    "Nota Anterior": nota_anterior,
    "Nota Final": nota_final
})

# Treinar o modelo
X = df_treino[["Horas de Estudo", "Nota Anterior"]]
y = df_treino["Nota Final"]
modelo = LinearRegression()
modelo.fit(X, y)

# Inputs do usuário
st.subheader("📋 Insira os dados para previsão:")
horas = st.slider("Horas de Estudo", 0, 12, 4)
nota_prev = st.slider("Nota Anterior", 0, 100, 70)

# Previsão
entrada = np.array([[horas, nota_prev]])
previsao = modelo.predict(entrada)[0]

st.markdown(f"### 🎯 Nota Prevista: **{previsao:.2f}**")

# Mostrar gráfico com ponto previsto
df_plot = df_treino.copy()
df_plot["Tipo"] = "Histórico"
novo_ponto = pd.DataFrame({
    "Horas de Estudo": [horas],
    "Nota Anterior": [nota_prev],
    "Nota Final": [previsao],
    "Tipo": ["Previsão"]
})
df_plot = pd.concat([df_plot, novo_ponto], ignore_index=True)

fig = px.scatter(df_plot, x="Horas de Estudo", y="Nota Final", color="Tipo",
                 size=np.where(df_plot["Tipo"] == "Previsão", 10, 5),
                 title="Notas em Função das Horas de Estudo")
st.plotly_chart(fig)
