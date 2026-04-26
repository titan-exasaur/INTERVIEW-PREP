from google import genai

client = genai.Client(api_key="AIzaSyD3mdM-sk6rgAZBEWulA48TUbYFTUQPIyc")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is Quantum Mechanics?"
)

print(response.text)