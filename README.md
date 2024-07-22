Here’s the updated README with the project name **AI PDF Chatbot**:

---

# AI PDF Chatbot

**AI PDF Chatbot** is an advanced PDF analyzer that utilizes Generative AI to enable contextual Q&A on file contents. This project integrates LangChain, OpenAI, Redis, and Streamlit to provide an interactive and intelligent PDF querying experience.

## Features

- **PDF Analysis**: Extracts and processes text from PDF files.
- **Contextual Q&A**: Provides answers to questions based on the content of the PDF using a large language model.
- **Retrieval-Augmented Generation (RAG)**: Enhances query responses with relevant context.
- **Chatbot Interface**: User-friendly interface built with Streamlit for interactive querying.
- **Vector Database**: Stores text embeddings and user sessions in Redis for fast retrieval and continuity.

## Requirements

- Python 3.7+
- Required Python packages: `langchain`, `openai`, `streamlit`, `redis`, `PyPDF2`

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/ai-pdf-chatbot.git
   cd ai-pdf-chatbot
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys**

   - Obtain an API key from OpenAI and replace `'your_openai_api_key'` in the code with your actual key.

4. **Start Redis Server**

   Ensure Redis is running on your local machine. You can start it with:

   ```bash
   redis-server
   ```

## Usage

1. **Run the Streamlit App**

   Start the Streamlit application with:

   ```bash
   streamlit run app.py
   ```

2. **Analyze a PDF**

   - Upload a PDF file via the Streamlit interface.
   - Enter a session key to store and retrieve analysis data.

3. **Ask Questions**

   - Once the PDF is analyzed, enter your questions in the Streamlit interface to get answers based on the PDF content.

## Code Overview

- **`pdf_analyzer.py`**: Contains functions for extracting text from PDFs, embedding text using OpenAI, and storing/retrieving data from Redis.
- **`rag_implementation.py`**: Implements retrieval-augmented generation using LangChain and OpenAI's GPT-3.5 Turbo.
- **`app.py`**: Streamlit app for interactive PDF analysis and Q&A.
