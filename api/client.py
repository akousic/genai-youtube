import requests
import streamlit as st


def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
                             json={"input": {'topic': input_text}})

    return response.json()["output"]["content"]


def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json={"input": {'topic': input_text}})

    return response.json()
    # streamlit framework


st.title('Langchain Demo With LLAMA2 API')
input_text = st.text_input("Write an essay on - (Powered by OpenAI)")
input_text1 = st.text_input("Write a poem on - (Powered by local llama2)")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))
