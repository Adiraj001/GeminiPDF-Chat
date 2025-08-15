# 📄 GeminiPDF-Chat

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Gemini API](https://img.shields.io/badge/Gemini%20API-Google-brightgreen)


> A simple **PDF Question-Answering Chatbot** built with **Streamlit** and **Google Gemini API**.  
> Upload a PDF, ask questions, and get instant answers — powered by **Gemini 2.0 Flash**.

---

## 🚀 Features
- 📂 **PDF Upload** – Extracts text from uploaded documents.
- 🤖 **AI Chatbot** – Answers based only on the document content.
- ⚡ **Gemini 2.0 Flash** – Fast, accurate responses from Google’s LLM.
- 💬 **Interactive UI** – Streamlit chat interface.
- 🛡 **Error Handling** – Handles missing API key and invalid PDF files.

---

## 📦 Installation & Usage

```bash
# Clone the repository
git clone https://github.com/Adiraj001/GeminiPDF-Chat.git
cd GeminiPDF-Chat

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## ▶️ Usage
```bash
streamlit run app.py
```
- Open your browser – Streamlit will start at http://localhost:8501.
- Enter your Google Gemini API key – Get it here.
- Upload a PDF file – The app will process and extract text.
- Ask questions – Get answers based only on the document content.

## ⚠️ Notes
- The chatbot only answers based on PDF content.
- Accuracy depends on PDF text extraction quality.
- Requires Google Gemini API access.
