from langchain import LangChain
from openai import GPT3Turbo

def initialize_rag():
    langchain = LangChain()
    gpt = GPT3Turbo(api_key='your_openai_api_key')
    return langchain, gpt

def generate_response_with_rag(question, context):
    langchain, gpt = initialize_rag()
    retrieved_context = langchain.retrieve_relevant_documents(question, context)
    response = gpt.generate_response(question, retrieved_context)
    return response
