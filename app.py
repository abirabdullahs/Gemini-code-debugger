import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
from PIL import Image

load_dotenv()

st.set_page_config(
    page_title="AI Code Debugger",
    layout="centered"
)

st.title("AI Code Debugger")
st.subheader("Developed by Abir Abdullah")
st.write("Upload a screenshot of your code error and let Gemini analyze it.")

default_api_key = os.getenv("GEMINI_API_KEY", "")

api_key = st.text_input(
    "Enter your Gemini API Key",
    value=default_api_key,
    type="password"
)

uploaded_file = st.file_uploader(
    "Upload Error Screenshot",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    st.image(uploaded_file, use_container_width=True)

response_type = st.selectbox(
    "Select Response Type",
    ["Select One", "Hints", "Solution with code"]
)

hint_tab, solution_tab = st.tabs(
    ["Hints", "Solution with code"]
)

if st.button("Debug Code"):

    if not api_key:
        st.error("Please enter your Gemini API Key.")

    elif uploaded_file is None:
        st.error("Please upload an error screenshot.")

    elif response_type == "Select One":
        st.error("Please select a response type.")

    else:
        client = genai.Client(api_key=api_key)

        image = Image.open(uploaded_file)

        if response_type == "Hints":
            prompt = """
You are an expert programming mentor.

Analyze the uploaded code error screenshot.

Provide:
- Error explanation
- Possible causes
- Helpful hints

Do not provide the complete corrected code.
"""
        else:
            prompt = """
You are an expert software engineer.

Analyze the uploaded code error screenshot.

Provide:
1. Error explanation
2. Why the error occurred
3. Step-by-step solution
4. Corrected code
5. Best practices
"""

        with st.spinner("Analyzing..."):

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[
                    prompt,
                    image
                ]
            )

        if response_type == "Hints":
            with hint_tab:
                st.markdown(response.text)

        else:
            with solution_tab:
                st.markdown(response.text)
