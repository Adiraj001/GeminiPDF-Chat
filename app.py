import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader 
import os


st.set_page_config(page_title="Chatbot with Gemini AI" , layout="centered")

st.title("Chatbot with Google Gemini API")
# --- API Key Input ---
st.subheader("Enter your Google Gemini API Key")
api_key = st.text_input(
    "Google Gemini API Key",
    type="password",
    help="Get your API key from https://makersuite.google.com/app/apikey",
    key="gemini_api_key_input"
)

if api_key:
    genai.configure(api_key=api_key)
    st.success("API Key configured!")
else:
    st.warning("Please enter your Google Gemini API Key to proceed.")


st.subheader("Upload your PDF Document")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

pdf_text = st.session_state.get('pdf_text', '')

if uploaded_file is not None:
    
    if 'last_uploaded_file_name' not in st.session_state or st.session_state.last_uploaded_file_name != uploaded_file.name:
        st.session_state.last_uploaded_file_name = uploaded_file.name
        st.info("Processing PDF... Please wait.")
        try:
            reader = PdfReader(uploaded_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            st.session_state.pdf_text = text # Store in session state
            st.session_state.chat_history = [] # Clear chat history on new PDF upload
            st.success("PDF loaded successfully! You can now ask questions.")
            pdf_text = text # Update local variable for immediate use
        except Exception as e:
            st.error(f"Error reading PDF: {e}")
            st.session_state.pdf_text = "" # Clear text on error
    else:
        st.info("PDF already loaded.")
else:
    st.session_state.pdf_text = "" # Clear PDF text if no file is uploaded

# --- Chat Interface ---
st.subheader("3. Chat with your PDF")

# Initialize chat history in session state if not present
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Display chat messages
chat_container = st.container()
with chat_container:
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input from user
if pdf_text and api_key:
    user_question = st.chat_input("Ask a question about the PDF...")
    if user_question:
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_question})
        with st.chat_message("user"):
            st.markdown(user_question)

        with st.spinner("Getting response..."):
            try:
                # Construct the prompt for the LLM
                # We tell the LLM to answer based ONLY on the provided text.
                prompt = f"""Based on the following document content, answer the question.
                If the answer is not found in the document, state that you cannot find the answer in the provided document.

                Document Content:
                \"\"\"
                {pdf_text}
                \"\"\"

                Question: \"{user_question}\""""

                # Initialize the generative model
                model = genai.GenerativeModel('gemini-2.0-flash')

                # Generate content
                response = model.generate_content(prompt)

                
                bot_response = response.text
                st.session_state.chat_history.append({"role": "assistant", "content": bot_response})
                with st.chat_message("assistant"):
                    st.markdown(bot_response)

            except Exception as e:
                st.error(f"Error communicating with Gemini API: {e}")
                st.session_state.chat_history.append({"role": "assistant", "content": f"Sorry, I encountered an error: {e}"})
                with st.chat_message("assistant"):
                    st.markdown(f"Sorry, I encountered an error: {e}")
elif not pdf_text and uploaded_file is not None:
    st.info("Please wait for the PDF to finish processing, or upload a PDF.")
else:
    st.info("Upload a PDF and enter your API key to start chatting!")


st.markdown("---")
st.markdown("Made by Adiraj")