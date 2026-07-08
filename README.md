# gemini Code Debugger

An AI-powered Streamlit application that analyzes programming error screenshots using Google's Gemini API.

## Features

- Upload error screenshots (PNG, JPG, JPEG)
- Enter your own Gemini API Key
- Get debugging hints
- Get complete solution with corrected code
- Clean and simple Streamlit interface

---

## Installation

Clone the repository

```bash
git clone <repository_url>
```

Move into the project folder

```bash
cd Code-Debugger
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the app

```bash
streamlit run app.py
```

---

## How to Use

1. Enter your Gemini API Key.
2. Upload a screenshot of your code error.
3. Select the response type.
4. Click **Debug Code**.
5. Gemini will analyze the screenshot and generate the response.

---

## Get a Gemini API Key

You can create a free Gemini API key from:

https://aistudio.google.com/app/apikey

---

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- Pillow
- python-dotenv

---

## Project Structure

```
Code-Debugger/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

## Requirements

- Python 3.10+
- Internet Connection
- Gemini API Key
