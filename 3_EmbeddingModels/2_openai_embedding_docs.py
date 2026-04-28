from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv() # loading creds

embedding = OpenAIEmbeddings(model='text-embedding-3-large',
                 dimensions=32)

documents = [
    "Kolkata is capital of west bengal",
    "Delhi is capital of India",
    "Chennai is capital of Tamil Nadu"
]

result = embedding.embed_documents(documents)

print(str(result))