from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro model and get responses
model = genai.GenerativeModel("learnlm-1.5-pro-experimental")
def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Gemini Vision")
st.header("Gemini Vision Application")

input=st.text_input("Input Prompt: ",key="input")

# Image upload section
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   

if uploaded_file is not None:
    # Convert the file to an image
    image = Image.open(uploaded_file)
    # Display the image
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Get the response from Gemini
submit=st.button("Tell me about the image")

if submit:
    if uploaded_file is None:
        st.warning("Please upload an image first!")
    else:
        response=get_gemini_response(input,image)
        st.subheader("The Response is")
        st.write(response)
