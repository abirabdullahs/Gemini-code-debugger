# Gemini Code Debugger

An AI-powered Streamlit application that analyzes programming error screenshots using the Gemini API.

## Features

- Upload error screenshots (PNG, JPG, JPEG)
- Get debugging hints
- Get complete solution with corrected code
- Gemini AI integration
- Simple and responsive UI

## Installation

Clone the repository

```bash
git clone <repository_link>
```

Go to the project directory

```bash
cd project_name
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- Pillow
- python-dotenv

## Project Structure

```
Code-Debugger/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```
