import PyPDF2
import openai
from langchain import LangChain
import redis

# Initialize OpenAI and Redis
openai.api_key = 'your_openai_api_key'
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def extract_text_from_pdf(pdf_path):
    pdf_reader = PyPDF2.PdfFileReader(pdf_path)
    text = ""
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extract_text()
    return text

def embed_text(text):
    response = openai.Embedding.create(input=text, engine='text-embedding-ada-002')
    return response['data'][0]['embedding']

def store_in_redis(text, embedding, key):
    redis_client.set(key, text)
    redis_client.set(f"{key}_embedding", embedding)

def get_contextual_answer(question, key):
    text = redis_client.get(key).decode('utf-8')
    embedding = redis_client.get(f"{key}_embedding")
    # Use LangChain to process the question with context
    chain = LangChain()
    answer = chain.generate_response(question, text, embedding)
    return answer

def analyze_pdf(pdf_path, key):
    text = extract_text_from_pdf(pdf_path)
    embedding = embed_text(text)
    store_in_redis(text, embedding, key)
