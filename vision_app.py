import google.generativeai as genai
import os
import streamlit as st
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv()

os.getenv("GIMINI_API_KEY")
genai.configure(api_key=os.getenv("GIMINI_API_KEY"))

# API_KEY = os.getenv("GIMINI_API_KEY")

# if API_KEY is None:
#     st.error("GEMINI_API_KEY is missing. check your environment variables.")
# else:
#     genai.configure(api_key=API_KEY)

# Load Gemini model
model = genai.GenerativeModel("models/gemini-2.0-flash")


def get_gemini_response(input_text="", image=None):
    """
    Generates a response using Gemini Pro Vision.
    
    Args:
        input_text (str, optional): Text prompt (default is empty).
        image (PIL.Image, optional): Image input (default is None).

    Returns:
        str: The generated response.
    """
    query = []
    if input_text:
        query.append(input_text)
    if image:
        query.append(image)
    
    if not query:
        return "Error: Please provide either text or an image."
    
    response = model.generate_content(query)
    return response.text


# Initialize the Streamlit app
st.set_page_config(page_title="Gemini Q&A App", page_icon="🔮", layout="wide")
st.header("Q&A with Gemini")

# User input
input_text = st.text_input("Ask a question")
uploaded_file = st.file_uploader("Upload an image (optional)...",
                                 type=["jpg", "jpeg", "png"])

image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Submit button
submit = st.button("Get Response")

if submit:
    if not input_text and not image:
        st.error("Please provide either a question or an image.")
    else:
        response = get_gemini_response(input_text, image)
        st.subheader("The Response is:")
        st.write(response)
