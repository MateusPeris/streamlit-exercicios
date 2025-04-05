FROM python:3.11-slim

WORKDIR /app

# Copia tudo
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir streamlit pandas numpy plotly scikit-learn wordcloud matplotlib requests Pillow

# Expor a porta do Streamlit
EXPOSE 8501

# Usar variável de ambiente com fallback para 1.py
ENV EXERCICIO=1.py

# Executar o arquivo especificado
CMD ["sh", "-c", "streamlit run $EXERCICIO --server.port=8501 --server.address=0.0.0.0"]
