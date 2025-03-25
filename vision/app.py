from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-2.0-flash-exp")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

input=st.text_input("input: ",key="input")
submit=st.button("Ask the question")

## After Submission
if submit:
    response=get_gemini_response(input)
    st.subheader("Response: ")
    st.write(response)

