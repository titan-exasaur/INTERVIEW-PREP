from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv() # loading the creds

model = ChatOpenAI(model="gpt-4",
                   temperature=0.5,
                   max_completion_tokens=10)

result = model.invoke("What is the capital of Ukraine?")

print(result.content)