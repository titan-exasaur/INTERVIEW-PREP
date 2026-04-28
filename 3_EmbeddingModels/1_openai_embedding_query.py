from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv() # loading creds

embedding = OpenAIEmbeddings(model='text-embedding-3-large',
                 dimensions=32)

result = embedding.embed_query("Bangalore is the capital of bangalore")

print(str(result))