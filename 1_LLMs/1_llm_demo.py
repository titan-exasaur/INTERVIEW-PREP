from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv() #loading the creds

llm = OpenAI(model="gpt-3.5-turbo-instruct")

result = llm.invoke("What is the capital of norway?")

print(result)