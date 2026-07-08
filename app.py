import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
from PIL import Image


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


st.set_page_config(
    page_title="AI Code Debugger",
    page_icon="",
    layout="centered"
)

st.title("AI Code Debugger")
st.write("Upload your code error screenshot and let Gemini analyze the error.")


uploaded_file = st.file_uploader(
    "Upload Error Screenshot",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Screenshot", use_container_width=True)


response_type = st.selectbox(
    "Select Response Type",
    ["Select One", "Hints", "Solution with code"]
)


hint_tab, solution_tab = st.tabs(
    ["Hints", "Solution with code"]
)


if st.button("Debug Code"):

    if uploaded_file is None:
        st.error("Please upload an error screenshot.")

    elif response_type == "Select One":
        st.error("Please select a response type.")

    else:

        with st.spinner("Analyzing your screenshot..."):

            image = Image.open(uploaded_file)

            if response_type == "Hints":

                prompt = """
You are an expert programming mentor.

Analyze the uploaded code error screenshot.

Provide:
- Error explanation
- Possible causes
- Helpful hints

Do NOT provide the complete corrected code.
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

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[prompt, image]
            )

            if response_type == "Hints":
                with hint_tab:
                    st.markdown(response.text)

            else:
                with solution_tab:
                    st.markdown(response.text)
