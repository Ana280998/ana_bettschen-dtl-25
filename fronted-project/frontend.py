from dotenv import load_dotenv
import os
import requests
import streamlit as st

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")
OPENROUTER_TOKEN = os.getenv("OPENROUTER_TOKEN")

st.sidebar.title("Configuracion")
st.sidebar.write("API_BASE_URL:", API_BASE_URL or "No configurado")
st.sidebar.write("OPENROUTER_TOKEN:", (OPENROUTER_TOKEN[:10] + "...") if OPENROUTER_TOKEN else "No configurado")

if not API_BASE_URL or not OPENROUTER_TOKEN:
    st.error("Faltan variables de entorno. Revisa tu archivo .env.")
    st.stop()

user_input = st.text_input("Escribe algo:", "Hola")

if st.button("Enviar"):
    try:
        url = f"{API_BASE_URL}/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENROUTER_TOKEN}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "mistralai/mistral-7b-instruct:free",
            "messages": [
                {"role": "user", "content": user_input}
            ]
        }

        response = requests.post(url, headers=headers, json=data)

        st.write("Respuesta cruda del servidor:")
        st.code(response.text)

        try:
            json_data = response.json()
            st.success("Respuesta del modelo:")
            st.write(json_data)
        except json.JSONDecodeError:
            st.error("El servidor no devolvió JSON válido. Verifica el endpoint o el token.")

    except Exception as e:
        st.error(f"Error al procesar la solicitud: {e}")
