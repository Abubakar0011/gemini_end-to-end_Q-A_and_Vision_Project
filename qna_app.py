import google.generativeai as genai
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


os.getenv("GIMINI_API_KEY")
genai.configure(api_key=os.getenv("GIMINI_API_KEY"))

# Loading gemini model

model = genai.GenerativeModel("models/gemini-1.5-pro")


def get_response(question):
    response = model.generate_content(question)
    return response.text


# Initializing the app
st.set_page_config(page_title="Q&A", page_icon="🔮", layout="wide")

st.header("Q&A with Gemini")

input = st.text_input("Ask a question")
submit = st.button("Submit")

if submit:
    response = get_response(input)
    st.subheader("The response is:")
    st.write(response)
