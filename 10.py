import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Chave de API da OpenWeatherMap
API_KEY = 'sua_chave_de_api_aqui'  # Substitua pelo seu API Key

# URL base da API de clima
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Função para obter dados climáticos
def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'pt_br'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Interface do usuário com Streamlit
st.title('🌤️ Aplicativo de Clima')

# Entrada do usuário
city = st.text_input('Digite o nome da cidade:', '')

if city:
    weather_data = get_weather(city)
    if weather_data:
        # Processando os dados recebidos
        temperatura = weather_data['main']['temp']
        umidade = weather_data['main']['humidity']
        descricao = weather_data['weather'][0]['description'].capitalize()
        icone = weather_data['weather'][0]['icon']

        # Exibindo as informações
        st.subheader(f'Condições atuais em {city.capitalize()}:')
        st.write(f'**Temperatura:** {temperatura}°C')
        st.write(f'**Umidade:** {umidade}%')
        st.write(f'**Condição:** {descricao}')

        # Obtendo e exibindo o ícone do clima
        icon_url = f'http://openweathermap.org/img/wn/{icone}@2x.png'
        response = requests.get(icon_url)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            st.image(image, caption=descricao)
        else:
            st.write('Ícone não disponível.')
    else:
        st.error('Cidade não encontrada. Verifique o nome e tente novamente.')
