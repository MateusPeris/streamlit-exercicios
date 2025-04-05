# 📆 Projeto: Exercícios com Streamlit e Docker

Este projeto contém uma série de aplicações interativas desenvolvidas com **Streamlit**, organizadas em arquivos separados, cada um focado em um tema diferente como visualização, processamento de texto, mapas, machine learning e APIs externas. O projeto também está configurado com **Docker** e **docker-compose** para facilitar a execução de cada exercício individualmente.

---

## 🚀 Como executar

### ✅ Usando Docker Compose (recomendado)

1. Faça o build de todos os serviços:

```bash
docker compose build
```

2. Rode o exercício desejado:

```bash
docker compose up exercicio5
```

3. Rode todos exercícios:

```bash
docker compose up
```   

4. Acesse no navegador:

| Exercício     | URL                      |
|---------------|---------------------------|
| Ex. 1         | http://localhost:8501     |
| Ex. 2         | http://localhost:8502     |
| Ex. 3         | http://localhost:8503     |
| Ex. 4         | http://localhost:8504     |
| Ex. 5         | http://localhost:8505     |
| Ex. 6         | http://localhost:8506     |
| Ex. 7         | http://localhost:8507     |
| Ex. 8         | http://localhost:8508     |
| Ex. 9         | http://localhost:8509     |
| Ex. 10        | http://localhost:8510     |

> ⚠️ Para o exercício 10 (API de Clima), edite o arquivo `docker-compose.yml` e substitua `SUA_CHAVE_AQUI` pela sua chave da API OpenWeather.

---

## 📂 Estrutura do Projeto

```
.
├── 1.py                      # Dashboard com upload de CSV, análise estatística e histograma           
├── 2.py                      # Tabela com filtros dinâmicos (multiselect e sliders)
├── 3.py                      # Simulador de investimento com gráfico de crescimento
├── 4.py                      # Mapa interativo com pontos e categorias
├── 5.py                      # Formulário com validação e resposta
├── 6.py                      # Análise de texto com contagem e nuvem de palavras
├── 7.py                      # Recomendacão de filmes com gráfico de pontuação
├── 8.py                      # Previsão de notas com regressão linear
├── 9.py                      # Painel multipágina com cache
├── 10.py                     # Consulta de clima via API externa (OpenWeatherMap)
├── Dockerfile                # Imagem base com suporte a Streamlit
├── docker-compose.yml        # Execução separada por porta para cada exercício
└── .gitignore                # Arquivos a serem ignorados pelo Git
```

---

## 📄 Requisitos (se quiser rodar localmente sem Docker)

```bash
pip install streamlit pandas numpy matplotlib plotly scikit-learn wordcloud requests Pillow
```

---

## 🌤️ Sobre o exercício 10 (API de Clima)

1. Crie uma conta gratuita em https://openweathermap.org
2. Copie sua chave da API
3. No `docker-compose.yml`, substitua:

```yaml
- API_KEY=SUA_CHAVE_AQUI
```

por:

```yaml
- API_KEY=coloque_sua_chave_aqui
```
