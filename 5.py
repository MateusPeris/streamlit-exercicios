import streamlit as st

st.title("📝 Formulário com Validação")

# Sessão para armazenar estado de "limpar"
if "submitted" not in st.session_state:
    st.session_state["submitted"] = False

# Formulário
with st.form("formulario_usuario"):
    nome = st.text_input("Nome:")
    idade = st.number_input("Idade:", min_value=0, max_value=120, step=1)
    cores = st.multiselect("Quais cores você gosta?", ["Azul", "Verde", "Vermelho", "Amarelo", "Preto", "Branco"])

    submitted = st.form_submit_button("Enviar")
    limpar = st.form_submit_button("Limpar")

# Ação ao enviar
if submitted:
    if nome and 0 <= idade <= 120:
        st.session_state["submitted"] = True
        st.success(f"Olá, **{nome}**, com **{idade}** anos, você gosta de: **{', '.join(cores) if cores else 'nenhuma cor selecionada'}**!")
    else:
        st.error("Por favor, preencha todos os campos corretamente.")

# Ação ao limpar
if limpar:
    st.session_state["submitted"] = False
    st.experimental_rerun()
