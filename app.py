import streamlit as st
from pdf_analyzer import analyze_pdf, get_contextual_answer

# Initialize the Redis client
import redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

st.title('QueryPDF Chatbot')

pdf_file = st.file_uploader("Upload a PDF", type="pdf")
session_key = st.text_input("Enter Session Key")

if pdf_file and session_key:
    st.write("Analyzing PDF...")
    analyze_pdf(pdf_file, session_key)
    st.write("PDF Analyzed and stored in Redis.")

if session_key:
    question = st.text_input("Ask a question about the PDF")
    if st.button("Get Answer"):
        answer = get_contextual_answer(question, session_key)
        st.write(f"Answer: {answer}")
